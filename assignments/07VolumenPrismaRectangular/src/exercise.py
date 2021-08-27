def area():
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))
    return b * a * p

def main():
    #escribe tu código abajo de esta línea
    print("El volumen del prisma es:",area())

if __name__=='__main__':
    main()
