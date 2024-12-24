from fsort.file_sort import sort
from argparse import ArgumentParser
import click

@click.command()
@click.option("--path", default=".", help="Directory path where the files need to be sorted")
@click.option("--key", default="name", help="Sort files by name/size/last_modified")
@click.version_option(package_name="fsort")
def run(path, key):
    sort(path, key)


if __name__ == "__main__":
    run()
