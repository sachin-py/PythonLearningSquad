"""
Drinking Water Reminder Script
------------------------------

This Python script sends desktop notifications reminding the user to drink water.
It uses the 'plyer' library for cross-platform notifications.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py/
"""

# Import required modules
from plyer import notification
import time

# Number of reminders to send
for i in range(2):
    notification.notify(
        title='Drinking Water Reminder',
        message='Take 2 Glasses of Water',
        app_icon='water.ico'  # Ensure the .ico file is in the same directory
    )
    time.sleep(2)  # Pause for 2 seconds between notifications
