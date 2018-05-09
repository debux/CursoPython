# aula 11 - Cores no terminal
# OBS: Para mais cores, necessário usar biblioteca (colorize).

# style:
#0 not change
#1 bold
#4 underline
#7 invert

# cor texto:
#30 branco
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 roxo
#36 azul claro
#37 cinza

# cor fundo:
#40 branco
#41 vermelho
#42 verde
#43 amarelo
#44 azul
#45 roxo
#46 azul claro
#47 cinza


# texo vermelho com fundo amarelo em negrito
print('\033[1;31;43mTestando!\033[m')

# texto amarelo com fundo azul e underline
print('\033[4;33;44mTestando!\033[m')

# texto roxo com fundo amarelo e negrito
print('\033[1;35;43mTestando!\033[m')

# texto branco com fundo verde
print('\033[30;42mTestando!\033[m')

# texto padrão
print('\033[mTestando!\033[m')

# inverte fundo com texto
print('\033[7;30mTestando!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Renan'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

# Desafio colorir o 10 desafios anteriores