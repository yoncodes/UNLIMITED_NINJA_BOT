from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class elite_match:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions


	def __call__(self):
		return self

	def toast(self):
		if eval(str(self.positions.parse(_SETTINGS, 'elite_match', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			print "[+] Elite Match : Open"
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'open'))
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_plum'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_close'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'join'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'close'))
			sleep(1)
			self.positions.write(_SETTINGS,'elite_match','done', 1)
		else:
			#self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'close'))
			pass