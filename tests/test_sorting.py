import subprocess
from datetime import datetime


def to_date_time(date_time_string):
    """Convert date_time_string to date_time object"""
    return datetime.strptime(date_time_string, "%Y-%m-%d %H:%M:%S")


def test_sorting_default_order_all_files():
    result = subprocess.run(
        "fsort --path ./tests/files | awk '{print $5}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ _file for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_by_name():
    result = subprocess.run(
        "fsort --path ./tests/files --key name | awk '{print $5}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ _file for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_by_file_size():
    result = subprocess.run(
        "fsort --path ./tests/files --key size | awk '{print $3}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ float(_file) for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_by_last_modified_date():
    result = subprocess.run(
        "fsort --key date | awk '{print $1, $2}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ to_date_time(_file)  for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_invalid_dir_path():
    result = subprocess.run(
        "fsort --path ./invalid/path",
        capture_output=True,
        shell=True,
        text=True
    )
    assert "not a valid directory" in result.stdout

def test_sorting_txt_files_by_name():
    result = subprocess.run(
        "fsort --path ./tests/files --file-extension txt | awk '{print $5}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [_file for _file in files_list if _file.strip()]
    assert "txt" not in _files_list

def test_sorting_jpg_files_by_size():
    result = subprocess.run(
        "fsort --path ./tests/files --file-extension jpg --key size | awk '{print $3}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ float(_file) for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_pdf_files_by_last_modified_date():
    result = subprocess.run(
        "fsort --path ./tests/files --file-extension pdf --key date | awk '{print $1, $2}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ to_date_time(_file)  for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)
