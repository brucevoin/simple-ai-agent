'''
Description: 
Author: haichun feng
Date: 2024-04-03 15:08:26
LastEditor: haichun feng
LastEditTime: 2024-04-03 15:17:27
'''

from executor_interface import Executor

class TestExecutor(Executor):
    def __init__(self):
        pass
    
    def execute_task(self, task):
        # 执行器1执行任务的具体逻辑
        print("Executor 1 is executing task:", task)

    def task_status(self):
        print("Task completed")