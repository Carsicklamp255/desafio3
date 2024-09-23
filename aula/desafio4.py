'''
crie uma função que recebe uma string por parâmetro e retorne o
tamanho máximo de uma subtring que não possui caracteres repetidos.

'abacdab' --> 4
'aweawaec' --> 4
'bbbb' --> 1

'''

def tamanho_maximo(string):
   texto = input('insira um texto: ')
   texto.translate()
