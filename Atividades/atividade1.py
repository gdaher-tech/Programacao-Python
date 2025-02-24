
print("Este programa tem o objetivo de manipular uma frase que digitar, substituindo letras por número")
frase = input("Digite uma frase: ")
nova_frase = frase.replace("a","4").replace("e","3").replace("i","1").replace("o", "0")

print("O programa ira realizar uma substituição simples: \n a = 4 \n e = 3 \n i = 1 \n o = 0")

print("A frase original era: ",frase)
print("Frase manipulada: ",nova_frase)


frase2 = input("Digite uma nova frase: ")

substituicoes = {"a" : "4", "e" : "3", "i" : "1","o" : "0" }
 
novafrase2 = frase2 

for letra, numero in substituicoes.items(): 
    novafrase2 = novafrase2.replace(letra,numero)

print("Frase manipulada: ",novafrase2)




