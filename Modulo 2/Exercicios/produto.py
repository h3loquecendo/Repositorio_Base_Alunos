nome_produto =  input("digite o nome do produto: ")
preco = float(input("digite o preco: R$"))
quantidade = float(input("digite a quantidade: "))


with open("produto.txt", "a") as produto:
    produto.write(f"Produto: {nome_produto} | valor: {preco} | quantidade: {quantidade}")