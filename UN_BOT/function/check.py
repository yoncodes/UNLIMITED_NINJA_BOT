import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\settings.ini'

class check:

	def __init__(self, positions, _time):
		self.positions = positions
		self.time = _time

	def __call__(self):
		return self


	def reset(self):
		# arena reset
		if(self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'arena','fights_reset_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), datetime.strptime(self.positions.parse(_SETTINGS,'arena','fight_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'))):
	 		self.positions.write(_SETTINGS,'arena','fights_today', 0)
	 		self.positions.write(_SETTINGS,'arena','claimed', 0)