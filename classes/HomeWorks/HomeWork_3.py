from random import sample

# 0
for_reversing = [x for x in sample(range(100), 20)]
print("Origin list: {0}\nReversed list: {1}\n".format(for_reversing, for_reversing[::-1]))

# 1
orig = [x for x in sample(range(100), 20)]
orig_max = max(orig)
print("Max item: {0}, Position: {1}".format(orig_max, orig.index(orig_max)))
print("Origin string: {0}\nWithout max one: {1}\n".format(orig, orig[0:orig.index(orig_max)] + orig[orig.index(orig_max) - 1:]))

#2
hello_string = "Hello!Anthony!Have!A!Good!Day!"
hello_list = hello_string.split('!')[0:-1]
print(hello_list, '\n')

#3
print(*(item + '\n' for item in hello_list), '\n', sep="")

#4
greeting = input("Enter 'Dear Mr./Mrs./Miss/Ms.': ")
if 'Mr.' in greeting: print('Men\n')
elif greeting.split()[1] in ['Mrs.', 'Miss', 'Ms.']: print("Women\n")
else: print("Wrong input")

#5
lines = [input("Enter string: ") for i in range(2)]
print("Second string is the substring of the first one") if lines[1] in lines[0] else print("Second string is'n substring")