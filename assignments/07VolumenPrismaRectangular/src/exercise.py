def area(b,a,p):
    return b * a * p

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))
    print("El volumen del prisma es:",area(b,a,p))

if __name__=='__main__':
    main()
