import os.path
def create_f(name):
    with open(os.path.normpath(name), 'x'):
        ...


# create_f(input("Enter name of file or absolute path: "))