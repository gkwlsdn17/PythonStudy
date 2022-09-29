import pyautogui
import time

def read_coordinate():
    print(pyautogui.position())
    time.sleep(0.1)

while True:
    read_coordinate()
