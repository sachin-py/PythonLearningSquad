"""
Description:
    Simulates mouse movements and Shift key presses to prevent the system from going idle.
    Useful when you want to appear active or keep your session alive (e.g., during long meetings).

Requirements:
    - Python 3.x
    - PyAutoGUI library

Install dependencies:
    pip install pyautogui

Usage:
    Run the script in a terminal

⚠️ Disclaimer:
    This script simulates real user input. Use responsibly and avoid violating workplace or service policies.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

import pyautogui
import time


def stay_awake(repeats=5, delay_between_actions=5):
    """
    Keeps the system active by moving the mouse and pressing Shift key.

    Args:
        repeats (int): Number of times to perform the action loop.
        delay_between_actions (int): Seconds to wait between iterations.
    """
    print("Stay-awake script starting in 2 seconds...")
    time.sleep(2)

    for i in range(repeats):
        print(f"Iteration {i+1}/{repeats} - Simulating activity...")

        # Simulate mouse movement
        pyautogui.moveTo(700, 200, duration=0.5)
        pyautogui.moveTo(700, 450, duration=0.5)
        pyautogui.moveTo(700, 200, duration=0.5)

        # Simulate Shift key press
        pyautogui.keyDown('shift')
        time.sleep(0.5)
        pyautogui.keyUp('shift')

        time.sleep(delay_between_actions)

    print("All done. You should have stayed 'awake' for a while!")


if __name__ == "__main__":
    stay_awake()
