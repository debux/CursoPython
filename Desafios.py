# Desafio 02

#nome = str(input('Digite seu nome: '))
#print('{}{}{}, seja bem-vindo!'.format('\033[4;32m', nome , '\033[m'))

# Desafio 03

#v1 = int(input('Insira o primeiro valor da soma: '))
#v2 = int(input('Insira o segundo valor da soma: '))
#print('A soma entre {}{}{} e {}{}{} é: {}'.format('\033[1;34m', v1 , '\033[m','\033[4;35m', v2, '\033[m' , v1 + v2))

# Desafio 04
algo = input('Digite algo: ')
cor = {'vermelho':'\033[1;31;40m',
        'limpa':'\033[m'}
print('O tipo primitivo é: {}{}{}'.format(cor['vermelho'], type(algo), cor['limpa']))

# Desafio 05

