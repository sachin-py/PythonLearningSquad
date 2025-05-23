"""
Description:
    Automates mouse movements and Shift key presses using PyAutoGUI.

Requirements:
    - Python 3.x
    - PyAutoGUI library

Install dependencies:
    pip install pyautogui

Usage:
    1. Ensure you have a working display and the script has permission to control the mouse and keyboard.
    2. Run the script
    3. After a 2-second delay, the mouse will move between two coordinates and press/release Shift,
       repeating 5 times.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

import pyautogui
import time

time.sleep(2)

counter = 0
while counter < 5:
    pyautogui.moveTo(700, 200, duration=1)
    pyautogui.moveTo(700, 450, duration=1)
    pyautogui.moveTo(700, 200, duration=1)

    pyautogui.keyDown('shift')
    time.sleep(1)
    pyautogui.keyUp('shift')
    time.sleep(5)
    counter += 1
