import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\settings.ini'

class dungeon:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))


	def __call__(self):
		return self

	def auto(self):
		time.sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'open'))
		time.sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'auto'))
		time.sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
