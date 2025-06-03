# dic_produto = {"ipad": 3000, "iphone": 5000, "airpod": 800, "macbook": 10000}
# print(dic_produto)

# #Encontrar valor no dicionário
# print(dic_produto['ipad'])

# #Adicionar valor no dicionario
# dic_produto['apple watch'] = 4000
# print(dic_produto)

# #calcular valor dentro do dicionário
# dic_produto['iphone'] = dic_produto['iphone'] * 1.3
# print(dic_produto)

# #remover valor do dicionário
# dic_produto.pop('apple watch')
# print(dic_produto)


# #Adicionar valor
# dic_produto['apple watch'] = 8000
# print(dic_produto)


# #Verificador de produto
# if 'iphone' in dic_produto:
#     print('O produto existe')
# else:
#     print("O produto não existe")

# #Verificador pelo Valor
# if 3000 in dic_produto.values():
#     print("Existe um produto com esse valor")
# else:
#     print("Não existe produto com esse valor")

# # cadastro de produto e preço no dicionário
# dic_produto['notebook da barbie'] = 200
# print(dic_produto)

#Atualizem os valores dos produtos com um aumento de 50%
# Atualizar os valores com aumento de 50%
# for produto in dic_produto:
#     dic_produto[produto] *= 1.5

# print(dic_produto)


meus_produtos = {'mouse': 150, 'teclado': 200, 'monitor': 800, 'gabinete': 500}
print(meus_produtos)

# nome_produto= input("Digite o nome do item que deseja encontrar: ")
# #Verificador de produto
# if nome_produto in meus_produtos:
#     print('O preço do', nome_produto, 'é: R$', meus_produtos[nome_produto])
# else:
#     print("Desculpe mas não foi possível encontrar este produto")



# item_adicionado= input("Digite o nome do produto que deseja adicionar: ")
# valor_adicionado=input("Digite o valor que deseja adicionar ao novo produto: ")
# meus_produtos[item_adicionado] = valor_adicionado
# print(meus_produtos)

# mudapreco = input("Digite o nome do produto que deseja alterar o valor: ")
# nvpreco = float(input("Digite o valor novo para o produto: "))
# if mudapreco in meus_produtos:
#     meus_produtos[mudapreco] = nvpreco
#     print(meus_produtos)

# else:
#     print("produto não encontrado!")


# remover_produto= input("Digite o produto para remover: ").lower()
# if remover_produto in meus_produtos:
#     meus_produtos.pop(remover_produto)
#     print(meus_produtos)
# else:
#     print("produto não existe!")



for produto in meus_produtos:
    meus_produtos[produto] = meus_produtos[produto] * 0.9
    print(meus_produtos)








