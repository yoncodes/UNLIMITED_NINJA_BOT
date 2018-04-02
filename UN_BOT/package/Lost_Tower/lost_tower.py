from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class lost_tower:

	def __init__(self, mouse, positions):

		self.mouse = mouse
		self.positions = positions

	def __call__(self):
		return self

	def tower(self, lvl, manual = False):
		if eval(str(self.positions.parse(_SETTINGS, 'lost_tower', 'done')[0])) != True:
			if lvl == 105 and manual == False :
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
				sleep(5)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'open'))
				sleep(2)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_105'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_105_auto'))
				sleep(32)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'confirm'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_close'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'close'))
				sleep(1)
				self.positions.write(_SETTINGS,'lost_tower','done', 1)
		else:
			print "[+] Lost tower : complete"