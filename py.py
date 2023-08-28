import random
import pyautogui as pg
import time

# 1. Open a new tab in your browser
time.sleep(8)
x,y= pg.position()
print("x", x, "y", y)

    # pg.leftClick(100, 100)
pg.write('https://pyautogui.readthedocs.io/en/latest/install.html')
pg.moveTo(1332, 500)
pg.press("enter")
pg.write('https://pyautogui.readthedocs.io/en/latest/install.html')
pg.press('enter')
    