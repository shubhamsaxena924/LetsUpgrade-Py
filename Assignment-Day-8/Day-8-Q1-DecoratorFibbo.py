# Write a decorator function for your taking input
# for you any kind of function you want to build,
# For example- You make a fibonacci series function, in which
# your input range is defined by the decorator program input

def returnFibbo(funct):
    def fibbo():
        n = funct()
        a, b = 0, 1
        for i in range(0, n):
            if i <= 1:
                print(i)
                continue
            c = a+b
            print(c)
            a = b
            b = c
    return fibbo


@returnFibbo
def takeInput():
    s = int(input('Enter a number: '))
    return s


takeInput()
