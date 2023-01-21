import pyautogui

print(pyautogui.size())
pyautogui.PAUSE=2
pyautogui.moveTo(850,1052,duration=1)
pyautogui.click()
pyautogui.moveTo(344,y=166,duration=1)
pyautogui.click()
pyautogui.write("putu")
pyautogui.moveTo(232,406,duration=1)
pyautogui.click()
pyautogui.moveTo(939,961,duration=1)
pyautogui.click()
pyautogui.write("hai bang")
pyautogui.moveTo(1870,971,duration=1)
pyautogui.click()

print(pyautogui.position())