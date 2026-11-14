from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Optional


@dataclass
class FileInfo:
    name: str
    date: datetime
    size: float


class FileSort:
    def _to_mega_bytes(self, bytes: float) -> float:
        return round(bytes / 1024**2, 2)

    def _stats(self, path: Path) -> tuple:
        stats = path.stat()
        file_name = path.name
        last_modified = datetime.fromtimestamp(stats.st_mtime)
        file_size = self._to_mega_bytes(stats.st_size)
        return (file_name, last_modified, file_size)


    def _files_to_sort(self, path: str, extension: str = "*") -> Optional[list[FileInfo]]:
        """Returns list of FileInfo objects"""
        path = Path(path)
        files: list[FileInfo] = []
        for item in path.glob(f"*.{extension}"):
            if item.is_file():
                name, last_modified, size = self._stats(item)
                file_info = FileInfo(name, last_modified, size)
                files.append(file_info)
        return files

    def _print_results(self, items: list[FileInfo]) -> None:
        """Prints the results in the console"""
        for item in items:
            sleep(0.05)
            # Converting all fields to str
            _last_modified: str = item.date.strftime("%Y-%m-%d %H:%M:%S")
            _size: str = f"{item.size:.2f} MB"
            _file_name: str = item.name
            print(f"{_last_modified:<20} {_size:>14}\t{_file_name}")

    def sort(self, path: str, by_what: str, pattern: str) -> None:
        """Sorts the list of files"""
        files_to_sort = self._files_to_sort(path, pattern)
        if not files_to_sort:
            return
        self._print_results(sorted(files_to_sort, key=lambda item: getattr(item, by_what)))
