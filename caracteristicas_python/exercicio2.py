frase = " Python é uma linguagem MUITO poderosa! Python é incrível "
print(frase)

# remove os espaços em branco no inicio e no fim da frase
frase = " ".join(frase.split())
print(frase)

frase =  frase.strip()
print(frase)

# transformar a frase em letras minusculas 
frase = frase.lower()
print(frase)

# transformar a frase em letras 
frase = frase.upper()
print(frase)

# colocar apenas a primeira letra da primeira palavra da frase com a letra maiuscula
frase = frase.capitalize()
print(frase)

# colocar as primeiras letras de todas as palavras maiusculas
frase = frase.title()
print(frase)

# substituir Python por java
frase = frase.replace("Python", "Java")
print(frase)

# contar quantas vezes o Python aparece na frase original
frase = " Python é uma linguagem MUITO poderosa! Python é incrível "
frase = frase.count('Python')
print(frase)
# encontrar a posição da palavra poderosa.
frase = " Python é uma linguagem MUITO poderosa! Python é incrível "
posicao = frase.find('poderosa')
print(posicao)
