#! python3

import pyautogui
import time
import argparse

def move_cursor_time(set_time):
    while True:
        now = time.strftime('%H:%M:%S', time.localtime())
        if now >= set_time:
            print(f"Stopped! Now is: {now}")
            break
        for i in range(-1, 2, 2):
            pyautogui.move(i, i)
            print(f"Time: {now} -- Position: {pyautogui.position()}")
            time.sleep(60)

def move_cursor():
    while True:
        for i in range(-1, 2, 2):
            pyautogui.move(i, i)
            print(f"Time: {time.strftime('%H:%M:%S', time.localtime())} -- Position: {pyautogui.position()}")
            time.sleep(60)

parser = argparse.ArgumentParser(prog = 'cursor_mover.py', description = 'Moves the cursor 1 pixel every specific time', usage = '%(prog)s [options]')
parser.add_argument("-t", metavar = 'HH:mm', dest = 'set_time', help = "Set time in HH:mm to stop (24-hour format)")
args = parser.parse_args()

if args.set_time:
    move_cursor_time(args.set_time)
else:
    move_cursor()