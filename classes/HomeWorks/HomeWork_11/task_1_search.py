import shelve
from task_1_store import Pupil


with shelve.open('pupils.db', 'r') as db:
    rows = []
    for i in db:
        rows.append(db[i])

print(rows)

data = {
        input('Enter first name: '),
        input('Enter last name: '),
        input('Enter gender (male/female): '),
        input('Enter age: ')
}.difference({'',})

for pupil in rows:
    if pupil.search(data):
        print('-' * 80)
        print("First Name: {pupil.f_name}\n"
              "Last Name: {pupil.l_name}\n"
              "Gender: {pupil.gen}\n"
              "Mark: {pupil.mark}".format(pupil=pupil))

