'''
crie uma função que recebe uma string por parâmetro e retorne o
tamanho máximo de uma subtring que não possui caracteres repetidos.

'abacdab' --> 4
'aweawaec' --> 4
'bbbb' --> 1
usar uma lista para armazenar e depois fazer com que ela limpe a si mesma
as letras iguais devem ser dadas em digitos númericos
'''

def tamanho_maximo(string):
   texto = input('insira um texto: ')
   texto.translate()
