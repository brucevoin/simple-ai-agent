'''
Description: 
Author: haichun feng
Date: 2024-04-03 15:08:26
LastEditor: haichun feng
LastEditTime: 2024-04-03 15:41:31
'''

from task_interface import Task
from test_executor import TestExecutor
from job import Job

class Supervisor:
    def __init__(self, executors):
        self.executors = executors
    
    def make_plan(self, job):

        print("Supervisor is making a plan for the Job", job)
        # Split the job into tasks and assign the task to the executor which is the best one to handle the task
        for task in tasks:
            # 
            pass

    def assign_task(self,tasks):
        pass

    def check_tasks(self):
        pass

    def accept(self,job):
        tasks = self.make_plan(job=job)
        self.assign_task(tasks=tasks)
        while(True):
            for task in tasks:
                if task.failed:
                    # what's the other way to solve the task?
                    # reassign task
                    pass
            


job = Job()
executor = TestExecutor()
supervisor = Supervisor([executor])
supervisor.accept(job=job)