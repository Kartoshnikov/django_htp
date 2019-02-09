from functools import reduce

with open('test.txt', 'r') as text:
    print(text)
    lines = text.readlines()
    report = [{'words_n': len(line.rstrip().split()), 'symb_n': len(line)}for line in lines]

    print('Number of lines:', len(lines))
    for i, line in enumerate(report):
        print('line{:3}: words -{elem[words_n]:>4}, symbols -{elem[symb_n]:>4}'.format(i+1, elem=line))