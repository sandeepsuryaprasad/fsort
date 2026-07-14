import subprocess

def test_sorting_default_order_all_files():
    result = subprocess.run(
        "fsort --path ./files | awk '{print $5}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ _file for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_by_name():
    result = subprocess.run(
        "fsort --path ./files --key name | awk '{print $5}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ _file for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

def test_sorting_by_file_size():
    result = subprocess.run(
        "fsort --path ./files --key size | awk '{print $3}'",
        capture_output=True,
        shell=True,
        text=True
    )
    files_list = result.stdout.split("\n")
    _files_list = [ float(_file) for _file in files_list if _file.strip()]
    assert _files_list == sorted(_files_list)

# def test_sorting_by_last_modified_date():
#     result = subprocess.run("fsort --key date", capture_output=True, shell=True, text=True)

# def test_sorting_invalid_dir_path():
#     result = subprocess.run("fsort --path /invalid/path", capture_output=True, shell=True, text=True)
#
# def test_sorting_valid_path():
#     result = subprocess.run("fsort --path ./files", capture_output=True, shell=True, text=True)
#
# def test_sorting_txt_files_by_name():
#     result = subprocess.run("fsort --path ./files --file-extension txt", capture_output=True, shell=True, text=True)
#
# def test_sorting_jpg_files_by_size():
#     result = subprocess.run("fsort --path ./files --file-extension jpg key size", capture_output=True, shell=True, text=True)
#
# def test_sorting_pdf_files_by_last_modified_date():
#     result = subprocess.run("fsort --path ./files --file-extension pdf key date", capture_output=True, shell=True, text=True)