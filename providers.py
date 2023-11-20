import paho.mqtt.client as mqtt
import psutil

class MetricProvider:
	def __init__(self):
		self._Name = "None"
		
	def getValue():
		"""
		Returns the metric value.
		
		Returns:
			int: The metric value.
		"""
		return 0

	def isValid(self):
		"""
		Checks if the metric provider is valid.
		
		Returns:
			bool: True if the metric provider is valid, False otherwise.
		"""
		return False
	
	def getName(self):
		"""
		Returns the name of the metric provider.
		
		Returns:
			str: The name of the metric provider.
		"""
		return self._Name
	
class GPUTempMetricProvider(MetricProvider):
	def __init__(self):
		self._Name = "gpu_temperature_celsius"
		try:
			from pyadl import ADLManager
			self._adlDevices = ADLManager.getInstance().getDevices()
		except:
			self._adlDevices = None

	def isValid(self):
		"""
		Checks if the GPU temperature metric provider is valid.
		
		Returns:
			bool: True if the GPU temperature metric provider is valid, False otherwise.
		"""
		if (self._adlDevices is not None):
			if (len(self._adlDevices) > 0):
				return True
		return False
	
	def getValue(self):
		"""
		Returns the GPU temperature value.
		
		Returns:
			int: The GPU temperature value.
		"""
		return self._adlDevices[0].getCurrentTemperature()
	
class CPUUsageMetricProvider(MetricProvider):
	def __init__(self):
		self._Name = "cpu_utilization_percent"
		
	def isValid(self):
		"""
		Checks if the CPU usage metric provider is valid.
		
		Returns:
			bool: True if the CPU usage metric provider is valid, False otherwise.
		"""
		return True
		
	def getValue(self):
		"""
		Returns the CPU utilization value.
		
		Returns:
			float: The CPU utilization value.
		"""
		return round(psutil.cpu_percent(), 1)
	
class RAMUsageMetricProvider(MetricProvider):
	def __init__(self):
		self._Name = "ram_used_percent"
		
	def isValid(self):
		"""
		Checks if the RAM usage metric provider is valid.
		
		Returns:
			bool: True if the RAM usage metric provider is valid, False otherwise.
		"""
		return True
		
	def getValue(self):
		"""
		Returns the RAM usage value.
		
		Returns:
			float: The RAM usage value.
		"""
		return round(psutil.virtual_memory().percent, 1)