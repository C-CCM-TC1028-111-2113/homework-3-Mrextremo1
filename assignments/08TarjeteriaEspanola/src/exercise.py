def tarjetones(pa,pl):
    return min(pa*12,pl*35)
    
def main():
    #escribe tu código abajo de esta línea
    pa = int(input("Dame la cantidad de pliegos de papel albanene: "))
    pl = int(input("ame la cantidad de plumones: "))
    print("El número máximo de tarjetas que se pueden hacer es:",tarjetones(pa,pl))
    

if __name__=='__main__':
    main()
