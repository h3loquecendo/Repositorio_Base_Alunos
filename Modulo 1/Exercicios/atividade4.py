print("-----------------------")
print("---sistema de loggin---")
print("-----------------------")

usuario = input("digite seu usuario: ")
senha = input("digite sua senha: ")

if usuario == "admin" and senha == "1234":
    print("logado")
else:
    print("usuario ou senha incorreta")