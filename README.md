# fsort-cli

[![Unit tests](https://github.com/sandeepsuryaprasad/fsort/actions/workflows/ci-test.yml/badge.svg?branch=main)](https://github.com/sandeepsuryaprasad/fsort/actions/workflows/ci-test.yml)
[![Development Status](https://img.shields.io/pypi/status/fsort-cli)](https://pypi.org/project/fsort-cli/)
[![Total Downloads](https://static.pepy.tech/badge/fsort-cli)](https://pepy.tech/project/fsort-cli)


`fsort` is a simple yet powerful terminal utility for viewing directory contents in an organized manner on your terminal window.

`fsort` lets you visualise the files in sorted order by `name`, `size`, or `last modified date`.

`fsort` provides a quick and convenient way to view files directly from the command line.

`fsort` does not actually modify/sort the files in the actual file system. It only reads the contents of the directory and displays the file name, size and last modified date in sorted order on terminal.

## Installation

```console
$ pip install fsort-cli
```
## Usage
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
### Demo Example
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files
2026-07-13 19:15:08         0.00 MB	apple.csv
2020-06-29 19:38:19         0.03 MB	apple.pdf
2026-07-13 19:17:14         0.01 MB	bar.py
2026-04-27 17:45:06         0.45 MB	bird.JPG
2026-02-15 09:33:03         0.00 MB	config.ini
2025-06-24 12:33:59         0.00 MB	config.txt
2026-04-27 17:46:08         0.32 MB	elephant.JPG
2026-05-27 17:03:43         0.00 MB	foo.py
2026-07-08 20:01:13         0.44 MB	google.pdf
2026-07-07 21:33:11         0.26 MB	ibm.pdf
2026-07-07 21:33:08         0.06 MB	msft.pdf
2026-04-27 17:43:24         0.43 MB	pic.JPG
2025-12-23 22:12:19         0.00 MB	py.txt
2025-03-14 22:17:03         0.00 MB	run.sh
2026-07-13 19:14:35         0.00 MB	sample.csv
2024-06-21 03:48:24         0.02 MB	sample.log
2026-07-13 19:16:48         0.00 MB	yank.py
2026-04-27 17:43:58         0.38 MB	zebra.JPG
```
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files --key size
2025-12-23 22:12:19         0.00 MB	py.txt
2025-06-24 12:33:59         0.00 MB	config.txt
2026-07-13 19:15:08         0.00 MB	apple.csv
2026-07-13 19:14:35         0.00 MB	sample.csv
2026-07-13 19:16:48         0.00 MB	yank.py
2025-03-14 22:17:03         0.00 MB	run.sh
2026-02-15 09:33:03         0.00 MB	config.ini
2026-05-27 17:03:43         0.00 MB	foo.py
2026-07-13 19:17:14         0.01 MB	bar.py
2024-06-21 03:48:24         0.02 MB	sample.log
2020-06-29 19:38:19         0.03 MB	apple.pdf
2026-07-07 21:33:08         0.06 MB	msft.pdf
2026-07-07 21:33:11         0.26 MB	ibm.pdf
2026-04-27 17:46:08         0.32 MB	elephant.JPG
2026-04-27 17:43:58         0.38 MB	zebra.JPG
2026-04-27 17:43:24         0.43 MB	pic.JPG
2026-07-08 20:01:13         0.44 MB	google.pdf
2026-04-27 17:45:06         0.45 MB	bird.JPG
```
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files --key date
2020-06-29 19:38:19         0.03 MB	apple.pdf
2024-06-21 03:48:24         0.02 MB	sample.log
2025-03-14 22:17:03         0.00 MB	run.sh
2025-06-24 12:33:59         0.00 MB	config.txt
2025-12-23 22:12:19         0.00 MB	py.txt
2026-02-15 09:33:03         0.00 MB	config.ini
2026-04-27 17:43:24         0.43 MB	pic.JPG
2026-04-27 17:43:58         0.38 MB	zebra.JPG
2026-04-27 17:45:06         0.45 MB	bird.JPG
2026-04-27 17:46:08         0.32 MB	elephant.JPG
2026-05-27 17:03:43         0.00 MB	foo.py
2026-07-07 21:33:08         0.06 MB	msft.pdf
2026-07-07 21:33:11         0.26 MB	ibm.pdf
2026-07-08 20:01:13         0.44 MB	google.pdf
2026-07-13 19:14:35         0.00 MB	sample.csv
2026-07-13 19:15:08         0.00 MB	apple.csv
2026-07-13 19:16:48         0.00 MB	yank.py
2026-07-13 19:17:14         0.01 MB	bar.py
```
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files --key size --file-extension pdf
2020-06-29 19:38:19         0.03 MB	apple.pdf
2026-07-07 21:33:08         0.06 MB	msft.pdf
2026-07-07 21:33:11         0.26 MB	ibm.pdf
2026-07-08 20:01:13         0.44 MB	google.pdf
```
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files --key size --file-extension py
2026-07-13 19:16:48         0.00 MB	yank.py
2026-05-27 17:03:43         0.00 MB	foo.py
2026-07-13 19:17:14         0.01 MB	bar.py
```
```console
~$ fsort --path /Users/sandeepsuryaprasad/Desktop/files --key size --file-extension JPG
2026-04-27 17:46:08         0.32 MB	elephant.JPG
2026-04-27 17:43:58         0.38 MB	zebra.JPG
2026-04-27 17:43:24         0.43 MB	pic.JPG
2026-04-27 17:45:06         0.45 MB	bird.JPG
```
## Installed version
```console
$ fsort --version
fsort 0.9.1
```