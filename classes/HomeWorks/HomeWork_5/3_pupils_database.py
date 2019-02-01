def find(first_name=None, last_name=None, gender=None, age=None):
    if not (first_name or last_name or gender or age): print("No arguments were passed!")
    args = {first_name, last_name, gender, age}; args.discard('')
    for num, line in enumerate(database):
        if args.issubset(set(line)):
            print(num, "- {0} {1} is a {2} and {3} years old".format(*line))



database = [
    ['Ivan', 'Ivanov', 'male', 8],
    ['Mike', 'Smith', 'male', 12],
    ['Nona', 'Maht', 'female', 6]
]


first_name = input("Enter name: ")
last_name = input("Enter last_name: ")
gender = input("Enter gender: ")
try:
    age = int(input("Enter age: "))
except:
    age = ''



find(first_name, last_name, gender, age)