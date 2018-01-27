import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class dungeon:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions



	def __call__(self):
		return self

	def auto(self):
		if eval(str(self.positions.parse(_SETTINGS, 'dungeon', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'open'))
			time.sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'auto'))
			time.sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
			self.positions.write(_SETTINGS,'dungeon','done', 1)
		else:
			print "[+] Dungeon : Complete"
			#self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
