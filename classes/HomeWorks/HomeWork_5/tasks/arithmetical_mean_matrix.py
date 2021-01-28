from random import sample

def input_data():
    initial_data = input("Enter matrix parameters (M N) without spaces: ")
    try:
        return (int(x) for x in initial_data.split())
    except:
        print("Wrong initial parameters!")
        exit(1)

def print_matrix(matrix):
    print("Initial maxtix: ")
    for line in matrix:
        print()
        for elem in line:
            print("{0:>2d}".format(elem), end=" ")
    print("\n")

def main():
    M, N = input_data()
    A = [[x for x in sample(range(99), M)] for i in range(N)]
    print_matrix(A)
    print("Arifmetical mean: ", sum(sum(line) for line in A)/(M*N))



if __name__ == '__main__':
    main()
