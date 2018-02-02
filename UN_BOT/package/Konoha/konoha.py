from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'



class konoha:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

	def __call__(self):
		return self

	def conquest_register(self):
		self.move(self.positions.parse(_POSITIONS, 'activity', 'open'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'enter'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'close'))

	def conquest(self):
		self.move(self.positions.parse(_POSITIONS, 'activity', 'open'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'enter'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest_auto'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest_confirm'))

	def defense(self):
		self.move(self.positions.parse(_POSITIONS, 'activity', 'open'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_defense'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'enter'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_defense_auto'))

	def rebels(self):
		self.move(self.positions.parse(_POSITIONS, 'activity', 'open'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'rebels_attack'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'enter'))
		sleep(5)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'rebels_attack_auto_skip'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'rebels_attack_auto'))

