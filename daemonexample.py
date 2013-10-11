#!/usr/bin/python
from daemon import Daemon
import sys
import time
import logging

PIDFILE = '/var/run/yourdaemon.pid'
LOGFILE = '/var/log/yourdaemon.log'

# Configure logging
logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)

class YourDaemon(Daemon):

	def run(self):
		# Define your tasks here
		# Anything written in python is permitted
		# For example you can clean up your server logs every hour
		
		
		# Logging errors and exceptions
		try:
			pass
		except Exception, e:
			logging.exception('Human friendly error message, the exception will be captured and added to the log file automaticaly')

		while True:
			# The daemon will repeat your tasks according to this variable
			# it's in second so 60 is 1 minute, 3600 is 1 hour, etc. 
			time.sleep(60)

if __name__ == "__main__":

	daemon = YourDaemon(pidfile=PIDFILE,name="YourDaemon")
