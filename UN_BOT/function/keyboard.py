import win32com.client as comclt
import time
import pyautogui

class keyboard:

	def __init__(self):
		pass

	def type(self,keys):
		wsh= comclt.Dispatch("WScript.Shell")
		time.sleep(.1)
		wsh.SendKeys(keys)

	def space(self):
		pyautogui.press('space')