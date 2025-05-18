"""
Drinking Water Reminder
-----------------------

This script sends periodic desktop notifications reminding the user
to drink water. It's built using the 'plyer' library, which supports
cross-platform desktop notifications.

Requirements:
- Python 3.x
- plyer library (`pip install plyer`)
- water.ico (icon file in the same directory as the script)

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

import time
import os
from plyer import notification

# Constants
REMINDER_COUNT = 2           # Number of reminders to send
INTERVAL_SECONDS = 2         # Delay between reminders in seconds
ICON_FILENAME = "water.ico"  # Icon file for the notification

# Get absolute path to the icon (ensures correct loading)
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, ICON_FILENAME)


def send_water_reminder():
    """
    Sends a desktop notification to remind the user to drink water.
    """
    notification.notify(
        title='Drinking Water Reminder',
        message='Time to take 2 glasses of water!',
        app_icon=icon_path,
        timeout=10  # Notification stays for 10 seconds
    )


def main():
    """
    Main function to trigger water reminders.
    """
    for i in range(REMINDER_COUNT):
        send_water_reminder()
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
