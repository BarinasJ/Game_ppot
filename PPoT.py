import random
aleatorio = random.randrange(0, 3)
elijePc = ""
c=5
puntos_jugador=0
puntos_pc=0
while (c>0):
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    opcion = int(input("Que elijes: "))

    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Tu elijes: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1:
        elijePc = "papel"
    elif aleatorio == 2:
        elijePc = "tijera"
    print("PC elijio: ", elijePc)
    print("...")
    if elijePc == "piedra" and elijeUsuario == "papel":
        c=c-1
        puntos_jugador=puntos_jugador+1
        print("Ganaste, papel envulve piedra")
    elif elijePc == "papel" and elijeUsuario == "tijera":
        c=c-1
        puntos_jugador=puntos_jugador+1
        print("Ganaste, Tijera corta papel")
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        c=c-1
        puntos_jugador=puntos_jugador+1
        print("Ganaste, Piedra pisa tijera")
    if elijePc == "papel" and elijeUsuario == "piedra":
        puntos_pc=puntos_pc+1
        c=c-1
        print("perdiste, papel envulve piedra")
    elif elijePc == "tijera" and elijeUsuario == "papel":
        puntos_pc=puntos_pc+1
        c=c-1
        print("perdiste, Tijera corta papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        puntos_pc=puntos_pc+1
        c=c-1
        print("perdiste, Piedra pisa tijera")
    elif elijePc == elijeUsuario:
        c=c-1
        print("empate")

# print("Tus puntos: " + puntos_jugador + "vs puntos del cpu" + puntos_pc)

if(puntos_jugador>puntos_pc):
    print("Felicidades... Venciste la cpu")
elif(puntos_pc>puntos_jugador):
    print("Buen intento... Pero la cpu ganó")
else:
    print("Empate")

print("tus puntos",puntos_jugador)

    # if(puntos_jugador>puntos_pc):
    #     print("Tus puntos:{} vs puntos del cpu:{}".format(puntos_jugador,puntos_pc) "Felicidades... Ganaste")
    # else:
    #     print("Tus puntos:{}  vs puntos del cpu:{}".format(puntos_jugador,puntos_pc) "Buen intento... Pero la cpu ganó")