from argparse import ArgumentParser
from importlib.metadata import version

from fsort.file_sort import FileSort


def console_entry():
    """Takes CLI inputs"""
    sorting_choices = ("name", "size", "date")
    _parser = ArgumentParser()
    _parser.add_argument(
        "--path",
        dest="path",
        default=".",
        help="Directory path of the files to be sorted"
    )
    _parser.add_argument(
        "--key",
        dest="key",
        default="name",
        choices=sorting_choices,
        help="Sort files by name/size/date"
    )
    _parser.add_argument(
        "--file-extension",
        dest="extension",
        default="*",
        help="File extension pattern e.g txt, pdf, jpg"
    )
    _parser.add_argument(
        "--version",
        action="version",
        version=f"fsort {version('fsort')}"
    )

    parser = _parser.parse_args()
    return parser


def run():
    """Executes sort"""
    parser = console_entry()
    file = FileSort()
    file.sort(path=parser.path, by_what=parser.key, pattern=parser.extension)


if __name__ == "__main__":
    run()