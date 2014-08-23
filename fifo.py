__author__ = 'Deyvison Melo'

dados = input().split()
qtQuadros = int(input())

for i in range(len(dados)):
    dados[i] = int(dados[i])

lista = []
for j in range(qtQuadros):
    lista.append('_')
MAX = qtQuadros

status = ""
indice = 0

for i in range(len(dados)):

    if (dados[i] not in lista):

        status = "miss"
        del lista[indice]
        lista.insert(indice,dados[i])
        indice = (indice+1) % MAX

    else:

        status = "hit"

    print(dados[i],"/",status,"/ memória:",lista)


