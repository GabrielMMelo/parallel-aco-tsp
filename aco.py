import random


class Grafo(object):
    def __init__(self, matriz_adjacencia, rank):
        self.matriz = matriz_adjacencia
        self.rank = rank
        self.feronomio = [[1 / (rank * rank) for j in range(rank)]
                          for i in range(rank)]


class ACO(object):
    def __init__(self, cont_formiga, geracoes, alfa, beta, ro, Q):
        self.Q = Q
        self.ro = ro
        self.beta = beta
        self.alfa = alfa
        self.cont_formiga = cont_formiga
        self.geracoes = geracoes

    def _atualiza_feronomio(self, grafo, formigas):
        for i, linha in enumerate(grafo.feronomio):
            for j, col in enumerate(linha):
                grafo.feronomio[i][j] *= self.ro
                for formiga in formigas:
                    grafo.feronomio[i][j] += formiga.feronomio_delta[i][j]

    def resolve(self, grafo):
        melhor_custo = float('inf')
        melhor_solucao = []
        for gen in range(self.geracoes):
            formigas = [
                _Formiga(self, grafo) for i in range(self.cont_formiga)
            ]
            for formiga in formigas:
                for i in range(grafo.rank - 1):
                    formiga._seleciona_proximo()
                formiga.custo_total += grafo.matriz[formiga.tabu[-1]][
                    formiga.tabu[0]]
                if formiga.custo_total < melhor_custo:
                    melhor_custo = formiga.custo_total
                    melhor_solucao = [] + formiga.tabu
                # atualiza feronomio
                formiga._atualiza_feronomio_delta()
            self._atualiza_feronomio(grafo, formigas)
            # print('generation #{}, best cost: {}, path: {}'.format(gen, melhor_custo, melhor_solucao))
        return melhor_solucao, melhor_custo


class _Formiga(object):
    def __init__(self, aco, grafo):
        self.colonia = aco
        self.grafo = grafo
        self.custo_total = 0.0
        self.tabu = []
        self.feronomio_delta = []
        self.permitido = [i for i in range(grafo.rank)]
        self.eta = [[
            0 if i == j else 1 / grafo.matriz[i][j] for j in range(grafo.rank)
        ] for i in range(grafo.rank)]  # informações da heuristica
        inicio = random.randint(0, grafo.rank - 1)  # inicio aleatório
        self.tabu.append(inicio)
        self.atual = inicio
        self.permitido.remove(inicio)

    def _seleciona_proximo(self):
        denominador = 0
        for i in self.permitido:
            denominador += self.grafo.feronomio[
                self.atual][i]**self.colonia.alfa * self.eta[
                    self.atual][i]**self.colonia.beta
        probabilidades = [
            0 for i in range(self.grafo.rank)
        ]  # probabilidades de mover para um nó no próximo passo
        for i in range(self.grafo.rank):
            try:
                self.permitido.index(i)  # test if permitido list contains i
                probabilidades[i] = self.grafo.feronomio[self.atual][i] ** self.colonia.alfa * \
                    self.eta[self.atual][i] ** self.colonia.beta / denominador
            except ValueError:
                pass  # do nothing
        # seleciona proximo node by probabilidade roulette
        selecionado = 0
        rand = random.random()
        for i, probabilidade in enumerate(probabilidades):
            rand -= probabilidade
            if rand <= 0:
                selecionado = i
                break
        self.permitido.remove(selecionado)
        self.tabu.append(selecionado)
        self.custo_total += self.grafo.matriz[self.atual][selecionado]
        self.atual = selecionado

    def _atualiza_feronomio_delta(self):
        self.feronomio_delta = [[0 for j in range(self.grafo.rank)]
                                for i in range(self.grafo.rank)]
        for _ in range(1, len(self.tabu)):
            i = self.tabu[_ - 1]
            j = self.tabu[_]
            self.feronomio_delta[i][j] = self.colonia.Q / self.custo_total
