# blanco -1   0   Maquina    
# negro   1   X   Usuario     

M1 = [
    [0, 0, 0, 0],
    [0, -1, 1, 0],
    [0, 1, -1, 0],
    [0, 0, 0, 0]
]


JuegaMaquina = False

MAX = 1  # maximo 1
MIN = -1  # minimo -1


#este metodo es la funcion de utilidad 
# en caso de empate es 1 
# numero de fichas del jugador 1 menos el jugador 2
def optenerPuntajeTablero(M1):
    puntaje = 0
    #recorremos la matriz
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] == MAX:
                puntaje = puntaje + 1
            elif M1[i][j] == MIN:
                puntaje = puntaje - 1
    
    if(puntaje < 0):
        return -1
    
    return puntaje
    

def verTablero(M1):
    #print(M1)
    print('----------------------')

    #for i in range(len(M1)):
    for i in M1:
        for j in range(0,len(i)):
            #if M1[i][j] == MAX:  #max es 1
            if i[j] == MAX:  #max es 1
                print('X',end=" ")
            if i[j] == MIN:  #min es -1
                print('0', end=" ")
            if (i[j] == 0):
                print('.', end=" ")
                #print('entra en el punto')
        print('')

    print('----------------------')

def setearJugada(M1, posJugada):
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            contador = contador+1
            if (contador == posJugada):
                M1[i][j] = 1
                

def getFila(M1,posJugada):
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            contador = contador+1
            if (contador == posJugada):
               return i

def getColumna(M1,posJugada):
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            contador = contador+1
            if (contador == posJugada):
               return j

def CoincidenciaFila(M1,numFila):
    #fila i
    #columna j
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if(numFila == i):
                #contador = contador+1
                if(JuegaMaquina):
                    #buscamos 1
                    if(M1[i][j] == -1):
                        contador = contador + 1
                else:
                    if (M1[i][j] == 1):
                        contador = contador + 1

    return contador-1


def CoincidenciaColumna(M1,numColumna):
    #fila i
    #columna j
    contador = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if(numColumna == j):
                #contador = contador+1
                if(JuegaMaquina):
                    #buscamos 1
                    if(M1[i][j] == -1):
                        contador = contador + 1
                else:
                    if (M1[i][j] == 1):
                        contador = contador + 1

    return contador-1


def actualizarFila(M1,numFila):
    #fila i
    #columna j
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if(numFila == i):
                #contador = contador+1
                if(JuegaMaquina):
                    #buscamos 1
                    if( (j+1) < 4):
                        if(M1[i][j] == -1 and M1[i][j+1] == 1 ):
                            #actualizamos el elemento siguiente
                            M1[i][j+1] = -1
                else:
                    if( (j+1) < 4): #verificamos que no sea mayor para que no se pase el indice
                        if (M1[i][j] == 1 and M1[i][j+1] == -1):
                            M1[i][j+1] = 1

def actualizarColumna(M1,numColumna):
    #fila i
    #columna j
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if(numColumna == j):
                #contador = contador+1
                if(JuegaMaquina):
                    #buscamos 1
                    if( (i+1) < 4):
                        if(M1[i][j] == -1 and M1[i+1][j] == 1 ):
                            #actualizamos el elemento siguiente
                            M1[i+1][j] = -1
                else:
                    if( (i+1) < 4): #verificamos que no sea mayor para que no se pase el indice
                        if (M1[i][j] == 1 and M1[i+1][j] == -1):
                            M1[i+1][j] = 1

 
def actulizarTablero(tableroAct,posJugada):
    FilaElemento = getFila(tableroAct,posJugada)
    #print("esta es la fila del elemento")
    #print(FilaElemento)
    ColumnaElemento = getColumna(tableroAct,posJugada)
    #print("esta es la columna del elemento")
    #print(ColumnaElemento)    

    #buscar coincidencia en fila
    varCoincidenciaFila = CoincidenciaFila(tableroAct,FilaElemento)
    #print("esta es la coincidencia en fila")
    #print(varCoincidenciaFila)
    
    #buscar coincidencia en columna
    varCoincidenciaColumna = CoincidenciaColumna(tableroAct,ColumnaElemento)
    #print("esta es la coincidencia en columna")
    #print(varCoincidenciaColumna)

    if(varCoincidenciaFila + varCoincidenciaColumna >= 1):
        if(varCoincidenciaFila >= 1):
            #llamamos actualizar fila
            actualizarFila(tableroAct,FilaElemento)
        if(varCoincidenciaColumna >= 1):
            #llamamos actualizar columna
            actualizarColumna(tableroAct,ColumnaElemento)

    #print("la nueva matriz queda")
    #verTablero(M1)

def miniMax(M1,jugador):
    print("esto llego a mimax")
    verTablero(M1)
    #print(M1)
    global jugada_maquina
    #i fila
    #j columna
    contador = 0  
    movimientos =[]
    nivelArbol = 0

    if(nivelArbol < 3):
        for i in range(len(M1)):
            for j in range(len(M1[i])):
                nivelArbol = nivelArbol +1
                contador = contador+1
                if M1[i][j] == 0:
                    tableroaux = M1[:]
                    #seteamos la jugada
                    setearJugada(tableroaux,contador) #tableroaux[jugada] = jugador
                    actulizarTablero(tableroaux, contador)
                    #print("este es el tablero actualizado")
                    #verTablero(tableroaux)
                    puntuacion= miniMax(tableroaux, jugador*(-1))
                    movimientos.append([puntuacion, M1[i][j] ]) #revizar esta parte // movimientos.append([puntuacion, jugada])
                    #print(movimientos)
                    
                    
        if jugador == MAX:    
            movimiento = max(movimientos)    
            jugada_maquina = movimiento[1]
            return movimiento
        else:
            movimiento = min(movimientos)
            return movimiento[0]


def juega_maquina(tablero):
    global jugada_maquina  
    punt = miniMax(tablero[:], MAX)
    tablero[jugada_maquina] = MAX
    return tablero


# programa principal
# mostrarMatriz(M1)
print("INICIO DEL JUEGO")
print("Las casillas 6, 7, 10, 11 estan bloqueadas")
verTablero(M1)

#optenemos el punaje del tablero inicial
#puntajeTablero = optenerPuntajeTablero(M1)
#print("El puntaje del tablero es: ")
#print(puntajeTablero)  

#pedimos la posicion de la casilla mientras sea diferente de 6, 7, 10, 11
while True:
    posJugada = int(input('introduce posicion de la casilla a jugar:'))
    if(posJugada not in(6,7,10,11)):
        break
    
setearJugada(M1, posJugada)
verTablero(M1)
actulizarTablero(M1, posJugada)
verTablero(M1)

#puntajeTablero = optenerPuntajeTablero(M1)
#print("El puntaje del tablero es: ")
#print(puntajeTablero)  


#tableroDeMaquina = juegaMaquina(M1)

#calculamos la jugada de la maquina
tableroMaquina = juega_maquina(M1)
#print(tableroMaquina)

 

