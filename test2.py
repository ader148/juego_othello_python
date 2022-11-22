
# 1 va a ser el color negro o la x   //maquina
# -1 va a ser el color blanco o 0    //usuario

#blanco -1  0   USUARIO    
# negro 1   X   MAQUINA     

M1 = [
    [0, 0, 0, 0],
    [0, -1, 1, 0],
    [0, 1, -1, 0],
    [0, 0, 0, 0]
]


MAX = 1  # maximo 1
MIN = -1  # minimo 1

#este metodo es la funcion de utilidad 
# en caso de empate es 1 
# numero de fichas del jugador 1 menos el jugador 2
def optenerPuntajeTablero(M1):
    puntaje = 0
    #recorremos la matriz
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] == MAX:
                print('X',end=" ")
            elif M1[i][j] == MIN:
                print('0', end=" ")
            else:
                print('.', end=" ")
    print("El puntaje del tablero es: %s", puntaje)  
    



def mostrarMatriz(M1):
    matrix_length = len(M1)
    for i in range(matrix_length):
        print(M1[i])
        # if(M1[i] == MIN):
        #    print('X')
        # else:
        #    print('0')


def verTablero(M1):
    print('----------------------')

    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] == MAX:
                print('X',end=" ")
            elif M1[i][j] == MIN:
                print('0', end=" ")
            else:
                print('.', end=" ")
        print('')

    print('----------------------')

def setearJugada(M1, posJugada):
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            contador = contador+1
            if (contador == posJugada):
                #print("se encontro")
                #print(M1[i][j], end=' ')
                #print("Se encontro en fila: %s" %i)
                #print("Se encontro en columna: %s" %j)
                # seteamos la x en la pocicion que se quiere jugar
                M1[i][j] = -1
                # print()


# programa principal
# mostrarMatriz(M1)
print("INICIO DEL JUEGO")
print("Las casillas 6, 7, 10, 11 estan bloqueadas")
verTablero(M1)

#pedimos la posicion de la casilla mientras sea diferente de 6, 7, 10, 11
while True:
    posJugada = int(input('introduce posicion de la casilla a jugar:'))
    if(posJugada not in(6,7,10,11)):
        break
    
setearJugada(M1, posJugada)
verTablero(M1)

#calculamos la jugada de la maquina
 

