from string import ascii_letters

string = input("Enter string: ")
words_length = [len(word) for word in string.split()]
shortest_word = string.split()[words_length.index(min(words_length))]
consonants = set(ascii_letters).difference(set('aeiouAEIOU'))
print(shortest_word + '\n', *set(shortest_word).difference(consonants), sep="")