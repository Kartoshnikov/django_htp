def main():
    test_list = [1,3,4,5,78,6,5,4,3,4,5,6,7,8,9,0,9,8,6,5,45,3,3,4,5,6,76,7,8,8,8,9,897,8,7,6,6,5,4,3,4,5,6,7,6]
    print("Original list:", test_list, sep="\n")
    print()

    test_list.sort()
    my_dict = {}
    for pos, i in enumerate(test_list):
        if i in my_dict.keys():
            if i == test_list[pos+1] or i == test_list[pos-1]:
                my_dict[i] += 1
        else:
            my_dict[i] = 1

    temp = [(x, y) for x,y in my_dict.items()]
    temp.sort(key=lambda x: x[1])
    print("The most frequently occurred element in the list - {0}.\n{0} occures in the list {1} times".format(*temp[-1]))

if __name__ == '__main__':
    main()