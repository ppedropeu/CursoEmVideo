""" Este programa deve ler algo inputado, mostrar na tela o seu tipo primitivo e todas as informações possíveis sobre ela"""

a = (input('Digite algo: '))
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabeto?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculo?', a.isupper())
print('Está em minusculo?', a.islower())
