import tasks.arithmetical_mean_matrix as arithmetical_mean
import tasks.elem_counter as elem_counter
import tasks.matrix_elem_counter as matrix_elem_counter
import tasks.pupils_database as pupils_database
import tasks.square_matrix as square_matrix


switch = {
    'arif mean': arithmetical_mean.main,
    'elem counter': elem_counter.main,
    'elem counter 2': matrix_elem_counter.main,
    'pupils database': pupils_database,
    'square matrix': square_matrix.main,
    'exit': exit
}

while True:
    print()
    [print("{}) {}".format(i+1, elem)) for i, elem in enumerate(switch.keys())]
    choice = input("Choose task (full or number): ")
    if choice.isdigit():
        try:
            list(switch.values())[int(choice)-1]()
        except IndexError:
            print("Wrong number!")
    elif choice.isprintable():
        switch.get(choice, lambda: print("Wrong test"))()