import datetime, time
import os

class countdown:

	def __init__(self):
		pass

	def timer(self,t):
	    while t:
	    	now = datetime.datetime.now()
	    	os.system('cls')
	        mins, secs = divmod(int(t), 60)
	        timeformat = '{:02d}:{:02d}'.format(mins, secs)
	        print now.strftime("[+] System date: %m-%d-%Y Current time: %H:%M:%S")
	        print timeformat,'\r'
	        if t < 1:
	        	time.sleep(t)
	        	t -= t
	        else:
	        	time.sleep(1)
	        	t -= 1