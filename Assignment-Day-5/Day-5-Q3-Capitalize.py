# Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions
lst = ['hey this is sai', 'I am in mumbai']
lst2 = list(map(lambda string: string.title(), lst))
print(lst2)
