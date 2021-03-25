import random
import time

class Carta:
    def __init__(self, numero, mazo):
        self.numero = numero
        self.mazo = mazo
        
class Jugador:
    def __init__(self, numero, puntaje):
        self.numero = numero
        self.puntaje = puntaje


print("Bienvenido al juego de Memorice!")
print("")
num_cartas = int(input("Por favor, ingrese el numero de cartas a jugar:\n"))
print("")

# Creamos a ambos jugadores

jugador_1 = Jugador(1, 0)
jugador_2 = Jugador(2, 0)
jugadores = []
jugadores.append(jugador_1)
jugadores.append(jugador_2)

numero_carta = 1
mazo_1 = []
mazo_2 = []

# Creo dos mazos con la cantidad de cartas
# que quieran los jugadores
while (numero_carta <= num_cartas):
    carta_mazo_1 = Carta(numero_carta, 1)
    carta_mazo_2 = Carta(numero_carta, 2)
    mazo_1.append(carta_mazo_1)
    mazo_2.append(carta_mazo_2)
    numero_carta += 1

a = num_cartas
mazo_1v2 = mazo_1
mazo_2v2 = mazo_2

# Creo dos nuevos mazos, pero esta vez con
# las cartas en orden aleatorio
mazo_azar = []


while (a > 0):
    carta_azar = random.randint(1, a) - 1
    mazo_azar.append(mazo_1v2[carta_azar])
    mazo_1v2.pop(carta_azar)
    a -= 1

a = num_cartas
while (a > 0):
    carta_azar = random.randint(1, a) - 1
    mazo_azar.append(mazo_2v2[carta_azar])
    mazo_2v2.pop(carta_azar)
    a -= 1

a = num_cartas
lista_juego = []
while (a > 0):
    lista = ["*", "*"]
    lista_juego.append(lista)
    a -= 1

# Creo una lista con dos listas:
# las dos columnas del juego
mazo_azarv2 = []
a = 0
while (a < num_cartas):
    fila = []
    num = a * 2
    fila.append(mazo_azar[num])
    fila.append(mazo_azar[num + 1])
    mazo_azarv2.append(fila)
    a += 1

for fila in mazo_azarv2:
    print(str(fila[0].numero) + "        " + str(fila[1].numero))

print("")
print("")
print("")






# Empezamos el juego:
print("")
print("Que comience el juego!")
print("")

game_active = True
num_turno = 1
num_jugador = 1
while (game_active == True):
    if (num_turno % 2 == 1):
        num_jugador = 1
        jugador = jugadores[0]
    else:
        num_jugador = 2
        jugador = jugadores[1]
    
    for fila in mazo_azarv2:
        print(str(fila[0].numero) + "        " + str(fila[1].numero))
    
    lista_juego_temp = []
    for l in lista_juego:
        lista_juego_temp.append(l[:])
    
    print("")
    print("")
    print("")
    print("Jugador " + str(num_jugador) + ", es su turno")
    print("")
    print("    0" + "        " + "1")
    
    b = 0
    while (b < num_cartas):
        print(str(b) + "   " + str(lista_juego_temp[b][0]) + "        " + str(lista_juego_temp[b][1]))
        b += 1

    print("Primera carta:")
    print("")
    num_col_1 = int(input("Elija una columna:\n"))
    #En caso de que elija un numero de columna invalido
    while (num_col_1 > 1):
        print("Coordenada invalida")
        print("")
        num_col_1 = int(input("Elija una columna:\n"))
    
    num_fila_1 = int(input("Elija una fila:\n"))
    #En caso de que elija un numero de fila invalido
    while (num_fila_1 >= num_cartas):
        print("Coordenada invalida")
        print("")
        num_fila_1 = int(input("Elija una fila:\n"))
    
    print("")
    print("")
    
    num_elegido_1 = mazo_azarv2[num_fila_1][num_col_1].numero
    
    lista_juego_temp[num_fila_1].pop(num_col_1)
    lista_juego_temp[num_fila_1].insert(num_col_1, num_elegido_1)
    
    b = 0
    print("    0" + "        " + "1")
    while (b < num_cartas):
        print(str(b) + "   " + str(lista_juego_temp[b][0]) + "        " + str(lista_juego_temp[b][1]))
        b += 1
    
    time.sleep(2)
    
    print("")
    print("")
    print("Segunda carta:")
    print("")
    
    num_col_2 = int(input("Elija una columna:\n"))
    #En caso de que elija un numero de columna invalido
    while (num_col_2 > 1):
        print("Coordenada invalida")
        print("")
        num_col_2 = int(input("Elija una columna:\n"))
    
    num_fila_2 = int(input("Elija una fila:\n"))
    #En caso de que elija un numero de fila invalido
    while (num_fila_2 >= num_cartas):
        print("Coordenada invalida")
        print("")
        num_fila_2 = int(input("Elija una fila:\n"))
    print("")
    
    #En caso de que se repitan las coordenadas de ambas cartas
    while (num_col_1 == num_col_2 and num_fila_1 == num_fila_2):
        print("Coordenadas invalidas. Deben ser distintas a la de la primera carta")
        print("")
        print("Segunda carta:")
        print("")
        num_col_2 = int(input("Elija una columna:\n"))
        num_fila_2 = int(input("Elija una fila:\n"))
        print("")
        
    num_elegido_2 = mazo_azarv2[num_fila_2][num_col_2].numero
    
    lista_juego_temp[num_fila_2].pop(num_col_2)
    lista_juego_temp[num_fila_2].insert(num_col_2, num_elegido_2)
    
    print("    0" + "        " + "1")
    b = 0
    while (b < num_cartas):
        print(str(b) + "   " + str(lista_juego_temp[b][0]) + "        " + str(lista_juego_temp[b][1]))
        b += 1
    
    if (num_elegido_1 == num_elegido_2):
        print("")
        print("Correcto!")
        jugador.puntaje += 1
        lista_juego[num_fila_1].pop(num_col_1)
        lista_juego[num_fila_1].insert(num_col_1, " ")
        lista_juego[num_fila_2].pop(num_col_2)
        lista_juego[num_fila_2].insert(num_col_2, " ")
    else:
        print("")
        print("Incorrecto!")
          
    time.sleep(2)
    
    ast_count = 0
    for l in lista_juego:
        for i in l:
            if (i == "*"):
                ast_count += 1
    
    if (ast_count == 0):
        print("")
        print("El juego se ha acabado!")
        game_active = False
    
    num_turno += 1
    
    print("")
    print("El puntaje del jugador 1 es", jugadores[0].puntaje)
    print("El puntaje del jugador 1 es", jugadores[0].puntaje)
    print("")
    
    print("")
    print("")
    print("")
    
print("")
print("El puntaje final del jugador 1 es", jugadores[0].puntaje)
print("El puntaje final del jugador 2 es", jugadores[1].puntaje)
print("")

if (jugadores[0].puntaje > jugadores[1].puntaje):
    print("Ha ganado el jugador 1!") 
elif (jugadores[1].puntaje > jugadores[0].puntaje):
    print("Ha ganado el jugador 2!")
else:
    print("Empate!")
    
    
    