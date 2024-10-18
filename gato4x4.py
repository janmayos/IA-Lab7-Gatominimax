
import random

def crear_tablero():
	tablero = [[" ", " ", " "," "],
			[" ", " ", " "," "], 
			[" ", " ", " "," "],
			[" ", " ", " "," "]]
	print_tablero(tablero)
	return tablero

def print_tablero(tablero):
	matrix_length = len(tablero)
	for i in range(matrix_length):
		print(tablero[i])

def solicitar_coordenadas():
	while True:
		fila = int(input("Ingresa la fila:"))
		if fila >= 0 and fila <=3:
			break
		else:
			print("Favor de ingresar un valor del 0-3")

	while True:
		columna = int(input("Ingresa la columna:"))
		if columna >= 0 and columna <=3:
			break
		else:
			print("Favor de ingresar un valor del 0-3")
	
	return fila,columna

def rellenar_casilla(tablero,fila,columna,valor):
	if tablero[fila][columna] == " ":
		tablero[fila][columna]= valor
		print_tablero(tablero)
	else:
		print("Casilla ocupada volver a seleccionar coordenadas")
		fila,columna = solicitar_coordenadas()
		rellenar_casilla(tablero,fila,columna,valor)

def eval_columnas(tablero,valor,matrix_length,matrix_length_column):
	ban = False
	for columna in range(matrix_length):
		for fila in range(matrix_length_column):
			if tablero[fila][columna] == " " or tablero[fila][columna] != valor:
				ban=False
				break
			else: 
				ban = True
		if ban:
			break
	return ban

def eval_filas(tablero,valor,matrix_length,matrix_length_column):
	ban = False
	for fila in range(matrix_length):
		for columna in range(matrix_length_column):
			if tablero[fila][columna] == " " or tablero[fila][columna] != valor:
				ban=False
				break
			else: 
				ban = True
		if ban:
			break
	return ban

def eval_diagonal(tablero,valor):
	ban = False
	if tablero[0][0] == valor and tablero[1][1] == valor and tablero[2][2] == valor and tablero[3][3] == valor:
		ban =  True
	if tablero[0][3] == valor and tablero[1][2] == valor and tablero[2][1] == valor and tablero[3][0] == valor:
		ban =  True
		
	return ban


def eval_tablero(tablero):
	matrix_length = len(tablero)
	matrix_length_column = len(tablero[0])
	if eval_columnas(tablero,"X",matrix_length,matrix_length_column):
		return "X gano en columna"
	if(eval_columnas(tablero,"O",matrix_length,matrix_length_column)):
		return "O gano en columna"
	if eval_filas(tablero,"X",matrix_length,matrix_length_column):
		return "X gano en fila"
	if(eval_filas(tablero,"O",matrix_length,matrix_length_column)):
		return "O gano en fila"
	if eval_diagonal(tablero,"X"):
		return "X gano en diagonal"
	if(eval_diagonal(tablero,"O")):
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


def generar_aleatorios_rellenar(tablero,valor):
	while True:
		fila = random.randint(0, 3)
		columna = random.randint(0, 3)
		if tablero[fila][columna] == " ":
			tablero[fila][columna]= valor
			print(fila,columna)
			break
	print_tablero(tablero)

def iniciar_juego_gato():
	tablero = crear_tablero()
	while(True):
		fila,columna = solicitar_coordenadas()
		print(fila,columna)
		rellenar_casilla(tablero,fila,columna,"X")
		if es_ganador(tablero):
			break
		#fila,columna = solicitar_coordenadas()
		#rellenar_casilla(tablero,fila,columna,"O")
		generar_aleatorios_rellenar(tablero,"0")
		if es_ganador(tablero):
			break


if __name__ == "__main__": 
	iniciar_juego_gato()