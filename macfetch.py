import platform
import psutil
import socket
import os
import cpuinfo
import gpuinfo
import uuid
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress
from datetime import datetime
from rich import box
from rich.align import Align

console = Console()

ascii_art = """
c,_.--.,y
            7 a.a(
           (   ,_Y)
           :  '---;
       ___.'\\.  - (
     .'"""S,._'--'_2..,_
     |    ':::::=:::::  \
     .     f== ;-,---.' T
      Y.   r,-,_/_      |
      |:\___.---' '---./
      |'`             )
       \\             ,
       ':;,.________.;L
       /  '---------' |
       |              \\
       L---'-,--.-'--,-'
        T    /   \\   Y
        |   Y    ,   |
        |   \\    (   |
        (   )     \\,_L
        7-./      )  `,
snd    /  _(      '._  \
     '---'           '--'
"""

def get_system_info():
    return {
        'OS': platform.system(),
        'OS Version': platform.version(),
        'Architecture': platform.architecture()[0],
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical CPUs': psutil.cpu_count(logical=True),
        'Memory (GB)': f"{psutil.virtual_memory().total / (1024 ** 3):.2f}",
        'Swap Memory (GB)': f"{psutil.swap_memory().total / (1024 ** 3):.2f}",
        'Hostname': socket.gethostname(),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'MAC Address': ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    }

def get_gpu_info():
    try:
        return gpuinfo.get_info()
    except Exception as e:
        return str(e)

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info.get('brand_raw', 'N/A')

def get_battery_info():
    battery = psutil.sensors_battery()
    return (battery.percent, battery.secsleft) if battery else ('N/A', 'N/A')

def get_disk_info():
    disks = {}
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks[part.device] = {
                'Total': f"{usage.total / (1024 ** 3):.2f} GB",
                'Used': f"{usage.used / (1024 ** 3):.2f} GB",
                'Free': f"{usage.free / (1024 ** 3):.2f} GB",
                'Percent': f"{usage.percent}%"
            }
        except PermissionError:
            continue
    return disks

def get_network_info():
    data = {}
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                data[iface] = addr.address
    return data

def display_header():
    console.print(Panel.fit(Text(ascii_art, style="bold magenta"), title="[bold cyan]SYSTEM INSPECTOR", subtitle="by snd", style="bold magenta"))
    console.print(Panel(Text(f"System Overview as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style="bold cyan"), style="bold blue"))

def display_table(title, data_dict, title_color):
    table = Table(title=title, style=title_color, box=box.DOUBLE_EDGE, title_style=f"bold {title_color}")
    for k, v in data_dict.items():
        table.add_row(str(k), str(v))
    console.print(Panel(table, style=f"bold {title_color}"))

def display_disk_info(disk_info):
    table = Table(title="Disk Usage", box=box.ROUNDED, style="bold cyan")
    table.add_column("Device")
    table.add_column("Total")
    table.add_column("Used")
    table.add_column("Free")
    table.add_column("Usage %")
    for dev, data in disk_info.items():
        table.add_row(dev, data['Total'], data['Used'], data['Free'], data['Percent'])
    console.print(Panel(table, style="bold cyan"))

def display_gpu_info(gpus):
    if isinstance(gpus, str):
        console.print(Panel(Text(gpus, style="bold red"), title="GPU Info", style="bold red"))
    else:
        table = Table(title="GPU Info", box=box.SQUARE, style="bold green")
        table.add_column("Name")
        table.add_column("Driver")
        table.add_column("Memory")
        table.add_column("Utilization")
        for gpu in gpus:
            table.add_row(gpu['name'], gpu['driver'], gpu['memory'], gpu['utilization'])
        console.print(Panel(table, style="bold green"))

def display_progress_bar():
    progress = Progress("[progress.description]{task.description}", "[progress.percentage]{task.percentage:>3}%", "{task.completed}/{task.total}")
    task = progress.add_task("Gathering info", total=6)
    with progress:
        for _ in range(6):
            time.sleep(0.4)
            progress.update(task, advance=1)

def main():
    display_progress_bar()
    display_header()
    display_table("System Information", get_system_info(), "white")
    display_gpu_info(get_gpu_info())
    display_table("CPU Info", {"Model": get_cpu_info()}, "magenta")
    percent, secs = get_battery_info()
    display_table("Battery Info", {"Percentage": f"{percent}%", "Time Left (s)": secs}, "red")
    display_disk_info(get_disk_info())
    display_table("Network Interfaces", get_network_info(), "yellow")

if __name__ == "__main__":
    main()