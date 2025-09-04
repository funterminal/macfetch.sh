# MacFetch - Advanced System Information Tool

## Overview

MacFetch is a comprehensive system information tool written in Python that provides detailed hardware and software specifications in an aesthetically pleasing format. Inspired by traditional system fetch tools, MacFetch offers enhanced functionality with rich visual output and extensive system probing capabilities.

## Features

- **Detailed System Profiling**: Retrieves comprehensive hardware and software information
- **Visual Presentation**: Utilizes rich text formatting for terminal output
- **Multi-Component Analysis**: Covers CPU, GPU, memory, disks, battery, and network
- **Cross-Platform Compatibility**: Works across different operating systems
- **Real-Time Data**: Provides up-to-date system metrics at runtime

## Installation

### Quick Install (Recommended)
```bash
wget https://raw.githubusercontent.com/funterminal/macfetch.sh/refs/heads/main/macfetch.py
```

### Manual Installation
1. Ensure Python 3.6+ is installed
2. Install required dependencies:
```bash
pip install psutil cpuinfo gpuinfo rich
```
3. Download the script:
```bash
wget https://raw.githubusercontent.com/beautifulsh2/macfetch.sh/refs/heads/main/macfetch.py
```
4. Make executable:
```bash
chmod +x macfetch.py
```

## Usage

Run MacFetch with Python:
```bash
python macfetch.py
```

For direct execution (after making executable):
```bash
./macfetch.py
```

## Technical Specifications

### Data Collection Components

1. **System Information**
   - Operating system details
   - Architecture and machine type
   - Hostname and network identifiers
   - Memory and swap specifications

2. **Processor Analysis**
   - CPU brand and model
   - Physical and logical core count
   - Architecture details

3. **Graphics Processing**
   - GPU model and specifications
   - Driver information
   - Memory utilization

4. **Storage Metrics**
   - Partition details
   - Usage statistics (total/used/free)
   - Mount points and devices

5. **Power Management**
   - Battery percentage
   - Estimated remaining time

6. **Network Interfaces**
   - Active network adapters
   - IP address assignments

### Dependencies

- `platform`: Built-in Python module for system information
- `psutil`: Process and system utilities
- `cpuinfo`: CPU identification
- `gpuinfo`: GPU information
- `rich`: Terminal formatting and styling
- `socket`: Network interface handling
- `uuid`: System identification

## Output Sections

1. **System Header**: ASCII art and timestamp
2. **Core System Information**: OS, architecture, memory
3. **GPU Details**: Model, driver, utilization
4. **CPU Specifications**: Processor model
5. **Battery Status**: Percentage and remaining time
6. **Disk Utilization**: Partition details and usage
7. **Network Configuration**: Interface addresses

## Performance Considerations

MacFetch implements intelligent data collection:
- Progressive loading with visual feedback
- Error handling for unavailable metrics
- Permission-aware disk scanning
- Graceful fallbacks for missing components

## Customization

Advanced users can modify:
- ASCII art in the `ascii_art` variable
- Color schemes in the display functions
- Information density by commenting sections
- Progress bar timing in `display_progress_bar()`

## Compatibility

Tested on:
- Linux distributions (Ubuntu, Arch, Fedora)
- macOS (Intel and Apple Silicon)
- Windows (with limited functionality)

## Contributing

Contributions are welcome through:
- Issue reporting
- Feature requests
- Pull requests
- Documentation improvements

## Support

For support or feature requests, please open an issue on the GitHub repository.

## Acknowledgments

- Python community for foundational modules
- Rich library developers for terminal enhancements
- Open source hardware detection projects