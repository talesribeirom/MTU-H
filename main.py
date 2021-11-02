# -*- coding: utf-8 -*-

# Arquivo principal


import os
import os.path
import argparse


def leitura(arquivo):
    with open(arquivo) as arquivo:
        maquinaTuring = arquivo.read().replace('\n', '') # remove quebras de linha
        print('Testando para o arquivo: ' .format(arquivo.name))
        return maquinaTuring # retorna arquivo tratado


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
            print("arquivo_path = ", arquivo_path)
            mTuring = leitura(arquivo_path)
            print("chegou aqui, caminho: ", mTuring)
            #TODO Simulação em si. Busca de caminho funcional!
    #caminho padrao
    elif args.arquivo:
        mt = leitura(args.arquivo)
        print("args.arquivo = ", args.arquivo)
        #TODO Simulação em si. Busca de caminho funcional!

if __name__ == '__main__':
    main()