#  1. Soma de Dois números
#  num1 = int(input("Digite o primeiro número: ")) 
#  num2 = int(input("Digite o segundo número: "))
#  soma = num1 + num2
#  print(f"A soma é: {soma}")


#2.	Verificador de número par ou ímpar 

# num = int(input("Digite um número: "))

# if num % 2 == 0: 
#     print("O número é par.") 
# else: 
#     print("O número é ímpar.")


#3.	Tabuada personalizada 
# num = int(input("Digite um número para ver a tabuada: "))
# for i in range(1, 11): 
#     print(f"{num} x {i} = {num * i}")

# 4. Contador de vogais 
# palavra = input("Digite uma palavra: ").lower() 
# vogais = 'aeiou' 
# contador = sum(1 for letra in palavra if letra in vogais) 
# print(f"Número de vogais: {contador}")


#5. Média de notas 
# nota1 = float(input("Digite a primeira nota: ")) 
# nota2 = float(input("Digite a segunda nota: ")) 
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3 
# if media >= 7: 
#     print(f"Média {media:.2f} - Aprovado") 
# elif media >= 5: 
#     print(f"Média {media:.2f} - Recuperação") 
# else: 
#     print(f"Média {media:.2f} - Reprovado")



# 6. Lista de compras 
# lista = [] 
# for i in range(5): 
#     item = input(f"Digite o item {i + 1} da lista de compras: ") 
#     lista.append(item) 

# print("Sua lista de compras é:") 
# for item in lista: 
#     print(f"- {item}") 



#7. Verificador de palíndromo 
# palavra = input("Digite uma palavra: ").lower() 
# if palavra == palavra[::-1]: 
#     print("É um palíndromo!") 
# else: 
#     print("Não é um palíndromo.")

#8. Calculadora Simples
# n1 = float(input("Digite o primeiro numero: "))
# operador = input ("digite o operador: ")
# n2 = float(input("Digite o segundo numero: "))

# if operador == "-":
#     resultado = n1 - n2
#     print("Resultado: ", resultado)

# elif operador == "+":
#     resultado = n1 + n2
#     print("Resultado: ", resultado )

# elif operador == "*":
#     resultado = n1 * n2
#     print("Resultado: ", resultado)

# elif operador == "/":
#     if n1 and n2 != 0:
#         resultado = n1 / n2
#         print("Resultado: ", resultado)
#     else:
#         print("Divisão inválida")

# else:
#     print("Operador Inválido!")




#9. Números pares de 1 a 50 
# for num in range(1,51):
#     if num % 2 == 0:
#         print(num)



#10. Cadastro de usuários 
# nome = input("Digite o nome: ") 
# idade = int(input("Digite a idade: ")) 
# email = input("Digite o e-mail: ") 
# usuario = { 
# 'nome': nome, 
# 'idade': idade, 
# 'email': email 
# } 
# print("Cadastro completo:") 
# print(usuario) 


# 11.	Contador de números positivos e negativos 
# positivos = negativos = zeros = 0
# for i in range(10):
#     num = float(input(f"Digite o {i+1}º número: "))
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
#     else:
#         zeros += 1

# print(f"Positivos: {positivos}, Negativos: {negativos}, Zeros: {zeros}")



# 12. Maior e menor número 
# numeros = [] 
# for i in range(5): 
#     n = float(input(f"Digite o {i+1}º número: ")) 
#     numeros.append(n) 
# print(f"Maior número: {max(numeros)}") 
# print(f"Menor número: {min(numeros)}")


#13. Contador de palavras 
# frase = input("Digite uma frase: ") 
# quantidade = len(frase.split()) 
# print(f"A frase contém {quantidade} palavras.")

# 14. Gerador de senha aleatória 
# import random 
# import string 
# caracteres = string.ascii_letters + string.digits + string.punctuation 
# senha = ''.join(random.choice(caracteres) for _ in range(8)) 
# print(f"Senha gerada: {senha}")



# 15. Fatorial de um número 
# num = int(input("Digite um número inteiro: ")) 
# fatorial = 1 
# for i in range(2, num + 1): 
#     fatorial *= i 
# print(f"{num}! = {fatorial}")



# 16. Verificador de número primo 
# num = int(input("Digite um número: ")) 
# if num < 2: 
#     print(f"{num} não é primo.") 
# else: 
#     eh_primo = True 
# for i in range(2, int(num ** 0.5) + 1): 
#     if num % i == 0: 
#         eh_primo = False 
#         break 
# if eh_primo: 
#     print(f"{num} é primo.") 
# else: 
#     print(f"{num} não é primo.")


#17. Conversor de temperatura 
# celsius = float(input("Digite a temperatura em Celsius: ")) 
# fahrenheit = (celsius * 9/5) + 32  
# print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")


#18.	Agenda de contatos 
# agenda = {} 
# for i in range(3): 
#     nome = input(f"Digite o nome do contato {i+1}: ") 
#     telefone = input("Digite o telefone: ") 
#     agenda[nome] = telefone 
# print("Contatos cadastrados:") 
# for nome, telefone in agenda.items(): 
#     print(f"{nome}: {telefone}")



#19. Contagem regressiva com tempo 
# import time 
# num = int(input("Digite um número para a contagem regressiva: ")) 
# for i in range(num, -1, -1): 
#     print(i) 
#     time.sleep(1) 
# print("Contagem finalizada!") 

# 20. Verificador de CPF simples  
# cpf = input("Digite o CPF (somente números): ") 
# if len(cpf) == 11 and cpf.isdigit(): 
#     print("CPF válido.")
# else: 
#     print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")

