def my_counter():
    n_string = input("Enter string of numbers without spaces: ")
    if not n_string.isdecimal(): print("Wrong string!"); exit(1)
    num = input("Enter any one digit number: ")
    if not num.isdecimal() or len(num) > 1:
        print("The number you've just entered isn't a one digit number!")
        exit(1)

    def counter():
        amount = n_string.count(num)
        print("The number {0} appears {1} times in the string.".format(num, amount)) if amount \
            else print("Your string doesn't contain number", num)

    return counter()


if __name__ == '__main__':
    my_counter()
