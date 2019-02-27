import json
import argparse


class Pupil:
    def search(self, items):
        if items == set(): return False
        return set(self.__dict__.values()).issuperset(items)


class PupilJSON(Pupil):
    def __init__(self, data):
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.gen = data['gen']
        self.mark = data['mark']

    @staticmethod
    def open():
        with open('pupils.json') as DB:
            for line in DB:
                yield json.loads(line, parse_int=str)


class PupilFILE(Pupil):
    DB = 'pupils.txt'

    def __init__(self, data):
        data = data.split()
        self.f_name = data[0]
        self.l_name = data[1]
        self.gen = data[2]
        self.mark = data[3]

    @staticmethod
    def open():
        with open('pupils.txt') as DB:
            for line in DB:
                yield line


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pupils database')
    parser.add_argument('-t', dest='type', choices=['json', 'text'], default='json', help='type of file to open')
    args = parser.parse_args()
    if args.type == 'json':
        Maker = PupilJSON
    else:
        Maker = PupilFILE

    data = {
        input('Enter first name: '),
        input('Enter last name: '),
        input('Enter gender (male/female): '),
        input('Enter mark: ')
    }.difference({'', })

    for row in Maker.open():
        pupil = Maker(row)
        if pupil.search(data):
            print('-' * 80)
            print("First Name: {pupil.f_name}\n"
                  "Last Name: {pupil.l_name}\n"
                  "Gender: {pupil.gen}\n"
                  "Mark: {pupil.mark}".format(pupil=pupil))
