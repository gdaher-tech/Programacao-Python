print("Este programa deve substituir strings usando sifras de césar")

print("Vamos começar com o deslocamento 3")

frase = input("Digite uma frase: ")

tabela = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "DEFGHIJKLMNOPQRSTUVWXYZABC")

frase = frase.upper().translate(tabela)

print("Frase manipulada: ", frase)

print("Vamos realizar a manipulação com descolocamento 5")

frase2 = input("Digite uma segunda frase: ")

desloc5 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "FGHIJKLMNOPQRSTUVWXYZABCDE")

frase2 = frase2.upper().translate(desloc5)

print("Frase manipulada: ", frase2)

