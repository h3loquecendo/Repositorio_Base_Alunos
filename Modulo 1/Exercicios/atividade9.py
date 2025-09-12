positivos = 0
negativos = 0
zeros = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")