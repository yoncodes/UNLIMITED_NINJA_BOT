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

	def conquest(self):
		self.move(self.positions.parse(_POSITIONS, 'activity', 'open'))
		sleep(3)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest'))
		sleep(62)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest_auto'))
		sleep(1800)
		self.move(self.positions.parse(_POSITIONS, 'activity', 'konoha_conquest_confirm'))

	def defense(self):
		pass 

	def rebels(self):
		pass

