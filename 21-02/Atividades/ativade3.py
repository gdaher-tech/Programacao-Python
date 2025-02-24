print("Este programa ira realizar manipulação de strings, trocando vogais por números")

frase = input("Digite uma frase: ")

substituicao = {"a" : "4", "e" : ">", "i" : "$", "o" : "0", "u" : "W-W"}

for letra, numero in substituicao.items():
    frase = frase.replace(letra, numero)
    
    
    
print("Frase manipulada: ", frase)
