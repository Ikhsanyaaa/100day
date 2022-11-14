import pyautogui
import time

pesan = "login"
n = 20

time.sleep(2)

for i in range(n) :
    pyautogui.typewrite(pesan + "\n")