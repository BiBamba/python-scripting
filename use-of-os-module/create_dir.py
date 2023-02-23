# import os module
import os
import sys

def list_dir(given_dir):
# list all the files and direcotry
    source_dir_list = os.listdir(given_dir)
    print("Here are the contents of '% s'" % given_dir)
    print(source_dir_list)

def create_dir(target_dir,new_dir):
    # mode 
    mode = 0o666

    # Path
    paths = os.path.join(target_dir, new_dir)

    # Create the directory
    os.mkdir(paths, mode)
    print("Directory '% s' is created" % new_dir)

def main(source,target):
    list_dir(source)
    create_dir(source,target)

if __name__ == "__main__":
    # command line argument
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must enter a source and target directory")
    source, target = args[1:] 
    main(source,target)
