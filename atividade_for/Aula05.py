#n = int(input("Digite um numero: "))
#soma = 0

#for i in range(1,n+1):
   # soma += i
   # print("A soma dos numeros é ", soma)

#palavra = "Python" 
#or letra in palavra:
#    print(letra)

#lista = []
#for i in range (5):
 #   nome = input("Digite um nome: ")
  #  lista.append(nome)
   # print(f"O nome que foi digitado é {nome}")
    #print(lista)

#lista = []
#for i in range (5):
 #   nome = input("Digite um nome: ").capitalize()
  #  lista.append(nome)
   # print(f"O nome que foi digitado é {nome}")
#print(lista)

#busca = input("digite o nome que deseja procurar: ").capitalize()

#if busca in lista:
 #   print(busca, "está na lista!")

#else:
 #   print(busca,"não está na lista")








# #num = 7
# #for i in range(11):
#  #   resultado = num * i 
#    print (f'{num} * {i} = {resultado}')


# num = int(input("digite um número para visualizar sua tabuada: "))

# for i in range(11):
#     resultado = num * i 
#     print (f'{num} * {i} = {resultado}')


# num = 8
# if num % 2 == 0:
#     print("Número par")
# else:
#     print("Número ímpar")


# for num in range(1,101):
#     if num % 2 == 0:
#         print(num)


# lista = [1000, 800, 2000, 2500, 700, 650, 999]

# meta = 1000

# for valor in (lista):
#     if valor >= meta:
#         print("Você atingiu a meta!")

#     else:
#         print("VocÊ não atingiu a meta!")





# notas = [7.5, 8.0, 6.9, 8.7, 5.3, 4.1, 3.8]

# for nota in (notas):
#     if nota >= 7.0:
#         print(f"Nota {nota} Aprovado!")

#     elif nota >=5 and nota <= 7:
#         print(f"Nota {nota} Recuperação")

#     elif nota < 5:
#         print(f"Nota {nota} Reprovado")

#     else:
#         print("nota não reconhecida")


#lista = []
#for i in range (5):
 #   nome = input("Digite um nome: ").capitalize()
  #  lista.append(nome)
   # print(f"O nome que foi digitado é {nome}")
#print(lista)

# soma = 0
# for i in range (5):
#     num = float(input("Digite um número: "))
#     soma += num
# print("A soma dos valores é: ", soma)

user = "admin"
password = 1234

for i in range(3):
    nome = input("Digite o nome de login: ")
    senha = int(input("Digite a senha de login: "))

    if nome == user and senha == password:
        print("Acesso de login permitido")
        break
    else:
        print(f"Tentativa {i + 1} de 3 falhou")
       
else:
    print("Conta Bloqueada!")







