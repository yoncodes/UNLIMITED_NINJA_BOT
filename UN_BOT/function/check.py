import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

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


	def master_reset(self):
		self.positions.write(_SETTINGS,'claim','check_in', 0)
		self.positions.write(_SETTINGS,'claim','kaguya_power', 0)
		self.positions.write(_SETTINGS,'claim','profile', 0)
		self.positions.write(_SETTINGS,'claim','vip', 0)
		self.positions.write(_SETTINGS,'daily_benefit','done', 0)
		self.positions.write(_SETTINGS,'dungeon','done', 0)
		self.positions.write(_SETTINGS,'elite_match','done', 0)
		self.positions.write(_SETTINGS,'forbidden_jutsu','done', 0)
		self.positions.write(_SETTINGS,'loto','done', 0)
		self.positions.write(_SETTINGS,'mount_myobuku','done', 0)
		self.positions.write(_SETTINGS,'occult_techniques','done', 0)
		self.positions.write(_SETTINGS,'samsara_land','done', 0)
		self.positions.write(_SETTINGS,'six_path_arcanum','done', 0)
		self.positions.write(_SETTINGS,'sage_heirloom','done', 0)
		self.positions.write(_SETTINGS,'top_kages','done', 0)
		self.positions.write(_SETTINGS,'wings','done', 0)