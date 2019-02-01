from random import sample

A = [[x for x in sample(range(99), 3)] for i in range(4)]
initial_data = input("Enter two numbers (p1 p2) with space and p1 < p2: ")
try:
    p1, p2 = (int(x) for x in initial_data.split())
    if p1 > p2: print("p1 > p2"); raise Exception
except:
    print("Wrong data!")
    exit(1)



print("Initial maxtix: ")
for line in A:
    print()
    for elem in line:
        print("{0:>2d}".format(elem), end=" ")
print("\n")

count = 0
for i in A:
    for j in i:
        if p1 < j < p2: count += 1

print("Count of numbers that satisfy the requirements: ", count)

