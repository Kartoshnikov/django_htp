from random import sample


try:
    size = int(input('Enter size of matrix (N): '))
except:
    print("Wrong N!"); exit(1)


A = [[x for x in sample(range(-size, size+1), size)] for i in range(size)]

print("Initial maxtix: ")
for line in A:
    print()
    for elem in line:
        print("{0:^3d}".format(elem), end=" ")
print("\n")

#print(A[0][-3:])
# for i in range(size-1):
#     print(A[i][-size+1+i:])
#
# new_A = [A[i][-size+1+i:] for i in range(size-1)]

temp = []
for line in [A[i][-size+1+i:] for i in range(size-1)]:
    temp.extend(filter(lambda x: x > 0, line))

print("Number of positive numbers above main diagonal is", len(temp))