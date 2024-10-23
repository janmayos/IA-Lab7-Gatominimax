
import random
import time
# Profundidad máxima para limitar el tiempo de búsqueda
PROFUNDIDAD_MAXIMA = 6


def crear_tablero():
    tablero = [[" ", " ", " ", " "],
               [" ", " ", " ", " "],
               [" ", " ", " ", " "],
               [" ", " ", " ", " "]]
    print_tablero(tablero)
    return tablero


def print_tablero(tablero):
    matrix_length = len(tablero)
    for i in range(matrix_length):
        print(tablero[i])


def solicitar_coordenadas():
    while True:
        fila = int(input("Ingresa la fila:"))
        if fila >= 1 and fila <= 4:
            break
        else:
            print("Favor de ingresar un valor del 1-4")

    while True:
        columna = int(input("Ingresa la columna:"))
        if columna >= 1 and columna <= 4:
            break
        else:
            print("Favor de ingresar un valor del 1-4")

    return fila-1, columna-1


def rellenar_casilla(tablero, fila, columna, valor):
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = valor
        print_tablero(tablero)
    else:
        print("Casilla ocupada volver a seleccionar coordenadas")
        fila, columna = solicitar_coordenadas()
        rellenar_casilla(tablero, fila, columna, valor)


def eval_columnas(tablero, valor, matrix_length, matrix_length_column):
    ban = False
    for columna in range(matrix_length):
        for fila in range(matrix_length_column):
            if tablero[fila][columna] == " " or tablero[fila][columna] != valor:
                ban = False
                break
            else:
                ban = True
        if ban:
            break
    return ban


def eval_filas(tablero, valor, matrix_length, matrix_length_column):
    ban = False
    for fila in range(matrix_length):
        for columna in range(matrix_length_column):
            if tablero[fila][columna] == " " or tablero[fila][columna] != valor:
                ban = False
                break
            else:
                ban = True
        if ban:
            break
    return ban


def eval_diagonal(tablero, valor):
    ban = False
    if tablero[0][0] == valor and tablero[1][1] == valor and tablero[2][2] == valor and tablero[3][3] == valor:
        ban = True
    if tablero[0][3] == valor and tablero[1][2] == valor and tablero[2][1] == valor and tablero[3][0] == valor:
        ban = True

    return ban


def eval_tablero(tablero):
    matrix_length = len(tablero)
    matrix_length_column = len(tablero[0])
    if eval_columnas(tablero, "X", matrix_length, matrix_length_column):
        return "X gano en columna"
    if (eval_columnas(tablero, "O", matrix_length, matrix_length_column)):
        return "O gano en columna"
    if eval_filas(tablero, "X", matrix_length, matrix_length_column):
        return "X gano en fila"
    if (eval_filas(tablero, "O", matrix_length, matrix_length_column)):
        return "O gano en fila"
    if eval_diagonal(tablero, "X"):
        return "X gano en diagonal"
    if (eval_diagonal(tablero, "O")):
        return "O gano en diagonal"

    return " "


def esta_lleno(tablero):
    matrix_length = len(tablero)
    matrix_length_column = len(tablero[0])
    for fila in range(matrix_length):
        for columna in range(matrix_length_column):
            if tablero[fila][columna] == " ":
                return False
    return True


def es_ganador(tablero):

    mensaje = eval_tablero(tablero)
    if esta_lleno(tablero):
        print("Es un empate")
    else:
        if mensaje == " ":
            return False
        else:
            print("El jugador " + mensaje)
    return True


def generar_aleatorios_rellenar(tablero, valor):
    while True:
        fila = random.randint(0, 3)
        columna = random.randint(0, 3)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = valor
            print(fila, columna)
            break
    print_tablero(tablero)


def iniciar_juego_gato():
    tablero = crear_tablero()
    while (True):
        print("Turno de X")
        fila, columna = solicitar_coordenadas()
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "X")
        if es_ganador(tablero):
            break
        # fila,columna = solicitar_coordenadas()
        # rellenar_casilla(tablero,fila,columna,"O")
        generar_aleatorios_rellenar(tablero, "0")
        if es_ganador(tablero):
            break


