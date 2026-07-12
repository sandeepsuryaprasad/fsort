import subprocess
from datetime import datetime, timedelta
from src.fsort.file_sort import FileSort

td = datetime.now()
t_delta_micro_seconds = timedelta(microseconds=20)
t_delta_milli_seconds = timedelta(milliseconds=10)
t_delta_seconds = timedelta(seconds=1)
t_delta_mins = timedelta(minutes=1)
t_delta_hours = timedelta(hours=1)
t_delta_days = timedelta(days=1)
t_delta_year = timedelta(days=364)

test_files = [
    ("abs.txt", 0.12, td + t_delta_seconds),
    ("junk.pdf", 12.34, td + t_delta_mins),
    ("notes.txt", 99.1, td + t_delta_hours),
    ("config.ini", 0.98, td + t_delta_days),
    ("demo.png", 10.29, td + t_delta_year),
    ("spam.jpg", 10.28, td - t_delta_seconds),
    ("Apple.txt", 9.99, td - t_delta_hours),
    ("GOOGLE.pdf", 9.98, td - t_delta_days),
    ("Microsoft.txt", 9.97, td - t_delta_year)
]

def test_file_sort_by_name():
    file_sort = FileSort()
    file_sort.sort()

def test_file_sort_by_date():
    subprocess.run("fsort --date=")

def test_file_sort_size():
    ...

def test_invalid_path():
    ...

def test_invalid_extension():
    ...