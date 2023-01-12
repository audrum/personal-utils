#! python3

import pyautogui
import time

while True:
    for i in range(-1, 2, 2):
        pyautogui.move(i, i)
        print(pyautogui.position())
        time.sleep(60)