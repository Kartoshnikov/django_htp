from random import sample

initial_data = input("Enter matrix parameters (M N) without spaces: ")
try:
    M, N = (int(x) for x in initial_data.split())
except:
    print("Wrong initial parameters!")
    exit(1)




A = [[x for x in sample(range(99), M)] for i in range(N)]
print("Initial maxtix: ")

for line in A:
    print()
    for elem in line:
        print("{0:>2d}".format(elem), end=" ")

print("\n")
print("Arifmetical mean: ", sum(sum(line) for line in A)/(M*N))
