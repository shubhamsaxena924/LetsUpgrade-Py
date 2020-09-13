# Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print
# “it’s a Match” if no then print “it’s Gone” in function.
# Example -
# Listy =[1,5,6,4,1,2,3,5] - it’s a Match
# Listy = [1,5,6,5,1,2,3.6] - it’s Gone

def check(mainList):
    subList = [1, 1, 5]
    c = 0
    for i in subList:
        if i in mainList[c:]:
            c = mainList.index(i, c)+1
        else:
            return False
    return True


listy = [1, 4, 6, 4, 4, 2, 3, 5, 1, 5]
c = check(listy)
if c == True:
    print("It's a match")
else:
    print("it's Gone")
