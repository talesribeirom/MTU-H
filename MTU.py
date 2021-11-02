# -*- coding: utf-8 -*-


class MTU:
    def __init__ (self,entrada):
        contador = 0;
        # não pode começar com 000
        if(entrada[0:3] != "000"):
            print("Inicio Incorreto")

        entradaTratada = entrada.split("000") #criterio de parada, verifica 000
        if len(entradaTratada) != 4:
            print("Erro nos separadores [000]")