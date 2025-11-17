# Subtask 3: Create two processes and run them concurrently
import logging
import multiprocessing

from task2 import system_process   # If you keep Subtask 2 in another file

if __name__ == '__main__':
    print("system starting")
    logging.info("System startup initiated")

    p1 = multiprocessing.Process(target=system_process, args=('process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('process-2',))

    p1.start()
    p2.start()
