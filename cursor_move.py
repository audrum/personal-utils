#! python3

import pyautogui
import time

while True:
    now = time.strftime("%H:%M", time.localtime())
    if now == "00:01":
        break
    for i in range(-1, 2, 2):
        pyautogui.move(i, i)
        print(f"Time: {now} -- Position: {pyautogui.position()}")
        time.sleep(30)
print(f"Stopped because now is: {now}")
    