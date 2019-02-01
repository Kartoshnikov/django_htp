grades = (['Ann', 9], ['Mark', 6], ['Kenny', 10])
a = list(grades)
a.sort(key=lambda x: x[1])
for name, grade in a:
    print("Hello {0}! Your grade is {1}.".format(name, grade))