"""
Description:
    This script retrieves the saved Wi-Fi password for a specified Wi-Fi network on a Windows machine
    using the `netsh` command.

Requirements:
    - Python 3.x
    - Windows OS (this script relies on the `netsh` command which is Windows-specific)
    - The specified Wi-Fi profile must exist on the system

Important:
    - You must run the script in a terminal or environment with permissions to access network profiles.
    - Replace 'your_wifi_name' with the actual Wi-Fi SSID saved on your system.

Usage:
    1. Open a terminal or command prompt.
    2. Edit the script to replace wifi_name = 'your_wifi_name' with the actual SSID.
    3. Run the script
    4. If the profile exists and contains a saved password, it will be printed to the console.

Security Note:
    - This script accesses sensitive system data. Use responsibly and avoid sharing outputs.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

import subprocess

wifi_name = 'your_wifi_name'

output = subprocess.check_output(
    f'netsh wlan show profile {wifi_name} key=clear', shell=True, encoding='utf-8')
print(output)
lines = output.splitlines()
for line in lines:
    if 'Key Content' in line:
        password_line = line
        break

if password_line:
    pwd = password_line.split(":")[1].strip()
    print('Password is :', pwd)
else:
    print('Password not found')
