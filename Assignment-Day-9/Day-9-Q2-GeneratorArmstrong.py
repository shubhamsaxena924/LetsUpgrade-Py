# Make a small generator function for returning armstrong
# numbers in between 1-1000 in a generator object

rangeList = list(range(1, 1001))


def generateArmstrong(lst):
    for i in lst:
        sum = 0
        j = i
        count = 0
        while(j > 0):
            j = j//10
            count += 1
        j = i
        while(j > 0):
            digit = j % 10
            j = j//10
            sum = sum+(digit**count)
        if sum == i:
            yield i


generateObj = generateArmstrong(rangeList)
print(list(generateObj))
