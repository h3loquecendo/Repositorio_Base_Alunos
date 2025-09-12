nome = input("digite seu nome: ")
email = input("digite seu e-mail: ")

arquivo = open("pessoa.txt", "a")
arquivo.write(f"{nome} | {email}\n")
arquivo.close()