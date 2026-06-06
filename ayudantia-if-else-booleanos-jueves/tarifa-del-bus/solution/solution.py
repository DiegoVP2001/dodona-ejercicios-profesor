tiene_tne = input() == "si"
es_regional = input() == "si"
if tiene_tne and es_regional:
    print("Tarifa a pagar: $490")
else:
    print("Tarifa a pagar: $810")
