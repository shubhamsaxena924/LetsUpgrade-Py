# Print all prime numbers between 1 and 200
for i in range(2, 201):
    for j in range(2, int(i**(1/2))+1):
        if(i % j == 0):
            break
    else:
        print(i, end=',')
print('...')
