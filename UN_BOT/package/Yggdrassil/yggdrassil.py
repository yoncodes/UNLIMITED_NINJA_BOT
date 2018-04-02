from time import sleep
from datetime import datetime, timedelta

import os.path


MASTER_FILE = os.path.join(os.path.dirname(os.getcwd())) + '\\UNLIMITED_NINJA_BOT\\master.ini'
_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class yggdrassil:

    def __init__(self, mouse, posistion):
        self.mouse = mouse
        self.posistion = posistion

    def __call__(self):
        return self

    def start(self, time):
        if time == self.posistion.parse(MASTER_FILE, 'yggdrassil', 'start'):
            sleep(3) 
            self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
            sleep(3)
            self.mouse.move(self.positions.parse(_POSITIONS, 'yggdrassil', 'open'))
            sleep(3)
            self.mouse.move(self.positions.parse(_POSITIONS, 'yggdrassil', 'start'))


    def claim(self, time):
        if time == self.posistion.parse(MASTER_FILE, 'yggdrassil', 'end'):
            sleep(3)
            self.posistion.parse(MASTER_FILE, 'yggdrassil', 'stop')
            sleep(1)
            self.posistion.parse(MASTER_FILE, 'yggdrassil', 'rewards')
            sleep(1)
            self.posistion.parse(MASTER_FILE, 'yggdrassil', 'claim')
            sleep(2)
            self.posistion.parse(MASTER_FILE, 'yggdrassil', 'close')