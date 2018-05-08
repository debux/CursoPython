# aula10
#tempo = int(input('Quantos anos tem seu carro?'))
#if tempo<=3:
#    print('Carro novo')
#else:
#    print('Carro velho')
#print('--FIM--')

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Renan':
#    print('Quem nome bonito você tem!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia {}!'.format(nome))

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda: '))
#m = (n1+n2)/2
#if m<6:
#    print('A sua média de {:.1f}, não foi boa!'.format(m))
#else:
#    print('A sua média de {:.1f}, foi boa, parabéns!'.format(m))

# Desafio 28
#import random
#guess = int(input('De 0 a 5, tente adivinhar qual número será sorteado! '))
#num = random.randrange(5)
#if guess == num:
#    print('Parabéns você acertou!')
#else:
#    print('Puxa não foi dessa vez, o número sorteado foi: {}'.format(num))

# Desafio 29
#kms = float(input('Insira sua velocidade atual: '))
#vel = float(80)
##multa = (kms - vel)
#if kms <=80:
#    print('OK, você está dentro do limite da via!')
#else:
#    print('Você foi multado por trafegar acima do limite (80km) permitido!')
#    print('A multa pela infração é de: {}'.format((kms-vel) * 7,00))

# Desafio 30
#num = int(input('Insira um número: '))
#if num%2 == 0:
#    print('O número escolhido é PAR!')
#else:
#    print('O número escolhido é ÍMPAR!')

# Desafio 31
#km = int(input('Insira em kilometros a distancia da viagem: '))
#pass200 = (0.50 * km)
#passmore = (0.45 * km)
#if km <= 200:
#    print('O valor da passagem é: {0:,.2f}'.format(pass200))
#else:
#    print('O valor da passage, é: {0:,.2f}'.format(passmore))

# Desafio 32
#Modo simples:
#from datetime import date
#ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
#if ano == 0:
#    ano = date.today().year
#if ano%4 == 0 and ano%100 !=0 or ano%400 ==0:
#    print('O ano {} é Bissexto'.format(ano))
#else:
#    print('O ano {} não é Bissexto'.format(ano))

#modo complexo
#import calendar
#ano = int(input('Insira o ano: '))
#if calendar.isleap(ano) == True:
#    print('O ano {} é Bissexto')
#else:
#    print('Ano não Bissexto')

# Desafio 33
#num1 = int(input('insira o primeiro número: '))
#num2 = int(input('insira o segundo número: '))
#num3 = int(input('insira o terceiro número: '))
#menor = num1
#if num2 < num1 and num2 < num3:
#    menor = num2
#if num3 < num1 and num3 < num2:
#    menor = num3
#print('O menor valor digitado foi {}'.format(menor))
#maior = num1
#if num2 > num1 and num2 > num3:
#    menor = num2
#if num3 > num1 and num3 > num2:
#    maior = num3
#print('O maior valor digitado foi {}'.format(maior))

# Desafio 34
#sal = int(input('Insira seu salário: '))
#if sal >= 1250:
#    print('Você terá um aumento de 10%, ficando em R${:.2f}:'.format(sal+sal*10/100))
#else:
#    print('Você terá um aumento de 15%, ficando em R${:.2f}:'.format(sal+sal*15/100))

# Desafio 35
#c1 = int(input('Insira o comprimento da primeira reta: '))
#c2 = int(input('Insira o comprimento da segunda reta: '))
#c3 = int(input('Insira o comprimento da terceira reta: '))
#if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
#    print('Com os comprimentos apresentados, é possível criar um triangulo!')
#else:
#    print('Infelizmente com os comprimentos apresentados não é possível criar um triangulo!')