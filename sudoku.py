##------------------------------------------------------------------------------##
##-----------------------------TRABALHO 01 - SUDOKU-----------------------------##
##------------------------------------------------------------------------------##
## Aluno 01: Igor Wagner Dutra Leandro          Matrícula: 0026496
## Aluno 02: Felipe Costa                       Matrícula: 0049539
##------------------------------------------------------------------------------##

import os

def e_valido(tabuleiro, linha, coluna, num):
    # Verifica se é seguro colocar o número 'num' na posição (linha, coluna)
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False

    # Verifica a submatriz 3x3
    inicio_linha, inicio_coluna = 3 * (linha // 3), 3 * (coluna // 3)
    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == num:
                return False

    return True

def resolver_sudoku(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if e_valido(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num

                        if resolver_sudoku(tabuleiro):
                            return True

                        tabuleiro[linha][coluna] = 0  # Retroceder (backtrack)

                return False  # Nenhuma solução válida encontrada

    return True

def imprimir_sudoku(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))

def ler_sudoku_de_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    tabuleiro_sudoku = [[int(num) for num in linha.split()] for linha in linhas]
    return tabuleiro_sudoku

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    nome_arquivo_entrada = dir_path + "/sudoku_input.txt"  # Diretorio atual concatenado com Nome do arquivo de entrada
    tabuleiro_sudoku = ler_sudoku_de_arquivo(nome_arquivo_entrada)

    if resolver_sudoku(tabuleiro_sudoku):
        print("Solução do Sudoku:")
        imprimir_sudoku(tabuleiro_sudoku)
    else:
        print("Não foi possível encontrar uma solução válida para o Sudoku.")
