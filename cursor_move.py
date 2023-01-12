#! python3

import pyautogui
import time

now = "00:00"

while now < "23:54":
    now = time.strftime("%H:%M", time.localtime())
    for i in range(-1, 2, 2):
        pyautogui.move(i, i)
        print(f"Time: {now} -- Position: {pyautogui.position()}")
        time.sleep(30)
    