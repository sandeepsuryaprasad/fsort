from argparse import ArgumentParser
from pathlib import Path

from fsort import __version__

from .file_sort import FileSort


class Result:
    """Represent the outcome of an operation.

    Stores either a successful result value or an error describing
    why the operation failed.

    Attributes:
        value: The value returned by a successful operation.
        error: An error message if the operation failed.

    The `is_ok` property indicates whether the operation succeeded.
    """
    def __init__(self, *, value=None, error=None):
        self.value = value
        self.error = error

    @property
    def is_ok(self):
        return self.error is None

class Validate:
    def validate_path(self, path: str):
        """Validate that the given path exists and is a directory.

        Args:
            path: The directory path to validate.

        Returns:
            Result: Contains the validated Path object on success,
                or an error message if validation fails.
        """
        path = Path(path)
        if not path.exists():
            return Result(error=f"{path!r} does not exist")
        if not path.is_dir():
            return Result(error=f"{path!r} is not a valid directory")
        return Result(value=path)

    def validate_key(self, key: str):
        """Validate the sorting key against the supported options.

        Args:
            key: The sorting key to validate.

        Returns:
            Result: Contains the validated key on success,
                or an error message if the key is invalid.
        """
        sorting_choices = ("name", "size", "date")
        if key not in sorting_choices:
            return Result(error=f"{key!r} is invalid key")
        return Result(value=key)


def _parser():
    """Takes CLI inputs"""
    parser = ArgumentParser()
    parser.add_argument(
        "--path",
        dest="path",
        help="Directory path of the files to be sorted"
    )
    parser.add_argument(
        "--key",
        dest="key",
        help="Sort files by name/size/date"
    )
    parser.add_argument(
        "--file-extension",
        dest="extension",
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

    validate = Validate()

    path = args.path if args.path else "."
    result =  validate.validate_path(path)
    if not result.is_ok:
        parser.error(result.error)

    key = args.key if args.key else "name"
    result = validate.validate_key(key)
    if not result.is_ok:
        parser.error(result.error)

    extension = args.extension if args.extension else "*"

    file = FileSort()
    file.sort(path=path, by_what=key, pattern=extension)
    return 0
