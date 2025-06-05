faturamento = 1500
custo = 700
imposto = 0.1 * faturamento
lucro = faturamento - custo - imposto

print (faturamento)
print (custo)
print (imposto)
print (lucro)

# Manipulando string
# print(f"O faturamento é {faturamento}, o custo é {custo}, o imposto é {imposto} e o lucro é {lucro}")
print("O faturamento é {}, o custo é {}, o imposto é {} e o lucro é {}".format(faturamento, custo, imposto, lucro))

email_cliente = "amanda@gmail.com"
# Colocando todas as letras maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)
# Colocando todas as letras minusculas
email_cliente = email_cliente.lower()
print(email_cliente)

nome_cliente = "amanda sousa"
# Colocando a primeira letra do nome maiuscula
nome_cliente = nome_cliente.capitalize()
print(nome_cliente)
# Colocando as primeiras letras do nome maiusculas
nome_cliente = nome_cliente.title()
print(nome_cliente)

# Encontrar um caractere no texto
print (nome_cliente.find("m"))

# Contar quantos caracteres tem no texto
print(len(nome_cliente))
print(len(email_cliente))

# Pegar um caractere
print(nome_cliente[11])

# Pegar um pedaço do texto
print(email_cliente[0:6])

# Substituir parte do texto
email_cliente = email_cliente.replace("@gmail.com", "@hotmail.com")
print(email_cliente)

# Dividir o texto
email = "qualquercoisa@gmail.com"
provedor = email.split("@")[1]
print("O provedor do email é", provedor)

nome = "Mateus Gonçalvez do Nascimento"
nome1 = nome.split()[0]
print(nome1)


#modificando

#modificando para outra atividade
