import random as r
import pyautogui as pyauto

döndür = r.randint(0000,9999)
pyauto.typewrite(str(döndür),interval=0.25)