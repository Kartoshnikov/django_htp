'''
area
circumference
volume
formulas = {
            'rectangle': ...,
            'square': ...,
            'triangle': ...,
            'circle': ...,
            'trapeze': ...
        }
'''
import math

figures = {}


def register(obj):
    figures[obj.__name__.lower()] = obj
    return obj


class Figure:
    def __init__(self, *args):
        if len(args) == 1:
            self.arg = args[0]
        else:
            self.edges = args

    def circumference(self):
        return sum(self.edges)

    def volume(self):
        return 'Flat figures have no volume property'

    def __getattr__(self, attr):
        return False



@register
class Rectangle(Figure):
    def area(self):
        return self.edges[0] * self.edges[1]

    def circumference(self):
        return 2 * self.edges[0] + 2 * self.edges[1]


@register
class Square(Figure):
    def circumference(self):
        return 4 * self.arg

    def area(self):
        return self.arg ** 2


@register
class Triangle(Figure):
    def area(self):
        return 0.5 * self.edges[0] * self.edges[1] * math.degrees(math.sin(self.edges[0] / self.edges[1]))


@register
class Circle(Figure):
    def circumference(self):
        return 2 * self.arg * math.pi

    def area(self):
        return math.pi * pow(self.arg, 2)


@register
class Trapeze(Figure):
    def area(self):
        a, d, b, c = (x for x in self.edges)
        try:
            sq = (a + b)/2 * math.sqrt(c**2 - pow(((pow(b - a, 2) + c**2 - d**2)/2*(b - a)), 2))
        except ValueError:
            return 'Wrong values of edges'
        return sq


while True:
    line = input('Enter figure (rectangle|square|triangle|circle|trapeze) and edges (exit|help): ').split()
    if line == 'exit':
        break
    elif line == 'help':
        print('usage:\nExample: rectangle 1 2 6 32\nExample: circle 12\n in case of circle, nubber is arg')
        continue

    rules = {
        'rectangle': 3,
        'square': 2,
        'triangle': 4,
        'circle': 2,
        'trapeze': 5
    }

    if not rules.get(line[0]) == len(line):
        print("Wrong number of arguments for this figure")
        [print('{} => {}'.format(key, val)) for key, val in rules.items()]
        print()
        continue

    figure = figures.get(line[0])(*[int(x) for x in line[1:]])
    if not figure is None:
        print('{}\narea: {}\ncircumference: {}\nvolume: {}\n'.format(line[0],
                                                                       figure.area(),
                                                                       figure.circumference(),
                                                                       figure.volume()))
