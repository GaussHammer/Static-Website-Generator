from textnode import *
from htmlnode import *
from shutil import rmtree, copy
from os import path, mkdir, listdir
from generate_page import *
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static()
    generate_pages_recursive("content", "template.html", "docs", basepath)

def copy_static(source = "static", destination = "docs"):
    if source == "static":
        if path.exists(destination):
            rmtree(destination)
            print("public deleted")
        mkdir(destination)
    elif not path.exists(destination):
        mkdir(destination)
    list_dir_static = listdir(source)
    for dir in list_dir_static:
        source_path = path.join(source, dir)
        dest_path = path.join(destination, dir)
        if path.isfile(source_path):
            copy(source_path,dest_path)
        else:
            mkdir(dest_path)
            copy_static(source_path, dest_path)
main()