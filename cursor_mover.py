#! python3

import pyautogui
import time
import argparse
import re
import datetime

def move_cursor_time(custom_time):
    print(f"This will stop at {custom_time.strftime('%H:%M')}")
    while True:
        for i in range(-1, 2, 2):
            current_time = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
            if custom_time == current_time:
                print(f"Stopped! Now is: {current_time.strftime('%h:%M')}")
                exit(0)
            pyautogui.move(i, i)
            print(f"Time: {current_time.strftime('%h:%M')} -- Position: {pyautogui.position()}")
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
    try:
        pattern = re.compile('ˆ[0-9]{1,2}\:[0-9]{2}$')
        check = pattern.match(args.set_time)
        hour_minute = args.set_time.split(":")
        custom_time = datetime.time(int(hour_minute[0]), int(hour_minute[1]))
        current_time = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
        if check and custom_time:
            move_cursor_time(custom_time)
    except ValueError:
        print(f"You entered {args.set_time}, please use a time value under 23:59")
    except IndexError:
        print(f"You entered {args.set_time}, please use the correct format HH:mm in 24-hour, for example 13:30")
else:
    move_cursor()