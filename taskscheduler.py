import win32com.client
import os

class TaskScheduler:
	def __init__(self):
		self.scheduler = win32com.client.Dispatch('Schedule.Service')
		self.scheduler.Connect()
		self.root_folder = self.scheduler.GetFolder('\\')
		
	def delete_task(self, task_name):
		"""
		Delete a task by name.

		Args:
			task_name (str): The name of the task to be deleted.
		"""
		scheduler = win32com.client.Dispatch('Schedule.Service')
		scheduler.Connect()
		root_folder = scheduler.GetFolder('\\') # root
		root_folder.DeleteTask(task_name, 0)

	def create_or_update_task(self, task_name, exe_path):
		"""
		Create or update a task.

		Args:
			task_name (str): The name of the task.
			exe_path (str): The path to the executable.

		"""
		scheduler = win32com.client.Dispatch('Schedule.Service')
		scheduler.Connect()
		root_folder = scheduler.GetFolder('\\') # root

		# Create a task definition
		task_def = scheduler.NewTask(0)  # 0 TASK_CREATE_OR_UPDATE
		task_def.Principal.RunLevel = 1 # Highest
		task_def.Settings.ExecutionTimeLimit = "PT0S" # No time limit

		# Create an action (e.g., execute a program)
		exec_action = task_def.Actions.Create(0)  # 0 corresponds to an executable action
		exec_action.Path = exe_path
		exec_action.WorkingDirectory = os.path.dirname(exe_path)
		exec_action.Arguments = 'task'

		# Create a trigger.
		trigger = task_def.Triggers.Create(8)  # boot
		trigger.Delay = "PT5M"

		# Register the task
		root_folder.RegisterTaskDefinition(
			task_name,
			task_def,
			6,  # TASK_CREATE_OR_UPDATE
			None,  # User and password are None for the current user
			None,
			2, # TASK_LOGON_S4U
		)