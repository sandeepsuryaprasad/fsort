
[![CI](https://github.com/sandeepsuryaprasad/fsort/actions/workflows/ci-test.yml/badge.svg?branch=main)](https://github.com/sandeepsuryaprasad/fsort/actions/workflows/ci-test.yml)  [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# fsort-cli

`fsort` is a simple yet powerful terminal utility for viewing directory contents in an organized manner on your terminal window.

`fsort` lets you visualise the files in sorted order by `name`, `size`, or `last modified date`.

`fsort` provides a quick and convenient way to view files directly from the command line.

`fsort` does not actually modify/sort the files in the actual file system. It only reads the contents of the directory and displays the file name, size and last modified date in sorted order on terminal.

![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort.png)
![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort_key_size.png)
![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort_key_date.png)
![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort_key_file_extension_pdf.png)
![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort_key_file_extension_py.png)
![fsort](https://raw.githubusercontent.com/sandeepsuryaprasad/fsort/main/images/fsort_key_file_extension_jpg.png)

### Installation

```console
$ pip install fsort-cli
```

```console
$ fsort --version
fsort 0.8.0
```

### Usage

By default `fsort` sorts the files in the current working directory by file "name"
```console
fsort
```

You can specify the directory using `--path` CLI argument
```console
fsort --path /path/to/directory
```

You can specify by what order the files need to be sorted using `--key` CLI argument

Mac/Linux:
```console
fsort --path /path/to/directory --key size

fsort --path /path/to/directory --key date

fsort --path /path/to/directory --key name
```
NOTE: Windows users please enclose the directory path in quotes. For Mac/Linux users wrapping the directory path in quotes is not mandatory.

Windows:
```console
fsort --path "C:\path\to\directory" --key size

fsort --path "C:\path\to\directory" --key date

fsort --path "C:\path\to\directory" --key name
```

You can sort specific file types using `--file-extension` CLI argument.

### Usage

Sort only those files with `jpg` extension by "name"

```console
fsort --path /path/to/directory --key name --file-extension jpg
```

Sort only those files with `txt` extension by "size"
```console
fsort --path /path/to/directory --key size --file-extension txt
```

Sort only those files with `png` extension by "last modified date"
```console
fsort --path /path/to/directory --key date --file-extension png
```