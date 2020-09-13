'''
This program handles exception of writing in a file opened in read mode.
'''
f = open('h.py', 'r')
try:
    f.write(input('Enter a string to write in the file: '))
except IOError as msg:
    print(msg)
