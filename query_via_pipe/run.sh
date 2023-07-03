rm -f mypipe
mkfifo mypipe
python custom_file_reader.py >> mypipe &
python run_pandas.py
