# import json
import shelve

_list = [
    {'f_name': 'Dima', 'l_name': 'Kartoshnikov', 'gen': 'male', 'mark': 4},
    {'f_name': 'Dima', 'l_name': 'Ivanov', 'gen': 'male', 'mark': 4},
    {'f_name': 'Bob', 'l_name': 'Smith', 'gen': 'male', 'mark': 2},
    {'f_name': 'Kate', 'l_name': 'Ramsel', 'gen': 'female', 'mark': 5}
]


class Pupil:
    def __init__(self, f_name, l_name, gen, mark):
        self.f_name = f_name
        self.l_name = l_name
        self.gen = gen
        self.mark = str(mark)

    def search(self, items):
        print(items)
        if items == {}: return False
        return set(self.__dict__.values()).issuperset(items)


with shelve.open('pupils.db', 'c') as db:
    for i, data in enumerate(_list):
        db[str(i)] = Pupil(**data)
