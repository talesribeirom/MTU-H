# -*- coding: utf-8 -*-

BLANK = "B" # constante para definir branco
DIR = 1 # direções
ESQ = 0

class Fita:
    def __init__(self,entrada):
        self.reiniciarFita(entrada)

    # zerar fita e reiniciar entrada
    def reiniciarFita(self,entrada):
        self.fita = BLANK + entrada
        self.cabecote = 0

    # define uma fita infinita
    def fitaInfinita(self,direcao):
        if(len(self.fita) == (self.cabeca+1) and direcao == DIR):
            self.fita += BLANK

    # Alteracoes na fita - instrucoes de transicao
    def trocaTransicao(self, direcao, simbulo):
    
        #Quebra a fita indo para ESQ no fim
        if self.cabecote == 0 and direcao == ESQ:
            raise Exception('Estouro na Fita')

        #Simulando Fita Infinita
        if len(self.fita) == (self.cabecote+1) and direcao == DIR:
            self.fita += BLANK
        
        #Salva simbolo anterior
        simbuloAnterior = self.fita[self.cabecote]
        
        #Troca de simbolos
        self.fita = self.fita[:self.cabecote] + simbulo + self.fita[(self.cabecote + 1):] 

        #Move cabecote
        if direcao == DIR: 
            self.cabecote += 1
        else: 
            self.cabecote -= 1
        return simbuloAnterior

    # Retorna simbolo onde cabecote aponta
    def getSimbolo (self):
        return self.fita[self.cabecote]

    # Escrita de fita
    def __str__(self):
        icone = "v"
        retorno = ""
        for i in range(self.cabecote):
            retorno += " "
        retorno += icone + "\n"
        return retorno + self.fita + BLANK

    def rebobinar(self):
        if self.fita[0] != BLANK:
            raise Exception('Fita estourada')
        self.cabecote = 0        