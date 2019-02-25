class Elevator:
    floors = 15
    elevators = []

    def __init__(self, name):
        self.new = True
        self.current = 1
        self.liftings = 0
        self.name = name
        self.__class__.elevators.append(self)

    def lift(self, floor):
        if floor <= 0 or floor > self.__class__.floors:
            print('Wrong floor')
        if self.current < floor:
            self.up(floor)
        elif self.current > floor:
            self.down(floor)

    def up(self, floor):
        print('going up ...')
        if self.new: self.new = False
        self.liftings += 1
        self.current = floor

    def down(self, floor):
        print('going down ...')
        self.current = floor

    def show(self):
        print(self.current)

    @classmethod
    def sum_liftings(cls):
        return sum((lift.liftings for lift in  cls.elevators))

    def __add__(self, other):
        return self.liftings + other
    __radd__ = __add__

    def __sub__(self, other):
        if self.new: print('Wrong operation!')
        return self.liftings - other

    def __rsub__(self, other):
        if self.new: print('Wrong operation!')
        return other - self.liftings

    def __lt__(self, other):
        return self.liftings < other

    def __gt__(self, other):
        return self.liftings > other

    def __str__(self):
        self.percent = self.liftings/self.__class__.sum_liftings() * 100
        return '-'*80 \
               + f'\nLift name: {self.name}\n' \
                 f'Liftings: {self.liftings}\n'\
                 f'Percent: {round(self.percent, 2)}\n'\
               + '-'*80

lift_1 = Elevator('lift_1')
lift_1.lift(10)
lift_1.lift(5)
lift_1.lift(1)
lift_1.lift(15)

lift_2 = Elevator('lift_2')
lift_2.lift(5)
lift_2.lift(6)
lift_2.lift(10)
lift_2.lift(1)

lift_3 = Elevator('lift_3')
lift_3.lift(10)
lift_3.lift(2)
lift_3.lift(6)
lift_3.lift(1)
print(lift_1.liftings, lift_2.liftings, lift_3.liftings, Elevator.sum_liftings())
print(lift_2 > lift_1, lift_1 + lift_3, lift_3 - lift_2)
print(lift_1)
