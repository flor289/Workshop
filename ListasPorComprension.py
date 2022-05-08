#ejemplo 1
lista = [ j**2 for j in range(5)]
print(lista)

#ejemplo 2
lista_anidada = [[ j for j in range(5)] for i in range(3)]
print(lista_anidada)

#ejemplo 3
results = [n**2 if n < 3 else n for n in range(5)]
print(results)



#¿por que usar lista por comprension?

from datetime import datetime
from random import randint
import numpy as np

#matriz de 10000*10000 mediante un bucle for
hora1=datetime.now()
matriz = []
for i in range(10000):
    matriz.append([])
    for j in range(10000):
        matriz[i].append(randint(0,100))
print(f'El tiempo con un bucle es de {datetime.now() - hora1} segundos')


#matriz de 10000*10000 mediante listas por comprension
hora1=datetime.now()
matriz_comprension = [[randint(0,100) for i in range(10000)]for i in range(10000)]
print(f'El tiempo con listas por comprension es de {datetime.now() - hora1} segundos')

#matriz de 10000*10000 mediante matriz_numpy
hora1=datetime.now()
matriz_numpy = np.random.randint(100, size=(10000,10000))
print(f'El tiempo con numpy es de {datetime.now() - hora1} segundos')


