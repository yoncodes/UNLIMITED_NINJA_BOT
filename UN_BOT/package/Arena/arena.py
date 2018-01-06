from time import sleep
from random import randint
from datetime import datetime, timedelta


import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class arena:
	 
	def __init__(self, mouse, positions, _time):
	 	self.mouse = mouse
	 	self.positions = positions
	 	self.time = _time
	 	
	 	if(self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'arena','fights_reset_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), datetime.strptime(self.positions.parse(_SETTINGS,'arena','fight_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'))):
	 		self.positions.write(_SETTINGS,'arena','fights_today', 0)

	def __call__(self):
		return self

	def fights(self, fights):
		self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'open'))
		sleep(3)
		self.fights = int(self.positions.parse(_SETTINGS, 'arena','fights_per_day')[0]) - int(self.positions.parse(_SETTINGS, 'arena','fights_today')[0])

		while self.fights <= fights and fights >= self.fights:
			num = self.positions.parse(_POSITIONS, 'arena', str((randint(2,10))) + '_place')
			print "[+] Waiting "
			sleep(2)
			self.mouse.move(num)
			print "[+] Fighting "
			sleep(1)
			print "[+] Waiting 20 seconds"
			sleep(19)
			self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'skip'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'ok'))

			self.fights += 1
			self.positions.write(_SETTINGS,'arena','fights_today', int(self.fights))
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'close'))

	def claim(self):
		if int(self.positions.parse(_SETTINGS, 'arena','claimed')[0]) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'open'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'claim'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'arena', 'close'))
		else:
			print '[+] Already claimed'

