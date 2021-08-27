def bisiesto(b):
    if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
        return True
    else:
        return False

def main():
    #escribe tu código abajo de esta línea
    bis = int(input())
    print(bisiesto(bis))


if __name__=='__main__':
    main()
