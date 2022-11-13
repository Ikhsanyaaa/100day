import pyautogui
import time

pesan = "spam"
n = 20

time.sleep(2)

for i in range(n) :
    pyautogui.typewrite(pesan + "\n")