def iniciar_juego_gato_2_jugadores():
    tablero = crear_tablero()
    while (True):
        fila, columna = solicitar_coordenadas()
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "X")
        if es_ganador(tablero):
            break
        # fila,columna = solicitar_coordenadas()
        # rellenar_casilla(tablero,fila,columna,"O")

        print("Turno de O")
        fila, columna = solicitar_coordenadas()
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "O")
        if es_ganador(tablero):
            break


def heuristica(tablero):
    """Evalúa el tablero para asignar un puntaje."""
    if eval_tablero(tablero)[0] == "O":
        return 10  # Gana la computadora
    elif eval_tablero(tablero)[0] == "X":
        return -10  # Gana el jugador
    return 0  # Empate o tablero sin ganador


def mejor_movimiento(tablero, simbolo, es_maximizando):
    mejor_puntaje = -float('inf')
    movimiento = None
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == " ":
                tablero[i][j] = simbolo
                puntaje = minimax_alpha_beta(
                    tablero, 0, es_maximizando, -float('inf'), float('inf'))
                tablero[i][j] = " "
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    movimiento = (i, j)
    return movimiento


def minimax_alpha_beta(tablero, profundidad, es_maximizando, alpha, beta):
    # print_tablero(tablero)
    ganador = eval_tablero(tablero)
    if ganador == None or esta_lleno(tablero) or profundidad == PROFUNDIDAD_MAXIMA:
        return heuristica(tablero)

    if es_maximizando:
        max_eval = -float('inf')
        for i in range(4):
            for j in range(4):
                if tablero[i][j] == " ":
                    tablero[i][j] = "O"
                    eval_alpha_beta = minimax_alpha_beta(
                        tablero, profundidad + 1, False, alpha, beta)
                    tablero[i][j] = " "
                    max_eval = max(max_eval, eval_alpha_beta)
                    alpha = max(alpha, eval_alpha_beta)
                    if beta <= alpha:
                        break  # Poda beta
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(4):
            for j in range(4):
                if tablero[i][j] == " ":
                    tablero[i][j] = "X"
                    eval_alpha_beta = minimax_alpha_beta(
                        tablero, profundidad + 1, True, alpha, beta)
                    tablero[i][j] = " "
                    min_eval = min(min_eval, eval_alpha_beta)
                    beta = min(beta, eval_alpha_beta)
                    if beta <= alpha:
                        break  # Poda alpha
        return min_eval


def iniciar_juego_gato_ia_ia():
    tablero = crear_tablero()
    while (True):
        print("Turno de X")
        fila, columna = mejor_movimiento(tablero, "X", True)
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "X")
        time.sleep(1)
        if es_ganador(tablero):
            break
        # fila,columna = solicitar_coordenadas()
        # rellenar_casilla(tablero,fila,columna,"O")

        print("Turno de O")
        fila, columna = mejor_movimiento(tablero, "O", False)
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "O")
        time.sleep(1)
        if es_ganador(tablero):
            break


def iniciar_juego_gato_jugador_ia():
    tablero = crear_tablero()
    while (True):
        print("Turno de X")
        fila, columna = solicitar_coordenadas()
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "X")
        if es_ganador(tablero):
            break
        # fila,columna = solicitar_coordenadas()
        # rellenar_casilla(tablero,fila,columna,"O")

        print("Turno de O")
        fila, columna = mejor_movimiento(tablero, "O", False)
        print(fila, columna)
        rellenar_casilla(tablero, fila, columna, "O")
        if es_ganador(tablero):
            break


if __name__ == "__main__":
    # iniciar_juego_gato()
    # iniciar_juego_gato_2_jugadores()
    # iniciar_juego_gato_jugador_IA()
    # iniciar_juego_gato_jugador_IA
    iniciar_juego_gato_ia_ia()
