# import os module
import os

# Function to get the current working directory.
def current_path():
    previous_wd = os.getcwd()
    print("Current working directory before")
    print(previous_wd)
    print()

# Printing Current working directory before chaning directory
current_path()

# Changing the Current working directory
os.chdir('../')

# print current working directory
current_path()

