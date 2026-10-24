from argparse import ArgumentParser

from fsort import __version__

from .file_sort import FileSort


def _parser():
    """Takes CLI inputs"""
    sorting_choices = ("name", "size", "date")
    parser = ArgumentParser()
    parser.add_argument(
        "--path",
        dest="path",
        default=".",
        help="Directory path of the files to be sorted"
    )
    parser.add_argument(
        "--key",
        dest="key",
        default="name",
        choices=sorting_choices,
        help="Sort files by name/size/date"
    )
    parser.add_argument(
        "--file-extension",
        dest="extension",
        default="*",
        help="File extension pattern e.g txt, pdf, jpg"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"fsort {__version__}"
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Executes sort"""
    parser = _parser()
    args = parser.parse_args(argv)
    file = FileSort()
    file.sort(path=args.path, by_what=args.key, pattern=args.extension)
    return 0
