def main():
    x = 105
    y = 278
    print(multiplication(x,y))
    # print(power(x,y))
    print(recMult(x,y))



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
    


main()