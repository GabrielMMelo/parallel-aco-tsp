import math
import sys

from plot import plot

IS_PARALLEL = int(sys.argv[1])

if IS_PARALLEL:
    print("PARALLEL")
    from aco_parallel import ACO, Grafo
else:
    from aco import ACO, Grafo

def calc_distancia(cidade1, cidade2):
    return math.sqrt((cidade1['x'] - cidade2['x'])**2 +
                     (cidade1['y'] - cidade2['y'])**2)


def main():
    cidades = []
    pontos = []
    with open('./data/chn31.txt') as f:
        for linha in f.readlines():
            cidade = linha.split(' ')
            cidades.append(
                dict(index=int(cidade[0]), x=int(cidade[1]), y=int(cidade[2])))
            pontos.append((int(cidade[1]), int(cidade[2])))
    matriz_adjacencia = []  # matriz de adjacencia
    rank = len(cidades)
    for i in range(rank):
        linha = []
        for j in range(rank):
            linha.append(calc_distancia(cidades[i], cidades[j]))
        matriz_adjacencia.append(linha)
    aco = ACO(cont_formiga=10, geracoes=100, alfa=1.0, beta=10.0, ro=0.5, Q=10)
    grafo = Grafo(matriz_adjacencia, rank)
    try:
        caminho, custo = aco.resolve(grafo)
        print('custo total: {}, caminho: {}'.format(custo, caminho))
        plot(pontos, caminho)
    except TypeError:
        pass


if __name__ == '__main__':
    main()
