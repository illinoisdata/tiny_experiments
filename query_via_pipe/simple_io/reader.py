from datetime import datetime
import sys


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

with sys.stdin as f:
    while True:
        buffer = f.buffer.read(1)
        if buffer == b'':
            break
        sys.stdout.write(buffer.decode('utf-8'))
        sys.stdout.flush()
