import os
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s: %(module)s]: %(message)s: '
log_dir = "logs"
log_filepath = ps.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir)