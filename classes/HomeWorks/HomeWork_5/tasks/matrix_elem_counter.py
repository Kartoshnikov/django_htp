from random import sample

def input_data():
    initial_data = input("Enter two numbers (p1 p2) with space and p1 < p2: ")
    try:
        p1, p2 = (int(x) for x in initial_data.split())
        if p1 > p2: print("p1 > p2"); raise Exception
        return p1, p2
    except:
        print("Wrong data!")
        exit(1)


def print_matrix(matrix):
    print("Initial maxtix: ")
    for line in matrix:
        print()
        for elem in line:
            print("{0:>2d}".format(elem), end=" ")
    print("\n")

def main():
    A = [[x for x in sample(range(99), 3)] for i in range(4)]
    count = 0
    p1, p2 = input_data()
    for i in A:
        for j in i:
            if p1 < j < p2: count += 1
    print_matrix(A)
    print("Count of numbers that satisfy the requirements: ", count)

if __name__ == '__main__':
    main()

