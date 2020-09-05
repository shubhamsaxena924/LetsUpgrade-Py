# List and its default function

mylist = ['Hello', 1, 2]
print('My list: ', mylist)

print('Length of my list: ', len(mylist))   # Length of the list

mylist.append(3)                            # Append the element at the last
print('My list: ', mylist)

mylist.insert(2, 'Bye')                     # inserts the elem. at speci. index
print('My list: ', mylist)

mylist2 = [5, 6, 7, 8]
print('My list 2: ', mylist2)

mylist.extend(mylist2)                      # adds contents of list 2 to list 1
print('My list: ', mylist)

# counts of the spec. element in the list
print('Count: ', mylist.count(5))

# prints index of the specified element
print('Index of 3:', mylist.index(3))

# returns the elem. spec. index, and also deletes the element from the list (default- last element)
print('Pop:', mylist.pop(), '\nList after popping: ', mylist)

# returns the element spec. and also deletes the element from the list
print('Remove:', mylist.pop(3), '\nList after removing: ', mylist)
