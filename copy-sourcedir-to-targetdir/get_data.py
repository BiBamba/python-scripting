import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        
        break
    
    return game_paths

def create_dir(path):
    if not os.path.exists(path):
        os.mkdi(path)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    print(game_paths)

    create_dir(target_path)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory only.")
    # Defintion of the argument from the input
    source, target = args[1:]

    # call of main function
    main(source, target)
    