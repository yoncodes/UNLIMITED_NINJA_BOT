import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class dungeon:

	def __init__(self, mouse, positions, check):
		self.mouse = mouse
		self.positions = positions
		self.check = check



	def __call__(self):
		return self

	def auto(self):
		if eval(str(self.positions.parse(_SETTINGS, 'dungeon', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'open'))
			time.sleep(10)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'auto'))
			time.sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
			self.positions.write(_SETTINGS,'dungeon','done', 1)
		else:
			print "[+] Dungeon : Complete"
			#self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))

	def claim(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		time.sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'open'))
		time.sleep(10)
		if self.check().dungeon_end():
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'practice_list'))
			time.sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'rewards'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'claim_rewards'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'rewards_2'))
			time.sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'practice_close'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
		else:
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))

	def occupy(self,floor):
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		time.sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'open'))
		time.sleep(10)
		if self.check().dungeon_end():
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'practice_list'))
			time.sleep(1)
			if floor == 50:
				time.sleep(5)
				self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'floor_50'))
				time.sleep(32)
				self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'skip'))
				time.sleep(3)
				self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'ok'))
				time.sleep(3)
				self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'practice_close'))
				time.sleep(3)
				self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
		else:
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'practice_close'))
			time.sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'dungeon', 'close'))
