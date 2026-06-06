nombre = input()
nivel_inicial = int(input())
puntos = int(input())

niveles_ganados = puntos // 100
nivel_final = nivel_inicial + niveles_ganados

print("Jugador:", nombre)
print("Nivel final:", nivel_final)
