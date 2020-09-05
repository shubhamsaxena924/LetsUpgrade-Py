str1 = 'Shubham Saxena'

print(str1.lower())  # lowers all alphabets
print(str1.upper())  # Block letters
print(str1.title())  # First letter capital of each word

print(str1.replace('a', 'w'))  # Replace occurence of 'a with 'w'

print(str1.find('z'))  # Find the index of 'z', if not present--> returns -1

print(str1.index('h'))  # finds the index of 'h', if not present--> error

print(str1.count('h'))  # count the occurences of 'h'

print(str1.split())  # returns the list containing each word of the string

print(str1.swapcase())  # swaps the cases
