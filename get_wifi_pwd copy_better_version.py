"""
Description:
    Retrieves the saved Wi-Fi password for a specified Wi-Fi network profile on a Windows system
    using the `netsh` command.

Requirements:
    - Python 3.x
    - Windows OS (uses `netsh`)
    - Wi-Fi profile must be saved on the machine

Installation:
    No external libraries needed. Just run on Windows with Python 3.

Usage:
    1. Run the script:
        python wifi_password_extractor.py
    2. Enter the name (SSID) of the Wi-Fi network when prompted.
    3. The script will display the saved password if found.

Notes:
    - Run in an environment with permission to access network profiles.
    - Do not share output containing sensitive information.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

import subprocess


def get_wifi_password(profile_name: str) -> str:
    """Fetch the saved Wi-Fi password for a given profile name using netsh.

    Args:
        profile_name (str): The name of the saved Wi-Fi network.

    Returns:
        str: The extracted password, or an error message.
    """
    try:
        command = f'netsh wlan show profile "{profile_name}" key=clear'
        output = subprocess.check_output(command, shell=True, encoding='utf-8')

        for line in output.splitlines():
            if "Key Content" in line:
                return line.split(":", 1)[1].strip()

        return "Password not found or not saved for this profile."

    except subprocess.CalledProcessError:
        return "Failed to retrieve profile. Make sure the profile exists."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    profile = input("Enter the Wi-Fi profile name: ").strip()
    password = get_wifi_password(profile)
    print(f"\nPassword: {password}")
