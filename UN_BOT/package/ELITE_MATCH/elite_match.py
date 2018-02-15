from time import sleep
from datetime import datetime, timedelta

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class elite_match:

	def __init__(self, mouse, positions, _time):
		self.mouse = mouse
		self.positions = positions
		self.time = _time


	def __call__(self):
		return self

	def toast(self):
		now_time = datetime.now()

		if eval(str(self.positions.parse(_SETTINGS, 'elite_match', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			print "[+] Elite Match : Open"
			sleep(5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'open'))
			sleep(2)

			if self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'elite_match','pre_start')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), datetime.strptime(self.positions.parse(_SETTINGS,'elite_match','pre_end')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p')):

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
			else:
				self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_after_enter'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_plum'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_close'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'join_after'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'close_after'))
				sleep(1)

		self.positions.write(_SETTINGS,'elite_match','done', 1)
		