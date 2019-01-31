orig = [1, 3, -5, 7, -3, 4, 0, 4, -3, 6, 0, -8, 9]
new_list = [x for x in orig if x < 0] + [x for x in orig if x == 0] + [x for x in orig if x > 0]

print(orig, new_list, sep='\n')