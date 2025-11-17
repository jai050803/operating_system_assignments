import logging
import multiprocessing
from task2 import system_process    # your dummy task

if __name__ == "__main__":
    logging.info("System shutdown check initiated")

    # Create processes again
    p1 = multiprocessing.Process(target=system_process, args=('process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('process-2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    logging.info("System shutdown complete")
    print("system shutdown")

