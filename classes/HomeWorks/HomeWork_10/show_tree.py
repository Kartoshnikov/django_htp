import os
import os.path as path


pwd = input('Enter root to show tree from: ')


def show_tree(pwd, indent=0):
    pwd = path.normpath(pwd)
    for entry in os.scandir(pwd):
        if not entry.is_dir():
            print('|--{} {} '.format('-' * indent, entry.name))
            continue
        print('|--{} {}\\'.format('-' * indent, entry.name))
        show_tree(entry, indent+4)


print(path.normpath(pwd), '\\', sep='')
show_tree(pwd)
