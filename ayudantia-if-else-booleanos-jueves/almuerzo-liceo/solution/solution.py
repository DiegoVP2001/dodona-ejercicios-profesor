es_4to = input() == "si"
tiene_voucher = input() == "si"
if es_4to or tiene_voucher:
    print("Almuerzo subvencionado: $0")
else:
    print("Almuerzo valor normal: $1.500")
