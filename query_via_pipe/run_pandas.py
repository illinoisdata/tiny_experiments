import pandas as pd
import time


start_time = time.time()
df = pd.read_csv('mypipe')
print(df.count())
elapsed_time = time.time() - start_time

print('elapsed time: {:.3f} secs'.format(elapsed_time))
print('''If the above elapsed time is roughly 10 seconds, it means that the DB layer is
automatically blocked until the custom file reader completes writing to a named pipe.''')