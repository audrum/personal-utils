# Cursor Move

This small script moves the cursor 1 pixel every 60 seconds just to keep your operating system awake and "online" status in your corporate messaging app.

## How to use

1. Install [Python](https://www.python.org/downloads/) (In case you do not have it already).

2. Install [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) using the command:

```Python
pip3 install pyautogui
```
3. Execute the script with the command:

```
python3 cursor_mover.py
```

If you want to set a time to stop, use the argument _-t_ followed by time in 24-hour format, example:

```
python3 cursor_mover.py -t 13:00
```

For manual stopping just press Ctrl + C

Any suggestions just reach out to me on [@audrum](https://t.me/audrum)
