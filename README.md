# fsort-cli

A lightweight command-line utility for sorting files in a directory by file name, file size, or last modified date.

### Installation

```console
$ pip install fsort-cli
```

```console
$ fsort --version
fsort 0.5.0
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