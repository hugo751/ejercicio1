import math

def calcular_circunferencia(radio):
    pi = round(math.pi, 6)
    circunferencia = 2 * pi * radio
    return round (circunferencia, 2)

radios = [3, 8, 10]

for radio in radios:
    print(f"La circunferencia con radio {radio} es: {calcular_circunferencia(radio)}")
