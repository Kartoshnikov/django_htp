def init_data():
    data = input("Enter string: ")
    sep = input("Enter separator: ") or ' '
    return [data, sep]

def separate(string, separator):
    return set([str(string.count(word)) + word
            for word in [x for x in string.split(separator) if x]])

def main():
    for item in separate(*init_data()):
        print(item)

if __name__ == '__main__':
    main()