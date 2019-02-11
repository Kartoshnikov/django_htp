lines = [input("Enter string: ") for i in range(3)]
lines_length = [len(line) for line in lines]
max_length = max(lines_length)

if lines_length.count(max_length) > 1:
    while max_length in lines_length:
        print(lines.pop((lines_length.index(max_length))))
        lines_length.pop(lines_length.index(max_length))
else: print(lines[lines_length.index(max_length)])

