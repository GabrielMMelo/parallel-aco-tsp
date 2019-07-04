import random


class Grafo(object):
    def __init__(self, matriz_adjacencia, rank):
        self.matriz = matriz_adjacencia
        self.rank = rank
        self.feromonio = [[1 / (rank * rank) for j in range(rank)]
                          for i in range(rank)]  # m x m


class ACO(object):
    def __init__(self, cont_formiga, geracoes, alfa, beta, ro, Q=0.0):
        """
        Q -- intensidade do feromonio (default=0.0)
        ro -- taxa de evaporação
        beta -- influencia da visibilidade (proximidade entre os nohs)
        alfa -- influencia do feromonio
        cont_formiga -- m
        geracoes -- iterações do algoritmo
        """
        self.Q = Q
        self.ro = ro
        self.beta = beta
        self.alfa = alfa
        self.cont_formiga = cont_formiga
        self.geracoes = geracoes

    def _atualiza_feromonio(self, grafo, formigas):
        """Atualização dos feromônios globais (entre cada cidade)

        Keyword arguments:
        grafo -- instância de Grafo
        formigas -- vetor das formigas da colônia
        """
        for i, linha in enumerate(grafo.feromonio):
            for j, coluna in enumerate(linha):
                grafo.feromonio[i][j] *= self.ro  # evaporacao
                for formiga in formigas:  # TODO: Ponto interessante para paralelizar
                    grafo.feromonio[i][j] += formiga.feromonio_delta[i][j]

    def resolve(self, grafo):
        """Execução do ACO

        Keyword arguments:
        grafo -- instância de Grafo
        """
        melhor_custo = float('inf')
        melhor_solucao = []
        for gen in range(self.geracoes):
            formigas = [
                _Formiga(self, grafo) for i in range(self.cont_formiga)
            ]
            for formiga in formigas:
                for i in range(grafo.rank - 1):
                    formiga._seleciona_proximo()
                formiga.custo_total += grafo.matriz[formiga.tabu[-1]][  # retorno para cidade inicial
                    formiga.tabu[0]]
                if formiga.custo_total < melhor_custo:
                    melhor_custo = formiga.custo_total
                    melhor_solucao = [] + formiga.tabu
                formiga._atualiza_feromonio_delta()  # atualiza feromonio
            self._atualiza_feromonio(grafo, formigas)
        return melhor_solucao, melhor_custo


class _Formiga(object):
    def __init__(self, aco, grafo):
        """
        Keyword arguments:
        aco -- instância de ACO
        grafo -- instância de Grafo
        """
        self.colonia = aco
        self.grafo = grafo
        self.custo_total = 0.0  # Lk
        self.tabu = []  # caminho escolhido pela formiga em uma geração
        self.feromonio_delta = []  #deltaT^Kij
        self.permitido = [i for i in range(grafo.rank)]
        self.eta = [[  # 1/Lij
            0 if i == j else 1 / grafo.matriz[i][j] for j in range(grafo.rank)
        ] for i in range(grafo.rank)]
        inicio = random.randint(0, grafo.rank - 1)  # inicio aleatório
        self.tabu.append(inicio)
        self.atual = inicio
        self.permitido.remove(inicio)

    def _seleciona_proximo(self):
        """Seleciona próxima cidade de uma formiga através do cálculo das
        probabilidades de aceder cada uma das demais. Utiliza técnica de
        Roullete Wheel para selecionar.
        """
        denominador = 0
        for j in self.permitido:
            denominador += self.grafo.feromonio[
                self.atual][j]**self.colonia.alfa * self.eta[
                    self.atual][j]**self.colonia.beta
        probabilidades = [
            0 for i in range(self.grafo.rank)
        ]  # probabilidades de mover para uma cidade no próximo passo
        for i in range(self.grafo.rank):
            try:
                self.permitido.index(i)
                probabilidades[i] = self.grafo.feromonio[self.atual][i] ** self.colonia.alfa * \
                    self.eta[self.atual][i] ** self.colonia.beta / denominador
            except ValueError:
                pass   # descarta se a cidade nao for permitida

        # seleciona a proxima cidade usando a técnica de roulette wheel
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

    def _atualiza_feromonio_delta(self):
        """Atualiza os feromônios locais de uma formiga"""
        self.feromonio_delta = [[0 for j in range(self.grafo.rank)]  # zera deltaT^kij
                                for i in range(self.grafo.rank)]
        for _ in range(1, len(self.tabu)):
            i = self.tabu[_ - 1]
            j = self.tabu[_]
            self.feromonio_delta[i][j] = self.colonia.Q / self.custo_total
