def main():
    x = 4
    y = 2
    print(multiplication(x,y))
    print("\n")
    print(recMult(x,y))
    



def multiplication(x, y):
    count = 0
    num = 0
    while count < y:
        num = num + x
        count += 1
    return num

def recMult(x , y):
    if x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return x + recMult(x, y - 1)
    


main()