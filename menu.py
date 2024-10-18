
from gato4x4 import iniciar_juego_gato_jugador_ia,iniciar_juego_gato_ia_ia,iniciar_juego_gato_2_jugadores


def menu():
	print("*** MENU  GATO 4x4***")
	print("1.-Humano vs Humano")
	print("2.-Humano vs IA")
	print("3.-IA vs IA")
	print("4.-Salir")
	while True:
		opcion = int(input("Ingresa la opción deseada entre 1-4:"))
		if opcion >= 1 and opcion <=4:
			break
		else:
			print("Valor incorrecto")
	return opcion

if __name__ == "__main__": 
	while True:
		opcion = menu()
		if opcion == 1:
			iniciar_juego_gato_2_jugadores()
		elif opcion == 2:
			iniciar_juego_gato_jugador_ia()
		elif opcion == 3:
			iniciar_juego_gato_ia_ia()
		else:
			print("Gracias por jugar")
			exit(0)