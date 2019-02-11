from random import sample

def input_data():
    try:
        return int(input('Enter size of matrix (N): '))
    except:
        print("Wrong N!"); exit(1)


def print_matrix(matrix):
    print("Initial maxtix: ")
    for line in matrix:
        print()
        for elem in line:
            print("{0:>2d}".format(elem), end=" ")
    print("\n")

def main():
    size = input_data()
    A = [[x for x in sample(range(-size, size+1), size)] for i in range(size)]
    print_matrix(A)
    temp = []
    for line in [A[i][-size+1+i:] for i in range(size-1)]:
        temp.extend([x for x in line if x >= 0])

    print("Number of positive numbers above main diagonal is", len(temp), temp)

if __name__ == '__main__':
    main()