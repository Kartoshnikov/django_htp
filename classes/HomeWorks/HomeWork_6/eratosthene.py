from math import gcd
def init_data():
    num = int(input("Enter number: "))
    return num

def erastofen(num):
    num_list = [x for x in range(2, num)]
    for count, i in enumerate(num_list):
        if i**2 > num:
            break
        for j in num_list[count+1:]:
            if not j % i:
                num_list.remove(j)
    return num_list

if __name__ == '__main__':
    print(erastofen(init_data()))

