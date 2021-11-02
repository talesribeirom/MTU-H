# -*- coding: utf-8 -*-

BLANK = "B" # constante para definir branco
DIR = 1 # direções
ESQ = 0

class Fita:
    def __init__(self,entrada):
        self.reiniciaFita(entrada)

    # zerar fita e reiniciar entrada
    def reiniciarFita(self,entrada):
        self.fita = BLANK + entrada
        self.cabeca = 0

    # define uma fita infinita
    def fitaInfinita(self,direcao):
        if(len(self.fita) == (self.cabeca+1) and direcao == DIR):
            self.fita += BLANK