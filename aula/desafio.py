'''
1|2|3
4|5|6
7|8|9

crie uma função que rotacione a matriz em 90 graus(NxN)

7|4|1
8|5|2
9|6|3
'''
def criar_matriz(quant_linhas, quant_colunas):
    matriz = [[0 for i in range(quant_colunas)]for j in range(quant_linhas)]

    for li in range(quant_linhas):
       for c in range(quant_colunas):
          matriz[li][c] = int(input(f'Digite o valor para [{li},{c}]: '))

    return matriz

def imprimir_matriz(matriz):
    print('-=' * 30)
    for linha in matriz:
      for valor in linha:
         print(f'[{valor:^5}]', end='')
      print()
    print('-=' * 30)

quant_linhas = int(input("Qual o número de linhas? "))
quant_colunas = int(input("Qual o número de colunas? "))
        
matriz = criar_matriz(quant_linhas, quant_colunas)

imprimir_matriz(matriz)
if quant_colunas == quant_linhas:
    resposta = input("Você deseja rotacinar a matriz? responda apenas com 'sim' ou 'não'")
    if resposta.lower() == 'sim':
        def rotacionar_matriz_90(matriz):
            matriz_transposta = [list(row) for row in zip(*matriz)]
            for linha in matriz_transposta:
                linha.reverse()
            return matriz_transposta

        matriz_rotacinada = rotacionar_matriz_90(matriz)

        imprimir_matriz(matriz_rotacinada)
    else:
        print("ok")