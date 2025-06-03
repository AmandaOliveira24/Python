n1 = float(input("Digite o primeiro numero: "))
operador = input ("digite o operador: ")
n2 = float(input("Digite o segundo numero: "))

if operador == "-":
    resultado = n1 - n2
    print("Resultado: ", resultado)

elif operador == "+":
    resultado = n1 + n2
    print("Resultado: ", resultado )

elif operador == "*":
    resultado = n1 * n2
    print("Resultado: ", resultado)

elif operador == "/":
    if n1 and n2 != 0:
        resultado = n1 / n2
        print("Resultado: ", resultado)
    else:
        print("Divisão inválida")

else:
    print("Operador Inválido!")





