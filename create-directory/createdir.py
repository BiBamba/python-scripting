import os
import sys

args = sys.argv
if len(args) != 3:
    raise Exception("You must pass target directory and directory to create")
target, createddir = args[1:]



