import array as arr

# 1. Array de números inteiros sequenciais simples (código 'i')
numeros_sequenciais = arr.array('i', [1, 2, 3, 4, 5,6,7,8,9,10])

# 2. Array de números decimais/float variados (código 'd')
numeros_decimais = arr.array('d', [1.5, 3.14, 7.8, 10.2, 42.0])

# 3. Array contendo apenas o número zero repetido (código 'i')
lista_zeros = arr.array('i', [0, 0, 0, 0, 0])

# 4. Array com números inteiros grandes (código 'i')
numeros_grandes = arr.array('i', [1000, 5000, 25000, 100000, 1000000])

# 5. Array com números negativos e positivos mesclados (código 'i')
numeros_mistos = arr.array('i', [-10, -5, 0, 5, 10])

def achar_menor(lista):
    menor = 0
    n0 = lista[0]
    if n0 > menor:
        menor = n0
    for i in lista:
        if menor > i :
            menor = i
    print(menor)

def achar_maior(lista):
    maior = 0
    for i in lista:
        if maior < i: 
            maior = i
    print(maior)

achar_maior(numeros_sequenciais)
achar_maior(numeros_decimais)