import win32api, win32con
import time

from win32api import GetSystemMetrics

# Globals
# ------------------

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

window_width = 1298
window_height = 850

x_pad = (screen_width / 2) - (window_width / 2)  + 18
y_pad = (screen_height / 2) - (window_height / 2) + 120

class mouse:
	def leftClick(self):
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	    time.sleep(.1)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	    #print "Click."          #completely optional. But nice for debugging purposes.

	def leftDown(self):
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	    time.sleep(.1)
	    #print 'left Down'
	         
	def leftUp(self):
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	    time.sleep(.1)
	    #print 'left release'

	def scrollDown(self, num):
		win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 615, 269, num, 0)
		time.sleep(.1)

	def drag_n_drop(self,current_pos, new_pos):
		self.mousePos((current_pos))
		self.leftDown()
		self.mousePos((new_pos))
		self.leftUp()

	def mousePos(self,cord):
	    win32api.SetCursorPos((x_pad + int(cord[0]), y_pad + int(cord[1])))
	     
	def get_cords(self):
	    x,y = win32api.GetCursorPos()
	    x = x - x_pad
	    y = y - y_pad
	    print x,y

	def move(self,pos):
		self.mousePos(pos)
		self.leftClick()
		time.sleep(.1)
