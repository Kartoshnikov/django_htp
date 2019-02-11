orig = [1, 3, -5, 7, -3, 4, 0, 4, -3, 6, 0, -8, 9]
print(orig)

negat_elem = []
for i, elem in enumerate(orig):
    if elem < 0:
        negat_elem.append(orig.pop(i))

new_list = negat_elem + orig
print(new_list, sep='\n')
