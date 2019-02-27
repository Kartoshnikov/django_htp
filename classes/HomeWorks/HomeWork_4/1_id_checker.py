from string import ascii_letters, digits

def my_input():
    while True:
        my_string = input("Enter alleged ID: ")
        if my_string.startswith(tuple(digits)) or len(my_string.split()) > 1:
            print("Id can't start with number or contain spaces or tabs!")
            continue
        break
    return my_string

def validate(string):
    control_group = ascii_letters + digits + '_'
    if not set(string).issubset(set(control_group)): print("The string contains wrong symbols!")
    else: print("Allowed ID.")

validate(my_input())
#print(ascii_letters + digits + '_')

