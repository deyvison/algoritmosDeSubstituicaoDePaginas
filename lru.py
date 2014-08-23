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
passado = []
for i in range(len(dados)):

    for p in dados[:i+1]:
        if p not in passado:

            passado.append(p)


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
                if(m not in passado):
                    isFor = False

                    poss = lista.index(m)
                    del lista[poss]
                    lista.insert(poss,dados[i])
                    break



            if(isFor):
                indicesDosDados = []
                for lol in lista:
                    indicesDosDados.append(passado.index(lol))
                menor = min(indicesDosDados)
                dado = passado[menor]
                poss = lista.index(dado)

                del lista[poss]
                lista.insert(poss,dados[i])



                passado.remove(dado)

    else:
        status = "hit"
        del passado[passado.index(dados[i])]

    print(dados[i],"/",status,"/ memória:",lista)

