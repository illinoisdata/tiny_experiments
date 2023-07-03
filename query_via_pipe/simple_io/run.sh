rm -f mypipe
mkfifo mypipe
python writer.py >> mypipe &
python reader.py < mypipe
