import win32api
import win32con
import time

while True:
    win32api.keybd_event(87,0,0,0)
    time.sleep(10)
