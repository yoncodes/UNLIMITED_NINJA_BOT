from datetime import datetime, time

class _time:

	def __init__(self):
		pass

	def isNowInTimePeriod(self,startTime, endTime):
		now = datetime.now()
		timeNow = now.time().strftime("%H:%M:%S%p")
		endTime = datetime.strptime(endTime, "%H:%M:%S%p")
		startTime = datetime.strptime(startTime, "%H:%M:%S%p")
		timeNow = datetime.strptime(timeNow, "%H:%M:%S%p")

		nowTime = timeNow

		if startTime < endTime:
			return nowTime >= startTime and nowTime <= endTime
		else: #Over midnight
			return nowTime >= startTime or nowTime <= endTime

	def until(self, startTime, endTime):
		first = datetime.strptime(str(startTime), "%H:%M:%S%p")
		second = datetime.strptime(str(endTime), "%H:%M:%S%p")
		delta = second - first

		return delta