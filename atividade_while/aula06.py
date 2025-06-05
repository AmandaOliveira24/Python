import os
os.system ("cls")
# x = 1
# while x <= 3:
#     print(x)
#     x = x + 1

# x = 1
# while x <= 100:
#     print(x)
#     x = x + 1


# x = 50
# while x <= 100:
#     print(x)
#     x = x + 1

# x = 10
# while x >= 0:
#     print(x)
#     x = x - 1
# print("Fogo!")

# x = 10
# while x <= 100:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1


# x = 0

# num = int(input("Digite a quantidade do loop: "))
# while x <= num:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

# senha = "senac"
# senhains = input("Digite a senha: ")
# while senhains != senha:
#     print("Senha incorreta. Tente novamente!")
#     senhains = input("Digite a senha: ")
    
# print("Acesso concedido!")


# soma = 0 
# while True:
#     numero = float(input("Digite um numero para somar ou 0 para sair"))
#     if numero == 0:
#         break
#     soma += numero
# print(f"A soma de todos os numeros digitados é {soma}")


# while True:
#     idade = int(input("Digite uma idade: "))
#     if idade >= 18:
#         print("Acesso a festa permitido!")
#     else:
#         print("Entrada proibida!")

#     while True:
#         continuar = input("Deseja verificar mais alguma idade [S ou N]: ").strip().upper()
#         if continuar =="S":
#             break
#         elif continuar == "N":
#             print("Fim da Verificação!")
#             exit()

#         else:
#             print("Dado inválido digite somente S ou N")





while True:
    idade = int(input("Digite uma idade: "))
    if idade >= 18:
        print("Acesso a festa permitido!")
    else:
        print("Entrada proibida!")

    continuar = input("Deseja verificar mais alguma idade [S ou N]: ").strip().upper()
    if continuar == "N":
       print("Fim da Verificação!")
       exit(18)
         
    elif continuar == "S":
        break
           
    else:
            print("Dado inválido digite somente S ou N") 
            


#modificando

#modificando para outra atividade


