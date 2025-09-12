nome = input("digite seu nome:")

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print ("abaixo do peso")
elif imc < 24.9:
    print("peso normal")
else:
    print("obesidade")

print(f"o imc do aluno {nome} é : {imc}")

