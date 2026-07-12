# fsort-cli

A lightweight command-line utility for sorting files in a directory by file name, file size, or last modified date.

## Installation

```console
pip install fsort-cli
```

## Usage

By default `fsort` sorts the files in the current working directory by file "name"
```console
fsort
```

You can specify the directory using `--path` cli argument
```console
fsort --path /path/to/directory
```

You can specify by what order the files need to be sorted using `--key` cli argument
```console
fsort --path /path/to/directory --key size

fsort --path /path/to/directory --key date

fsort --path /path/to/directory --key name
```

You can sort specific types of files using `--file-extension` cli argument.

Sort all jpg files by "name"
```console
fsort --path /path/to/directory --key name --file-extension jpg
```

Sort all txt files by "size"

```console
fsort --path /path/to/directory --key size --file-extension txt
```

Sort all png files by "last modified date"
```console
fsort --path /path/to/directory --key date --file-extension png
```