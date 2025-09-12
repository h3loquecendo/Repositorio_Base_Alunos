nome_produto =  input("digite o nome do produto: ")
preco = float(input("digite o preco: R$"))
desconto = float(input("digite o percentual: "))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print("-----------------------------")
print(f"produto: {nome_produto}")
print(f"preco final: R$ {preco_final}")
print("------------------------------")