from time import sleep

import datetime

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'


class claim:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions


	def __call__(self):
		return self

	def online(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online_default'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online_close'))
		sleep(.5)

	def check_in(self):
		print "[+] Online : Checking in"
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_default'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in'))
		sleep(3)
		print "[+] Online : Claiming Rewards"
		self.mouse.move(self.positions.parse(_POSITIONS,'claim', 'check_in_rewards'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_cumulative'))
		sleep(2)
		self.day()
		sleep(1)
		print "[+] Online : Checking in Closing"
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_close'))
		sleep(.1)

	def day(self):
		today = datetime.date.today()
		go = False
		if today.day != 29:
			if today.day != 30:
				if today.day != 31:
					go = True
		if go == True:
			num = self.positions.parse(_POSITIONS, 'online', 'day' + str(today.day))
			print "[+] Online : Claim Day {}".format(today.day)
			self.mouse.move(num)

	def kaguya_power(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'open'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'claim'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'close'))
		sleep(.1)

	def vip(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'open'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'claim'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'close'))
		sleep(.1)

	def profile(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'open'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'claim'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'close'))
		sleep(.1)