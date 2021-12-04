# -*- coding: utf-8 -*-

from MTU import MTU, DIREITA

class MTU_Heuristicas(MTU):
    def simulacao(self):
        self.verificaTransCrit()
        # verifica se existem loop para todos simbolos em alguma transicao
        q_erro = self.verificaErro()
        # verifica se o número de iterações ultrapassa o numero maximo de combinações 
        max_combinacoes = self.calcula_max_combinacoes()
        iteracoes = 0
        # executa a simulação
        while not self.simularTransicao():
            if self.verificaTransAtualCrit():
                return False
            if self.estadoAtual() == q_erro:
                return False
            iteracoes += 1
            if iteracoes >= max_combinacoes:
                return False
        return True

    #Retorna se para ou entra em loop
    def resultado(self):
        status = self.simulacao()
        if status:
            return "A MT simulada aceita w e para.\n"
        else:
            return "A MT entra em loop com a entrada w.\n"

    def verificaErro(self):
        NUM_SIMBOLOS = 3
        num_transicoes_estado = {}
        for transicao in self.transicoes:
            elementos = transicao.split("0")
            if elementos[0] == elementos[2]:
                if elementos[0] in num_transicoes_estado:
                    num_transicoes_estado[elementos[0]] += 1
                else:
                    num_transicoes_estado[elementos[0]] = 1
        for estado, num_transicoes in num_transicoes_estado.items():
            if num_transicoes >= NUM_SIMBOLOS:
                return estado

    def calcula_max_combinacoes(self):
        num_transicoes_mt = len(self.transicoes)
        tam_palavra = len(self.palavra.split('0'))
        num_simbolos = 3
        _max = num_transicoes_mt * tam_palavra * (num_simbolos ** tam_palavra)
        return _max


    def verificaTransCrit(self):
        self.transicoesCriticas = list()
        transicoes = self.fita1.fita.split("00")
        for transicao in self.transicoes:
            elementosTransicao = transicao.split("0")
            if elementosTransicao[1] == elementosTransicao[3]: #verifica se nao muda simbolo na primeira transicao
                for transicao2 in self.transicoes:
                    elementosTransicao2 = transicao2.split("0")
                    isCritico = elementosTransicao2[1] == elementosTransicao2[3]               #verifica se nao muda o simbolo na segunda transicao
                    isCritico = isCritico and elementosTransicao[0] == elementosTransicao2[2]  #verifica se a primeira esta apontando pra segunda
                    isCritico = isCritico and elementosTransicao[2] == elementosTransicao2[0]  #verifica se a segunda esta apontando pra primeira
                    isCritico = isCritico and elementosTransicao[4] != elementosTransicao2[4]  #direita esquerda ou esquerda direita
                    if isCritico:
                        self.transicoesCriticas.append(transicao)
    
    def verificaTransAtualCrit(self):
        estadoAtual = self.estadoAtual()
        simboloAtual =  self.simboloAtual() 
        posicaoTransicao = self.fita1.fita.find("00" + estadoAtual + "0" + simboloAtual + "0") + 2

        self.fita1.rebobinar()
        while self.fita1.cabecote != posicaoTransicao:
            self.fita1.trocaTransicao(DIREITA, self.fita1.getSimbolo())
        transacao = ""
        while transacao[-2:] != "00":
            transacao += self.fita1.trocaTransicao(DIREITA, self.fita1.getSimbolo())
            posicaoTransicao += 1
        transacao = transacao[:-2]
        for tc in self.transicoesCriticas:
            if tc == transacao:
                return True
        return False

    
