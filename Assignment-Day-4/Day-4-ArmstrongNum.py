# Print the first ArmStrong number in the range of
# 1042000 to 702648265 and
# exit the loop as soon as you encounter the first armstrong number.
i = 1042000
j = 702648265
while(i <= j):
    sum = 0
    n = i
    count = 0
    while(n > 0):
        n = n//10
        count = count+1
    n = i
    while(n != 0):
        dig = n % 10
        n = n//10
        sum = sum+dig**count
    if(sum == i):
        print('The first Armstrong Number is', i)
        break
    i = i+1
