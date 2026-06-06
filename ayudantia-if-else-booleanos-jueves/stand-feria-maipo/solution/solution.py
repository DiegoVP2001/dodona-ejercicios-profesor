ficha_al_dia = input() == "si"
puestos = int(input())
print("¿Puede inscribir su stand?", ficha_al_dia and puestos > 0)
