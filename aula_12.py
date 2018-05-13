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
anos = int(input('Insira em quantos anos irá pagar: '))
prest = (val / (anos*12))
limit = ((sal * 30) / 100)
print('prestação: {%.2f} e limite: {:.3f}'.format(prest,limit))
#if prest <= limit:
#    print('O Valor da prestação mensal é de: {:.3f}'.format(prest))
#else:
#    #prest > limit:
#    print('O Valor da prestação mensal {:.3f} está acima do permitido: {:.3f}'.format(prest, limit))