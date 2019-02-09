import os
from os import path

while True:
    _dir = input('Enter directory to list (or exit): ')
    if not _dir or _dir == 'exit': break

    with os.scandir(path.normpath(_dir)) as it:
        for elem in it:
            print(elem.name)