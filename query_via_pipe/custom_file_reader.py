import sys
import time


def write_to_stdout(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


def gen_header():
    return 'col1,col2\n'


def gen_row():
    return 'hello,world\n'


def write_csv(row_count=10):
    write_to_stdout(gen_header())
    for _ in range(row_count):
        time.sleep(1)
        write_to_stdout(gen_row())


if __name__ == "__main__":
    write_csv()
