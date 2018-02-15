import pyautogui
import time


# Globals
# ------------------

screen_width = pyautogui.size()[0]
screen_height = pyautogui.size()[1]

window_width = 1298
window_height = 850

x_pad = (screen_width / 2) - (window_width / 2)  + 18
y_pad = (screen_height / 2) - (window_height / 2) + 140 -50

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


class mouseMac:

	def leftClick(self):
		pyautogui.click(button='left')

	def leftDown(self):
		pyautogui.mouseDown(button='left')

	def leftUp(self):
		pyautogui.mouseUp(button='left')

	def scrollDown(self, amount):
		pyautogui.scroll(amount) # -10 10

	def drag_n_drop(self, current_pos, new_pos):
		self.mousePos((current_pos))
		self.leftDown()
		self.mousePos((new_pos))
		self.leftUp()

	def mousePos(self, cord):
		pyautogui.moveTo(x_pad + int(cord[0]), y_pad + int(cord[1]))
		print("x = " + str((x_pad + int(cord[0]))))
		print("y = " + str((y_pad + int(cord[1]))))
		print("\n")

	def get_cords(self):
		x, y = pyautogui.position()
		x = x - x_pad
		y = y - y_pad
		print x,y

	def move(self,pos):
		self.mousePos(pos)
		self.leftClick()
