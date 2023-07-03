from datetime import datetime
import time
import sys

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def write_to_stdout(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()

def write_to_stderr(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

for i in range(10):
    msg = f'message {i}\n'
    write_to_stdout(msg)
    # write_to_stderr(f'{get_current_time()} wrote: ' + msg)
    time.sleep(2)
