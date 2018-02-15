from time import sleep
from datetime import datetime, timedelta

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'


class guild:

	def __init__(self, mouse, keyboard, positions, time1):
		self.mouse = mouse
		self.keyboard = keyboard
		self.positions = positions
		self.time = time1

	def __call__(self):
		return self

	def donate(self, amount):
		
		if bool(eval(self.positions.parse(_SETTINGS, 'guild', 'donate_done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'open'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'donate'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'donate_amount'))
			sleep(1)
			self.keyboard.type(amount)
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'donate_confirm'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'donate_close'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'close'))


	def inject(self):

		current = self.positions.parse(_SETTINGS, 'guild', 'injects')[0]
		next_inject_time = self.positions.parse(_SETTINGS, 'guild', 'next_inject')[1]
		now_time = datetime.now()
		two_hour_min = datetime.now() + timedelta(minutes=121)

		
		
		if  self.positions.parse(_SETTINGS, 'guild', 'max_inject')[0] > current:
			if self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'guild','last_inject')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), next_inject_time) != True:
				self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'open'))
				sleep(3)
				self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'treasure_tree'))
				sleep(1)
				self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'inject'))
				sleep(2)
				self.mouse.move(self.positions.parse(_POSITIONS, 'guild', 'close'))
				sleep(.1)

				current = int(current)
				current += 1
				self.positions.write(_SETTINGS,'guild','injects',int(current))
				self.positions.write(_SETTINGS,'guild','last_inject', '{:%H:%M:%S%p}'.format(now_time))
				self.positions.write(_SETTINGS,'guild','next_inject', '{:%H:%M:%S%p}'.format(two_hour_min))