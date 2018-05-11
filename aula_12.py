# aula 11

#nome = str(input('Qual é seu nome? '))
#if nome == 'Renan':
#    print('Tenha um bom dia, {}!'.format(nome))
#elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
#    print('Seu nome é bem popular no Brasil.!')
#elif nome in 'Ana Cláudia Jéssica Juliana':
#    print('Belo nome feminino.')
#else:
#    print('Seu nome é bem normal.')
#print('Tenha um bom dia!, {}'.format(nome))

# Desafio 36

val = float(input('Insira o valor da casa: '))
sal = float(input('Insira seu salário: '))
anos = int(input('Insira em quantos irá pagar: '))
prest = ((sal * anos) /100)
limit = (sal * 30) / 100)
if prest < limit:
    print('O Valor da prestação mensal é de: {:.3f}'.format(prest))
elif prest >= limit:
    print('O Valor da prestação mensal está acima do permitido {:.3f}'.format(limit))