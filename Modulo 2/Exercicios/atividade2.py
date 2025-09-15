nome = input("digite seu nome: ")
idade = int (input("digite sua idade: "))
possui_carteira = input("1-sim | 2-nao")

if idade >= 18: 
    print("você é maior de idade !!!")
    if possui_carteira == "sim":
        print("pode dirigir")
    else:
        print("nao pode dirigir!")
else:
    print("menor de idade!")