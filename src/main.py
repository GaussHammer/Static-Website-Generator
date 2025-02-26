from textnode import *
from htmlnode import *
from shutil import rmtree, copy
from os import path, mkdir, listdir
from generate_page import *

def main():
    copy_static()
    generate_page_recursive("content", "template.html", "public")

def copy_static(source = "static", destination = "public"):
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