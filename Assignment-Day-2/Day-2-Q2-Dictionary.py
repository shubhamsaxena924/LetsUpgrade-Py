dict1 = {'FirstName': 'Shubham', 'LastName': 'Saxena', 'Age': '18'}
dict1['College'] = 'GLA'
print('Dict1 :', dict1)

# returns list of tuples of key-value pair
print('Items in the dictionary: ', dict1.items())

# returns the value of the key specified, if key is not present, default_value is printed
print('First Name: ', dict1.get('FirstName', 'NoName'))

dict2 = dict([('College', 'Amity'), ('Section', 'R'), ('Branch', 'CS-CCV')])
print('Dict2:', dict2)

# adds the key-value pair present in dict2 but not in dict1
dict1.update(dict2)
print('After updating, dict1:', dict1)

# empties the particular dictionary
dict2.clear()
print('After clear(), dict2:', dict2)
dict2['College'] = 'Amity'

# copies elements of dict1 to dict2
dict2 = dict1.copy()
print('After copying, dict1 to dict2, dict2: ', dict2)
