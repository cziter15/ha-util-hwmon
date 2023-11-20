import os
import sys
import time
import ctypes
import configparser
from providers import *

# Importing the MessageBox function from the ctypes library
MessageBox = ctypes.windll.user32.MessageBoxW

class MetricHandler:
	"""Class to handle metrics"""

	def __init__(self, client, updateTime):
		"""
		Initialize MetricHandler object

		Args:
			client: MQTT client object
			updateTime: Time interval for updating metrics
		"""
		self._providers = []
		self._mqttClient = client
		self._updateTime = updateTime
		self._currentTimestamp = time.time()
		self._prefix = "hwinfo/"

	def addProvider(self, provider):
		"""
		Add a provider to the list of providers

		Args:
			provider: Provider object
		"""
		self._providers.append(provider)

	def sendUpdate(self):
		"""Send metric update to MQTT broker"""
		for provider in self._providers:
			if provider.isValid():
				self._mqttClient.publish(self._prefix + provider.getName(), provider.getValue())

	def loop(self):
		"""Main loop for updating metrics"""
		if (time.time() - self._currentTimestamp) > self._updateTime:
			self.sendUpdate()
			self._currentTimestamp = time.time()

def main():
	"""Main function"""

	print("Starting...")

	config = configparser.ConfigParser()
	config.read('config.ini')

	client = mqtt.Client()
	client.username_pw_set(config.get('credentials', 'user'), config.get('credentials', 'pass'))
	client.connect(config.get('credentials', 'host'), 1883, 60)

	Metrics = MetricHandler(client, 15)

	Metrics.addProvider(CPUUsageMetricProvider())
	Metrics.addProvider(RAMUsageMetricProvider())
	Metrics.addProvider(GPUTempMetricProvider())

	while True:
		Metrics.loop()
		client.loop()

if __name__ == "__main__":
	if "task" in sys.argv:
		main()
	else:
		from taskscheduler import *
		scheduler = TaskScheduler()
		if "install" in sys.argv:
			script_path = os.path.abspath(sys.argv[0])
			try:
				scheduler.create_or_update_task('PerfMonMQTT', script_path)
				MessageBox(None, 'Scheduled task has been created', 'Info',  0)
			except Exception as e:
				MessageBox(None, 'Scheduled task creation failed!\n\n' + str(e), 'Info', 0)
		else:
			if "uninstall" in sys.argv:
				try:
					scheduler.delete_scheduled_task('PerfMonMQTT')
					MessageBox(None, 'Scheduled task has been deleted', 'Info',  0)
				except Exception as e:
					MessageBox(None, 'Scheduled task deletion failed!\n\n' + str(e), 'Info', 0)
			else:
				MessageBox(None, 'No args specified!\n\n[WITH ADMING RIGHTS]\nUsage: python monitor.py install', 'Info', 0)
				pass