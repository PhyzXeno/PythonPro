# this script deletes every file who ends with "p.downloading" in ./  

import os

from os.path import join, getsize

for root, dirs, files in os.walk('./'):   # root lists current dir; dirs is all directories; files is all fieles; dirs and files are lists
    for name in files:
        filename = join(root, name)   # get relative file path
        if "p.downloading" in filename:
            os.remove(filename)
