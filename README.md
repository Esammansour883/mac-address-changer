# MAC Address Changer

A Python script to change the MAC address of a specified network interface. This tool can be used for various purposes such as network testing, privacy enhancement, or device impersonation.

## Features

- **Change MAC address**: Easily change the MAC address of your network interface.
- **Bypass network filters**: Modify your MAC address to bypass MAC-based filters or restrictions in networks.
- **Device impersonation**: Spoof another device by setting its MAC address.
- **Privacy enhancement**: Change your MAC address to protect your privacy and avoid tracking based on your network interface.
- **Cross-platform**: The script works on Linux and macOS, but Windows requires modification.

## Prerequisites

Before using the script, make sure you have the following:

- **Python**: Ensure you have Python 2.7 or 3.x installed.
- **Administrator/Sudo Privileges**: Changing MAC addresses requires elevated privileges.
- **Linux or macOS**: The script uses `ifconfig`, which is available on Unix-like systems. On Windows, the script would need modifications to use `netsh` or similar tools.

## Installation

### Clone the repository

First, clone the repository to your local machine:

 ```bash
 git clone https://github.com/Esammansour883/mac-address-changer.git
 cd mac-address-changer
 ```

### Install Dependencies

This script uses Python’s subprocess, argparse, and re libraries, which are available by default in Python.

No external dependencies need to be installed, but ensure you have Python installed on your system.

## Usage

To change the MAC address of a network interface, run the script with the following command:

 ```bash
 python chang_mac_address.py -i <interface> -m <new_mac>
 ```

Where:
- **<interface>**: The network interface (e.g., eth0, wlan0, etc.).
- **<new_mac>**: The new MAC address in the format XX:XX:XX:XX:XX:XX.

### Example:

 ```bash
 python chang_mac_address.py -i eth0 -m 00:55:77:44:77:88
 ```

### Script Output

- **Success**: If the MAC address is successfully changed, you will see a message like:

```bash
 [+] Changing MAC address for eth0...
 [+] The MAC address has been successfully changed to 00:55:77:44:77:88
 ```

- **Failure**: If an error occurs, an appropriate error message will be displayed:

 ```bash
 [-] Failed to change MAC address. Check your permissions or inputs.
 ```

## How It Works

- The script first checks whether the provided MAC address has a valid format using regular expressions.
- It then verifies that the specified network interface exists on the system.
- The script uses the ifconfig tool to disable the interface, change the MAC address, and then bring the interface back up.
- After the operation, it checks if the MAC address was successfully updated by inspecting the output of ifconfig.

## Enhancements and Use Cases

- **Privacy**: Frequently changing your MAC address can enhance privacy, especially in public Wi-Fi networks.
- **Network Testing**: Useful for network administrators or testers to simulate different devices or bypass network restrictions.
- **Device Impersonation**: You can impersonate another device by setting its MAC address, useful for testing network behavior.

## Limitations

- **Windows Compatibility**: This script uses ifconfig, which is not available on Windows. To make it work on Windows, you would need to modify the script to use Windows-specific commands like netsh.
- **Network Adapter Support**: Not all network adapters support changing the MAC address, especially on virtual machines or certain hardware.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Author

Created by Essam Mansour.
