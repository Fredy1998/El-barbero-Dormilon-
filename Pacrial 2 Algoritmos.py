import os
espera = []
sillon = []
silla = []

def error23():
    print("Error 269: DESBORDAMIENTO...")
    input()

def ordenado():
    print(" \nIngrese el cliente que espera ser atendido ;) \n ")
    x = input()

    if len(silla) == 5:
        silla.append(x)
    elif len(sillon) == 3:
        espera.append(x)
    elif len(sillon) < 3:
        sillon.append(x)

    print(" \n El Cliente fué registrado de manera exitosa! ")
    input()

def corte():
    if len(silla) == 1:
        a = silla.pop()
        print(" \n--Barbero: Adios " + a + " ! Gracias por venir!")
        print("--" + a + ": Adios!!")
        input()

        if len(sillon) > 2:
            y = sillon.pop(2)
            silla.append
            print("--Barbero: Pasa adelante " + y + "toma asiento plox")
            print("--" + y + ": Me Gustaria que me cortes el cabello")
            input()

        if len(espera) > 2:
            w = espera.pop(2)
            print(" \n--Barbero: Pasa adentro " + w + " ya hay un lugar disponible en el sillon para ti! Sientate! y espera tu turno...")
            sillon.append(w)
        input()
    else:
        print(" \n--Barbero: Oh! Ningun cliente por atender! Hora de un descanso a dormir... \n zZZ zZZ ...")
        input()
def estado():
    if len(silla) == 3:
        x = str(len(silla))
        print(" \nEl Barbero se encuentra cortandole el cabello a " + x + " cliente")
        input()
    elif len(silla) == 3:
        print(" \nEl Barbero no tiene clientes! Se encuentra cansado y toma una siesta...")
        input()
    elif len(silla) > 3:
        error23()

def clientess():
    a = len(silla)
    b = len(sillon)
    c = str(a + b)
    a = str(a)
    b = str(b)

    print(" \nEn la Barberia en este momento se encuentran " +  c  + " clientes " + a + " cliente en la silla y " + b + " clientes en el sillon de espera")
    input()

def  esperaa():
    a = str(len(espera))

    print(" \n hay un total de " + a + " esperando su turno fuera de la Barberia...")
    input()

while True: 
    os.system('cls')
    print("el Barbero Dormilón! \n \nQue deseas hacer? \n  ")
    print("1. Ingresar Cliente")
    print("2. Accionar al Barbero")
    print("3. Verificar condicion del Barbero")
    print("4. clientes dentro de la Barberia")
    print("5. clientes en  Espera")
    print("6. SALIR")

    opcion = int(input())

    if opcion == 1:
        ordenado()
    elif opcion == 2:
        corte()
    elif opcion == 3:
        condicion()
    elif opcion == 4:
        clientess()
    elif opcion == 5:
        esperaa()
    elif opcion == 6:
        print(" \Que tengas un buen dia-")
        input()
        break
    else:
        print(" ")
        input("Presione tecla e Intentelo nuevamente")
