# -*- coding: utf-8 -*-

DIREITA = True
ESQUERDA = False
BLANK = "B"
TRASH = "#"
LEFT = "11"
RIGHT = "1"

from Fita import Fita

class MTU:
    def __init__ (self,entrada):
        contador = 0;
        # não pode começar com 000
        if(entrada[0:3] != "000"):
            print("Inicio Incorreto")

        if entrada[-3:] != "000":
            print("Final Incorreto")

        entradaTratada = entrada.split("000") # verifica 000
        if len(entradaTratada) != 4:
            print("Erro nos separadores [000]")

        self.transicoes = entradaTratada[1].split("00")  
        headTransicoes = list() # verifica determinismo

        for transicao in self.transicoes:
            #Transicao quintupla
            if(len(transicao.split("0")) != 5):
                print("Transicao com 0 errados: {}".format(transicao))
            #Transicao com 1's
            elementosTransicao = transicao.split("0")
            for elemento in elementosTransicao:
                for numero in elemento:
                    if numero != "1":
                        print("Transicao nao contem somente 1's")
            #Direcao
            direcao = elementosTransicao[4]
            if len(direcao) != 1 and len(direcao) != 2:
                print("Direcao desconhecida")
            #Palavra
            self.palavra = entradaTratada[2]
            letras = self.palavra.split("0")
            for letra in letras:
                if len(letra) > 3 and len(letra) < 1:
                    print ("Formato incorreto para a palavra")
            #Inicializando fitas
            self.fita1 = Fita("000" + entradaTratada[1] + "000")
            self.fita2 = Fita("1")
            self.fita3 = Fita(self.palavra)
            self.fita3.trocaTransicao(DIREITA, BLANK)

    #Retorna fitas 
    def __str__(self):
        retorno  = "Fita 1: \n" + self.fita1.__str__() + "\n\n" 
        retorno += "Fita 2: \n" +self.fita2.__str__() + "\n\n"
        retorno += "Fita 3: \n" +self.fita3.__str__()
        return retorno
            
    #Retorna estado atual    
    def estadoAtual(self): 
        estado = ""
        self.fita2.rebobinar()
        self.fita2.trocaTransicao(DIREITA, BLANK)
        while self.fita2.getSimbolo() != BLANK:
            estado += self.fita2.trocaTransicao(DIREITA, self.fita2.getSimbolo())
        return estado
            
    #Retorna o simbolo atual
    def simboloAtual(self):
        simbolo = ""
        voltar = 0
        while self.fita3.getSimbolo() != "0" and self.fita3.getSimbolo() != BLANK:
            simbolo += self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
            voltar += 1
        for i in range(voltar):
            self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())           
        return simbolo

    #Simula a transicao
    def simularTransicao(self):
        estadoAtual = self.estadoAtual()
        simboloAtual =  self.simboloAtual() 
        posicaoTransacao = self.fita1.fita.find("00" + estadoAtual + "0" + simboloAtual + "0") + 2
        if posicaoTransacao == 1:
            return True
        #pega a transicao
        self.fita1.rebobinar()
        while self.fita1.cabecote != posicaoTransacao:
            self.fita1.trocaTransicao(DIREITA, self.fita1.getSimbolo())
        transicao = ""
        while transicao[-2:] != "00":
            transicao += self.fita1.trocaTransicao(DIREITA, self.fita1.getSimbolo())
            posicaoTransacao += 1
        transicao = transicao[:-2]
        elementosTransicao = transicao.split("0")
        #muda MT de estado
        self.fita2.reiniciarFita(elementosTransicao[2])
        #Simula fita infinita
        if elementosTransicao[4] == RIGHT:
            cabecote = self.fita3.cabecote
            self.simboloDireita(self.fita3, "0")
            if cabecote == self.fita3.cabecote:
                while self.fita3.getSimbolo() != BLANK:
                    self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
                self.fita3.trocaTransicao(DIREITA, "0")
                self.fita3.trocaTransicao(DIREITA, "1")
                self.fita3.trocaTransicao(DIREITA, "1")
                self.fita3.trocaTransicao(DIREITA, "1")
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
            self.simboloEsquerda(self.fita3, "0")
        #Muda Simbolo
        if len(elementosTransicao[1]) > len(elementosTransicao[3]):
            #substitui "1" no "111" fazendo "1##"
            for i in elementosTransicao[2]:
                self.fita3.trocaTransicao(DIREITA, i)
            while self.fita3.getSimbolo() != "0":
                self.fita3.trocaTransicao(DIREITA, TRASH)
            #remove os lixos            
            while self.temLixoEsquerda(self.fita3):
                self.removerLixoAEsquerda(self.fita3)
            #cabeça de leitura escrita no mesmo lugar
            self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
            while self.fita3.getSimbolo() == "1":
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
            self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
        elif len(elementosTransicao[1]) < len(elementosTransicao[3]):
            #substitui crescendo a fita pra esquerda
            for i in range(len(elementosTransicao[3])):
                if self.fita3.getSimbolo() == "0":
                    self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
                    self.criarBlankDireita(self.fita3)
                    self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
                self.fita3.trocaTransicao(DIREITA, elementosTransicao[3][i])
            #retorna cabeça de leitura e escrita antes da edição 
            self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
            self.simboloEsquerda(self.fita3, "0")
        #move a cabeça de leitura e escrita
        testeBlank = self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
        if testeBlank == BLANK and elementosTransicao[4] == LEFT:
            raise Exception('Mt simlada foi quebrada')
        self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
        if elementosTransicao[4] == LEFT:
            self.simboloEsquerda(self.fita3, "0")
        if elementosTransicao[4] == RIGHT:
            self.simboloDireita(self.fita3, "0")
        #não aceita
        return False

    #Move para direita
    def simboloDireita(self, fita, separador):
        while fita.getSimbolo() != separador and fita.getSimbolo() != BLANK:
            fita.trocaTransicao(DIREITA, fita.getSimbolo())
        if fita.getSimbolo() == BLANK:
            fita.trocaTransicao(ESQUERDA, fita.getSimbolo())
            self.simboloEsquerda(fita, "0")
        else:
            fita.trocaTransicao(DIREITA, fita.getSimbolo())  

    #Move para esquerda
    def simboloEsquerda(self, fita, separador):
        fita.trocaTransicao(ESQUERDA, fita.getSimbolo())
        if fita.getSimbolo() == BLANK:
            fita.trocaTransicao(DIREITA, fita.getSimbolo())
        else:    
            fita.trocaTransicao(ESQUERDA, fita.getSimbolo())
            while fita.getSimbolo() != separador and fita.getSimbolo() != BLANK:
                fita.trocaTransicao(ESQUERDA, fita.getSimbolo())
            fita.trocaTransicao(DIREITA, fita.getSimbolo())

    #Remove lixos (#) a esquerda
    def removerLixoAEsquerda(self, fita):
        inicio = fita.cabecote
        while fita.getSimbolo() != BLANK:
            if fita.getSimbolo() == "0":
                fita.trocaTransicao(ESQUERDA, TRASH)
                fita.trocaTransicao(DIREITA, "0")
                fita.trocaTransicao(DIREITA, TRASH)
            if fita.getSimbolo() == "1":
                fita.trocaTransicao(ESQUERDA, TRASH)
                fita.trocaTransicao(DIREITA, "1")
                fita.trocaTransicao(DIREITA, TRASH)
    
        fita.trocaTransicao(ESQUERDA, BLANK)
        fita.trocaTransicao(ESQUERDA, BLANK)
        fita.rebobinar()
        
        while fita.cabecote != inicio:
            fita.trocaTransicao(DIREITA, fita.getSimbolo() )
        fita.trocaTransicao(ESQUERDA, fita.getSimbolo())

    def imprimeTratado(self):
        estado = -1;
        self.fita2.rebobinar()
        self.fita2.trocaTransicao(DIREITA, self.fita2.getSimbolo())
        while self.fita2.getSimbolo() != BLANK:
            estado += 1
            self.fita2.trocaTransicao(DIREITA, self.fita2.getSimbolo())
        self.fita2.rebobinar()
        print("Estado q{}: ".format(str(estado)))

        #jump e cabecote
        fita = ""
        cabecoteInicial = self.fita3.cabecote
        jump = cabecoteInicial
        while self.fita3.getSimbolo() != BLANK:
            simbolo = 0
            while self.fita3.getSimbolo() != "0" and self.fita3.getSimbolo() != BLANK:
                simbolo += 1
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
            jump -= simbolo
            if self.fita3.getSimbolo() != BLANK:
                self.fita3.trocaTransicao(ESQUERDA, self.fita3.getSimbolo())
        for i in range(jump):
            fita += " "
        fita += "v" + "\n"

        # fita
        self.fita3.rebobinar()
        self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
        dicionario = {1:"a", 2:"b", 3:"B"}
        while self.fita3.getSimbolo() != BLANK:
            simbolo = 0
            while self.fita3.getSimbolo() != "0" and self.fita3.getSimbolo() != BLANK:
                simbolo += 1
                self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
            fita += dicionario[simbolo]
            self.fita3.trocaTransicao(DIREITA, self.fita3.getSimbolo())
        print(fita)
        self.fita3.cabecote = cabecoteInicial 