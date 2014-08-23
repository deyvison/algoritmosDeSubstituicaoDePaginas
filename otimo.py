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

for i in range(len(dados)):
    futuro = dados[i:]
    if (dados[i] not in lista):

        status = "miss"

        if("_" in lista):
            pos = lista.index("_")
            del lista[pos]
            lista.insert(pos,dados[i])
        else:
           ##
            isFor = True
            for m in lista:
                if(m not in futuro):
                    isFor = False

                    poss = lista.index(m)
                    del lista[poss]
                    lista.insert(poss,dados[i])
                    break



            if(isFor):
                indicesDosDados = []
                for lol in lista:
                    indicesDosDados.append(futuro.index(lol))
                maior = max(indicesDosDados)
                dado = futuro[maior]
                poss = lista.index(dado)

                del lista[poss]
                lista.insert(poss,dados[i])


    else:
        status = "hit"


    print(dados[i],"/",status,"/ memória:",lista)


