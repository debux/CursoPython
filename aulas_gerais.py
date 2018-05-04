#nome = input('Qual o seu nome? ')
#if nome == "Renan":
#    print('Olá, parceiro!')
#else:
#    print('Fala brother!')

#dia = int(input('Qual o dia de seu aniversário?'))
#mes = input('Qual o mês de seu aniversário?')
#ano = input('Qual o ano de seu aniversário?')
#print('Você nasceu em: ',dia,'/',mes,'/',ano)

#num1 = int(input('Insira o primeiro número da soma: '))
#num2 = int(input('Insira o segundo número da soma: '))
#total = num1 + num2
##print('A soma entre ', n1, 'e', n2, 'vale:', s) python2
##print('A soma entre {0} e {1} é: {2}'.format(num1, num2, total)) python3
#print('A soma entre {} e {} é: {}'.format(num1, num2, total))

#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

#n1 = int(input('Insira um número: '))
#n2 = int(input('Outro valor: '))
#print('A soma \n é: {:.3f}'.format(n1/n2))

#num1 = int(input('Insira um número: '))
#print('O número inserido foi: {}'.format(num1))
#print('O número anterior é: {}'.format(num1-1))
#print('O número posterior é: {}'.format(num1+1))

#num = int(input('Insira um número: '))
#raiz = num**(1/2)
#print('O número informado é: {}'.format(num))
#print('O dobro de {0} é: {1} '.format(num, num*2))
#print('O triplo de {0} é: {1}'.format(num, num*3))
#print('A raiz de {0} é: {1}'.format(num, raiz))

#num1 = int(input('Insira sua nota do primeiro semestre: '))
#num2 = int(input('Insira a sua nota do segundo semestre: '))
#print('A sua média do ano é {0}'.format((num1+num2)/2))

#8
#mts = int(input('Insira o tamanho da parede em metros: '))
#print('O tamanho da parede em centimetros é: {}'.format(mts*100))
#print('O tamanho da parede de milimetros é: {0}'.format(mts*1000))

#9
#tabuada = int(input('Insira o número que você quer a tabuada: '))
#print('{0} x 1 = {1}'.format(tabuada, tabuada*1))
#print('{0} x 2 = {1}'.format(tabuada, tabuada*2))
#print('{0} x 3 = {1}'.format(tabuada, tabuada*3))
#print('{0} x 4 = {1}'.format(tabuada, tabuada*4))
#print('{0} x 5 = {1}'.format(tabuada, tabuada*5))
#print('{0} x 6 = {1}'.format(tabuada, tabuada*6))
#print('{0} x 7 = {1}'.format(tabuada, tabuada*7))
#print('{0} x 8 = {1}'.format(tabuada, tabuada*8))
#print('{0} x 9 = {1}'.format(tabuada, tabuada*9))
#print('{0} x 10 = {1}'.format(tabuada, tabuada*10))

#10
#wallet = int(input('Quantos reais você tem na carteira? '))
#dollar = 3.27
#print('Você tem o equivalente a {:.2f} dolares!!!'.format(wallet/dollar))

#11
#larg = float(input('Qual é a largura da parede que será pintada? '))
#alt = float(input('Qual a altura da parede que será pintada? '))
#area = larg*alt
#print('A quantidade de tinta necessaria em litros é: {}'.format(area/2))

#12
#valor = float(input('Insira o valor do produto: '))
#desc = valor*0.05
#print('O valor do produto com 5% de desconto é {:.2f}'.format(valor-desc))

#13
#salario = float(input('Entre com seu salário: '))
#aumento = salario*0.15
#print('Seu novo salário é: {:.2f}'.format(salario+aumento))

# aula09
#frase = 'Curso em Video Python'
#print(frase[::14])
#print(frase[1:14:2])
#print(frase.count('o'))
#print(frase.upper().count('N'))
#print(frase.__len__())
#print(frase.strip())
#print(len(frase))
#print(frase.replace('Python', 'Android'))
#print(frase.lower().find('video'))


#
#from math import sqrt, ceil
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
## raiz de 29 é 5.385164807134504. Ceil arredonda para cima.

#import random
#num = random.random()
#num = random.randint(1, 10)
#print(num)

#import emoji
#print(emoji.emojize('Python é :smile:', use_aliases=True))

#import math
#num = float(input('Insira o número: '))
#print('O número Real de {} é: {}'.format(num, math.trunc(num)))

# 17
#from math import hypot
#octO = float(input('Insira o comprimento do octeto oposto: '))
#octA = float(input('Insira o comprimento do octeto adjacentr: '))
##hipsa = (octO ** 2 + octA ** 2) ** (1/2)
#hipsa = math.hypot(octO,octA)
#print('O comprimento da hipotenusa é: {:.2f}'.format(hipsa))

# 18
#from math import radians, sin, cos, tan
#angulo = float(input('Entre com o angulo desejado: '))
#sen = sin(radians(angulo))
#cos = cos(radians(angulo))
#tan = tan(radians(angulo))
#print('O angulo de {} tem o seno de {:.2f}'.format(angulo, sen))
#print('O angulo de {} tem o coseno de {:.2f}'.format(angulo, cos))
#print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tan))

# 19
#from _random import choice
#nome01 = str(input('Nome do aluno 01: '))
#nome02 = str(input('Nome do aluno 02: '))
#nome03 = str(input('Nome do aluno 03: '))
#nome04 = str(input('Nome do aluno 04: '))

#lista = [nome01, nome02, nome03, nome04]
#sorteado = random.choice(lista)
#print('O aluno sorteado foi: {}'.format(sorteado))

# 20
#import random
#nome01 = str(input('Nome do aluno 01: '))
#nome02 = str(input('Nome do aluno 02: '))
#nome03 = str(input('Nome do aluno 03: '))
#nome04 = str(input('Nome do aluno 04: '))

#lista = [nome01, nome02, nome03, nome04]
#random.shuffle(lista)
# #print('A ordem de apresentação será: \n{}'.format(lista))

# 21
#import pygame
#pygame.init()
#pygame.mixer.music.load('musica.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

# 22

# aula10
tempo = int(input('Quantos anos tem seu carro?'))
if tempo<=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')