"""Este exercício deve ler um número e mostrar: o seu dobro, o seu triplo e raiz quadrada"""
n = int(input('Digite um número: '))
dobro = n *2
triplo = n * 3
raiz = n ** (1/2)
print('Seu número é: {}, o dobro dele é {}, o triplo dele é {} e araiz quadrada dele é {}!'.format(n, dobro, triplo, raiz))