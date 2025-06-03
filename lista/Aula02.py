frutas = ["Uva", "Manga", "Laranja", "Abacate"]
numeros = [1, 2, 3, 4, 5, 2, 3, 2, 1, 2]
variados = [1, "dois", 3, "quatro", True]
print(frutas)

print(frutas[0])
print(numeros[-1])
print(variados[2])


# substituir valores na lista
frutas[1] = "Abacaxi"
print(frutas)

variados = [1, "dois", 3, "quatro", True]

variados[1] = 2
print(variados)

#adiciona coisa na lista
numeros.append(6)
print(numeros)

#adiciona posição determinada
frutas.insert(0,"cupuaçu")
print(frutas)

#remove valores da lista
frutas.remove("cupuaçu")
print(frutas)

frutas.pop()
print(frutas)

#conta quantas vezes o valor aparece na lista
print(numeros.count(1))

print(len(numeros))


#ordem alfabética
frutas.sort()
print(frutas)

#ordem inversa
numeros.reverse()
print(numeros)





#criar lista com Nomes
nomes = ["Raimunda", "Italo", "Ronaldo", "Boaventura"]
print(nomes)
#adicionar mais 3 nomes
nomes.append("Pedro")
nomes.append("Kaio")
nomes.append("Matheus")
print(nomes)
#excluir 2 nomes
nomes.remove("Italo")
nomes.remove("Ronaldo")
print(nomes)

#vao colocar em ordem alfabética
nomes.sort()
print(nomes)