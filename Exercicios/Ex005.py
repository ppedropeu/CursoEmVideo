"""Este programa deve ler um número inteiro e mostrar na seta o seu sucessor e o seu antecessor"""
n1= int(input('Digite um número: '))
sucessor = n1 + 1
antecessor = n1 - 1
print('O seu número é {}, o seu antecessor é {} e o seu sucessor é {}!'. format(n1, antecessor, sucessor))