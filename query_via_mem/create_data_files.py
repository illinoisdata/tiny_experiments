import os

DATA_FILE = 'mydata.csv'
REPLICA_FILES = ['mydata_direct.csv', 'mydata_via_mem.csv']
TEMP_FILE = 'temp'
TARGET_SIZE = int(1e9)
COL_COUNT = 10


def gen_a_row():
    row = ''
    for i in range(COL_COUNT):
        if i != 0:
            row += ','
        row += f'mycolhelloworld{i}'
    return row


def gen_header():
    row = ''
    for i in range(COL_COUNT):
        if i != 0:
            row += ','
        row += f'colname{i}'
    return row


ITR_MAX = 1000
for i in range(ITR_MAX):
    new_file = f'{TEMP_FILE}{i}'
    if i == 0:
        row = gen_a_row()
        os.system('echo "{}" > {}'.format(row, new_file))
        continue
    prev_file = f'{TEMP_FILE}{i-1}'
    os.system('cat {} {} > {}'.format(prev_file, prev_file, new_file))
    fsize = os.path.getsize(new_file)
    if fsize >= TARGET_SIZE:
        break


os.system('echo "{}" > {}'.format(gen_header(), DATA_FILE))
os.system('cat {} >> {}'.format(new_file, DATA_FILE))
for fname in REPLICA_FILES:
    os.system('cp {} {}'.format(DATA_FILE, fname))
os.system('rm temp*')
