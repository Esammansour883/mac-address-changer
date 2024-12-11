#!/usr/bin/python
import subprocess
import argparse
import re
import sys

# Function to validate the MAC address format
def is_valid_mac(mac_address):
    return bool(re.match(r'^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$', mac_address))

# Function to check if the network interface exists
def interface_exists(interface):
    try:
        subprocess.check_output(['ifconfig', interface])
        return True
    except subprocess.CalledProcessError:
        return False

# Create a parser for the inputs
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', dest='network_interface', help='Specify the network interface')
parser.add_argument('-m', '--mac', dest='new_mac', help='Specify the new MAC address')

args = parser.parse_args()

# Check if both the interface and MAC address are provided
if not args.network_interface or not args.new_mac:
    print("[-] Please provide both the network interface and new MAC address.")
    sys.exit()

# Check if the MAC address format is valid
if not is_valid_mac(args.new_mac):
    print("[-] Invalid MAC address format. Ensure the format is XX:XX:XX:XX:XX:XX.")
    sys.exit()

# Check if the network interface exists
if not interface_exists(args.network_interface):
    print(f"[-] Network interface {args.network_interface} not found. Please verify the interface name.")
    sys.exit()

# Attempt to change the MAC address
try:
    print(f"[+] Changing MAC address for {args.network_interface}...")
    subprocess.check_call(['ifconfig', args.network_interface, 'down'])
    subprocess.check_call(['ifconfig', args.network_interface, 'hw', 'ether', args.new_mac])
    subprocess.check_call(['ifconfig', args.network_interface, 'up'])
except subprocess.CalledProcessError:
    print("[-] Failed to change MAC address. Check your permissions or inputs.")
    sys.exit()

# Read the result of the ifconfig command
ifconfig_result = subprocess.check_output(['ifconfig', args.network_interface]).decode('utf-8')

# Search for the MAC address in the result
mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

# Verify the success of the operation
if mac and mac.group(0) == args.new_mac:
    print(f"[+] MAC address for {args.network_interface} successfully changed to {args.new_mac}")
else:
    print("[-] The operation failed. Please verify your MAC address and network interface.")
    sys.exit()
