grades = [('Ann', 9), ('Mark', 6), ('Kenny', 10)]
grades.sort(key=lambda x: x[1])
for name, grade in grades:
    print("Hello {0}! Your grade is {1}.".format(name, grade))