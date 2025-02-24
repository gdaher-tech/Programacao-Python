
### 1 - Manipule a string para fazer substituições simples como nos exemplos abaixo: 

    - Letras por números:

        - As galinhas têm um sistema → As g4l1nh4s têm um s1st3m4
        - Para fazer qualquer coisa → P4r4 f4z3r qu4lqu3r c01s4

``
``` python 
	frase = input("Digite uma frase: ") ## recebe una frase do usuário e armazena na variavel frase

	novafrase = frase.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0")  ## define uma nova variável com nome novafrase como a variavel frase com as funções de replace para manipulação de strings. 

	print("O programa ira realizar uma substituição simples: \n a = 4 \n e = 3 \n i = 1 \n o = 0")

	print("A frase original era: ",frase) ## imprime a frase inicial sem a manipulação dos dados 

	print("Frase manipulada: ",novafrase) ## Imprime a frase manipulada 
	
```


`frase = input("Digite uma frase")` - define uma variável chamada frase e usa o input para receber o valor desta variável pelo usuário.

`novafrase = frase.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0")` - define uma variável chamada ``novafrase`` com uma  com metodos ``.replace`` para fazer manipulações e substituições de strings na variável frase. 

`print("O programa ira realizar uma substituição simples: \n a = 4 \n e = 3 \n i = 1 \n o = 0")`  - imprime uma frase indicando que a frase original era a que estava armazenada na variável ``frase`` 

`print("Frase manipulada: ",novafrase)` - imprime uma frase indicando que a nova frase manipulada é a variável ``novafrase`` 

---

### 2 - Letras por símbolos  

        - As galinhas têm um sistema → As g@l1nh@s têm um s1st3m@
        - Para fazer qualquer coisa → P@r@ f@z3r qu@lqu3r c01s@

``` python 
	print("Este programa irá realizar uma manipulação de strings, substituindo letras por simbolos")

	frase = input("Digite uma frase: ")

	novafrase = frase.replace("a","@").replace("o","()").replace("i","|")

	print("Frase manipulada: ",novafrase)

```

```
print("Este programa irá realizar uma manipulação de strings, substituindo letras por simbolos")
```
O programa imprime uma mensagem ao usuário indicando que irá realizar uma manipulação de string, substituindo letras por símbolos 

``frase = input("Digite uma frase: ")``
O programa define uma variável frase, que recebe seu valor através de um input que captura a frase inserida pelo usuário. 

``novafrase = frase.replace("a","@").replace("o","()").replace("i","|")``
O programa define uma variável ``novafrase`` que recebe o valor de frase com um método .``replace``, este método é responsável por manipular as strings, trocando "a" por "@", "o" por "0", "i" por "|". 

``print("Frase manipulada: ",novafrase)``
Por fim, o programa imprime um texto indicando que a frase manipulada é a variável `novafrase`


---

### 3 - Vogais por números/símbolos 

Vogais por números/símbolos:

        - As galinhas têm um sistema → As g4l1nh4s têm um s1st3m4
        - Para fazer qualquer coisa → P4r4 f4z3r qu4lqu3r c01s4


``` python 
print("Este programa ira realizar manipulação de strings, trocando vogais por números")

  
frase = input("Digite uma frase: ")

substituicao = {"a" : "4", "e" : ">", "i" : "$", "o" : "0", "u" : "W-W"}


for letra, numero in substituicao.items():

    frase = frase.replace(letra, numero)

print("Frase manipulada: ", frase)
```


``print("Este programa ira realizar manipulação de strings, trocando vogais por números")``  - Imprime uma mensagem ao usuário para orienta-lo que o programa ira realizar uma manipulação de strings trocando vogais por números. 

``frase = input("Digite uma frase: ")`` -- Cria uma variável frase que recebe uma frase do usuário 


``substituicao = {"a" : "4", "e" : ">", "i" : "$", "o" : "0", "u" : "W-W"}`` - Cria um dicionário que contem as letras como chaves e seus valores como as substituições que o programa irá fazer 


``for letra, numero in substituicao.items():``  -  o método `.items`  retorna pares chaves-valor  de um dicionário.  neste caso `letra` representa a chave (que será procurado na ``frase``), e número representa valor (que substituirá a chave)

``    frase = frase.replace(letra, numero)`` - O método `.replace(letra, numero)` é utilizado para substituir todas as ocorrências de `letra` dentro de `frase` por `numero`.

`.items()` - retorna uma lista de tuplas de, neste caso letra e número, letra sendo chave e número sendo valor. 

---

### Desafio 

Manipule a string para fazer substituições suando cifras de césar como nos exemplos abaixo:

    - Deslocamento de letras:
        - As galinhas têm um sistema (deslocamento 3) → Dv jdolqkdvh têm xp vlvwhpd
        - Para fazer qualquer coisa (deslocamento 5) → Ufwd gdgjwdj wxguxhu frlvd

``` python

print("Este programa deve substituir strings usando sifras de césar")

print("Vamos começar com o deslocamento 3")


frase = input("Digite uma frase: ")

tabela = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "DEFGHIJKLMNOPQRSTUVWXYZABC")

frase = frase.upper().translate(tabela)

  
print("Frase manipulada: ", frase)

## ----------------- ##

print("Vamos realizar a manipulação com descolocamento 5")


frase2 = input("Digite uma segunda frase: ")

desloc5 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "FGHIJKLMNOPQRSTUVWXYZABCDE")

frase2 = frase2.upper().translate(desloc5)


print("Frase manipulada: ", frase2)
```


`print("Este programa deve substituir strings usando sifras de césar")
``print("Vamos começar com o deslocamento 3")

O programa imprime dois textos ao seu usuário, o primeiro indicando a sua função e o segundo avisando o início com deslocamento 3. 


``frase = input("Digite uma frase: ")``

A variável ``frase`` é criada, o seu valor é atribuído a ela como a leitura da frase do usuário por meio de um ``input`` 

``tabela = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "DEFGHIJKLMNOPQRSTUVWXYZABC")``

A variável **`tabela`** é criada e recebe um mapeamento de caracteres gerado pela função **`str.maketrans`**. Este mapeamento substitui cada letra do alfabeto (de **A** a **Z**) pela letra correspondente deslocada em 3 posições à frente, de modo que, por exemplo, **A** se torna **D**, **B** se torna **E**, e assim por diante.

``frase = frase.upper().translate(tabela)``

A variável **`frase`** recebe o valor dela mesma, mas primeiro tem todos os seus caracteres convertidos para **maiúsculas** com o método **`upper()`**. Em seguida, esses caracteres são substituídos de acordo com o mapeamento da **`tabela`** usando o método **`translate()`**

``print("Vamos realizar a manipulação com descolocamento 5")``

O programa imprime uma mensagem ao seu usuário indicando que a próxima manipulação é com deslocamento 5 

``frase2 = input("Digite uma segunda frase: ")``

A variável `frase2` è criada e recebe seu valor através de um `input` 

``desloc5 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "FGHIJKLMNOPQRSTUVWXYZABCDE")``

A variável `desloc5` é criada e recebe um mapeamento de caracteres gerados pela função ``str.maketrans`` este mapeamento substitui cada letra do alfabeto (A a Z) pela letra correspondente deslocada em 5 posições a frente 

``frase2 = frase2.upper().translate(desloc5)``

A variável frase 2 recebe o valor dela mesma porém com o método `.upper()` para transformar todos os seus caracteres em maiúsculo e o método `.translate()` para traduzir cada um de seus caracteres usando o mapeamento `desloc5`  
