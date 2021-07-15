def main():
    x = 105
    y = 278
    print(multiplication(x,y))
    # print(power(x,y))
    print(recMult(x,y))
    fourVarPairs(10)


def multiplication(x, y):
    count = 0
    num = 0
    while count < y:
        num = num + x
        count += 1
    return num

def power(x , y):
    if y < 0:
        return 0 #error
    elif y == 1:
        return y
    else:
        return x * power(x, y - 1)

def recMult(x, y):
    if y < 0:
        return 0 #error
    elif y == 1:
        return x
    else:
        return x + recMult(x, y - 1)

def fourVarPairs(x):
    n = x
    a = 0
    b = 0
    c = 0
    d = 0
    while a < n:
        while b < n:
            while c < n:
                while d < n:
                    if a**2 + b == c**2 + d:
                        print(a,b,c,d) 
                    d += 1 
                c += 1
                d = 0 
            b += 1
            c = 0
            d = 0 
        a += 1
        b = 0 
        c = 0
        d = 0
    


main()