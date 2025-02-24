
print("Este programa irá realiza uma manipulação de strings, substituindo letras por símbolo")

frase = input("Digite uma frase: ")
novafrase = frase.replace("a", "@").replace("o","()").replace("i", "|")

print("Frase manipulada: ",novafrase)

frase2 = input("Digite outra frase: ")

novafrase2 = frase2 

substituicoes = {"a" : "@", "o" : "()", "i" : "|" }

novafrase2 = frase2

for letra, numero in substituicoes.items():
    novafrase2 = novafrase2.replace(letra, numero)
    

print("A frase manipulada: ",novafrase2)