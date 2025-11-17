# Subtask 2: Define the Dummy Task
import logging
import time

def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)
    logging.info(f"{task_name} ended")
