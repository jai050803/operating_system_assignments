# Subtask 1: Initialize the logging
import logging

logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

logging.info("Logging system initialized")

