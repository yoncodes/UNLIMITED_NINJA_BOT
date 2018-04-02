from UN_BOT import app

import os.path,os

import time
from PIL import ImageGrab, ImageChops, Image
from time import gmtime, strftime

MASTER_FILE = _SETTINGS = os.path.join(os.path.dirname(os.getcwd())) + '\\UNLIMITED_NINJA_BOT\\master.ini'

UN_START = app.app()

USERNAME = UN_START.position().read(MASTER_FILE, 'account','username')
PASSWORD = UN_START.position().read(MASTER_FILE, 'account','password')
SERVER = UN_START.position().read(MASTER_FILE, 'account','server')
PLATFORM = UN_START.position().read(MASTER_FILE, 'account','platform')

if UN_START.update() != True:

	#UN_START.cord() # testing

	#UN_START.system_checks().master_reset() #resets everything back to zero, great for at reset
	#UN_START.start(USERNAME, PASSWORD, SERVER, PLATFORM)
	UN_START.show_window(PLATFORM)
	
	#UN_START.claim().check_in()
	
	#UN_START.claim().kaguya_power()
	
	#UN_START.claim().vip()
	#UN_START.claim().profile()
	#UN_START.samsara_land(land='nightmare')
	#UN_START.top_kages(ri=True,practice='all')
	#UN_START.treasure_map().hunt()
	#UN_START.arena().fights(2) 
	#UN_START.arena().claim()
	#UN_START.forbidden_jutsu().claim()
	#UN_START.six_path_arcanum().claim()
	#UN_START.mount_myobuku()
	#UN_START.occult_techniques()
	#UN_START.sage_heirloom().claim()
	#UN_START.dungeon().auto()
	#UN_START.dungeon().claim()
	#UN_START.dungeon().occupy(50)
	#UN_START.daily_benefit().claim(extra=False)
	#UN_START.loto().claim(ri=True)
	#UN_START.wings()
	#UN_START.mail().check(pages = 1)
	#UN_START.elite_match().toast()
	#UN_START.guild().inject()
	#UN_START.guild().donate(1000)
	#UN_START.lost_tower().tower(lvl=105,manual=False)
	#UN_START.claim().online()
	#print UN_START.system_checks().dungeon_end()