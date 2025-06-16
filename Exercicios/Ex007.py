"""Este programa deve ler duas notas de um aluno, calcular e mostrar sua média"""
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
soma = nota1 + nota2
media = (nota1 + nota2) / 2
print('A sua 1ª nota é {}, sua 2ª nota é {}, a soma delas é {} e a sua média é {}'.format(nota1, nota2, soma, media))
