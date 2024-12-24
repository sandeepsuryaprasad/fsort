from argparse import ArgumentParser
from time import sleep
from pathlib import Path
from datetime import datetime


class FileInfo:
    def __init__(self, name, last_modified, size):
        self.name = name
        self.last_modified = last_modified
        self.size = size

    def __repr__(self):
        return f"({self.name}, {self.last_modified}, {self.size})"


def display_results(items):
    for item in items:
        sleep(0.1)
        print(item)


def get_file_stats(pathobject):
    stats = pathobject.stat()
    return (pathobject.name, datetime.fromtimestamp(stats.st_mtime), stats.st_size)


def sort(dir_path, by):
    files = [ ]
    path = Path(dir_path)
    if by.upper() not in ("NAME", "LAST_MODIFIED", "SIZE"):
        raise Exception("Invalid sort order")
    if not path.exists():
        raise Exception("Invalid path")
    for item in path.glob("*"):
        if item.is_file():
            name, last_modified, size = get_file_stats(item)
            files.append(FileInfo(name, last_modified, size))

    if by.upper() == "NAME":
        display_results(sorted(files, key=lambda item: item.name))
    elif by.upper() == "LAST_MODIFIED":
        display_results(sorted(files, key=lambda item: item.last_modified))
    else:
        display_results(sorted(files, key=lambda item: item.size))
