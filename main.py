# -*- coding: utf-8 -*-

# Arquivo principal


import os
import os.path
import argparse

from Heuristicas import MTU_Heuristicas


def leitura(arquivo):
    with open(arquivo) as arquivo:
        maquinaTuring = arquivo.read().replace('\n', '') # remove quebras de linha
        print('Testando para o arquivo: {} '.format(arquivo.name))
        return maquinaTuring # retorna arquivo tratado

def simular(mt):
    uh = MTU_Heuristicas(mt)
    resultado = uh.resultado()
    print(resultado)

def main():
    # Constroi string de argumento de execução
    # Busca arquivo na pasta raiz, se não passado nome do arquivo como argumento busca 'test.txt' por padrao
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('arquivo', type=str, nargs='?', default='test.txt')
    parser.add_argument('-d', '--dir', type=str, nargs=1)
    args = parser.parse_args()

    #caminho fornecido
    if args.dir:
        arquivos = [arquivo for arquivo in os.listdir(args.dir[0])
                    if arquivo.endswith(".txt")]
        for arquivo in arquivos:
            arquivo_path = os.path.join(args[0], arquivo)
            mTuring = leitura(arquivo_path)
            simular(mTuring)
    #caminho padrao
    elif args.arquivo:
        mTuring = leitura(args.arquivo)
        simular(mTuring) 

if __name__ == '__main__':
    main()