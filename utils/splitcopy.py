import sys, os
from os.path import isdir, abspath, join
import json
import shutil

def CopyFilesFromJSONDictToDir(json_file, src_dir, dest_dir):
    """
    Given a json file containing a dictionary where keys are sub-directories to
    create in the dest_dir and values are the filenames that belong in those
    respective sub-directories, copy files from src_dir to their respective sub-
    directories accordingly.
    """
    if not isdir(parent_dir):
        raise Exception("Parent directory does not exist")
    with open(json_file, "r") as f:
        split_data = json.load(f)
    for key, val in split_data.items():
        src = join(src_dir, val)
        dest_dir = join(parent_dir, key)
        if not isdir(dest_dir):
            os.makedirs(dest_dir)
        shutil.copy2(src, dest_dir)

if __name__ == "__main__":
    # JSON File containing dictionary with filenames for respective split
    split_file = abspath(sys.argv[1])
    # Source directory
    src_dir = abspath(sys.argv[2])
    # Parent destination directory
    parent_dir = abspath(sys.argv[3])
    CopyFilesFromJSONDictToDir(split_file, src_dir, parent_dir)
