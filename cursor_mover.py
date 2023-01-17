#! python3

import time
import argparse
import re
import datetime
import pyautogui

def move_cursor_time(limit_time):
    """Executes until time defined by user"""
    print(f"This will stop at {limit_time.strftime('%H:%M')}")
    try:
        while True:
            for i in range(-1, 2, 2):
                now = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
                if limit_time == now:
                    print(f"Stopped! Now is: {now.strftime('%H:%M')}")
                    exit(0)
                pyautogui.move(i, i)
                print(f"Time: {now.strftime('%H:%M')} -- Position: {pyautogui.position()}")
                time.sleep(60)
    except KeyboardInterrupt:
        print("\nStopped manually!")

def move_cursor():
    """Executes until user press Ctrl + C"""
    print("Executing indefinitely, press Ctrl + C to stop execution")
    try:
        while True:
            now = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
            for i in range(-1, 2, 2):
                pyautogui.move(i, i)
                print(f"Time: {now.strftime('%H:%M')} -- Position: {pyautogui.position()}")
                time.sleep(60)
    except KeyboardInterrupt:
        print("\nStopped manually!")

PARSER = argparse.ArgumentParser(prog='cursor_mover.py', description='Moves the cursor 1 pixel every specific time', usage='%(prog)s [options]')
PARSER.add_argument("-t", metavar='HH:mm', dest='set_time', help="Set time in HH:mm to stop (24-hour format)")
ARGS = PARSER.parse_args()

if ARGS.set_time:
    try:
        PATTERN = re.compile('^[0-9]{1,2}:[0-9]{2}$')
        CHECK = PATTERN.match(ARGS.set_time)
        HOUR_MINUTE = ARGS.set_time.split(":")
        CUSTOM_TIME = datetime.time(int(HOUR_MINUTE[0]), int(HOUR_MINUTE[1]))
        if CHECK and CUSTOM_TIME:
            move_cursor_time(CUSTOM_TIME)
    except ValueError:
        print(f"You entered {ARGS.set_time}, please use a time value under 23:59")
    except IndexError:
        print(f"You entered {ARGS.set_time}, please use the correct format HH:mm in 24-hour, for example 13:30")
else:
    move_cursor()
