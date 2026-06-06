saldo = int(input())
precio = int(input())

print("Alcanza para comprar?", saldo >= precio)
print("Queda saldo positivo?", saldo - precio > 0)
print("Saldo exacto al precio?", saldo == precio)
