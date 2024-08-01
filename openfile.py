my_arq = open("teste.txt")

print(my_arq.read())
my_arq.seek(0)

for line in my_arq:
  print(line)

string = "Minha grama é verde, certo?"
string2 = "Teste de string"
inteiro = ['a','b','c']

#print(string[::-1])
#print(string[::2])
print (inteiro[1:])

#print('Saida: {}'.format(string2))
print('String: %s e Inteiro: %r' %(string2, inteiro))

a1 = 'One: {a}, Two: {c}, Three: {b}'.format(a=1, b='two', c=3.14)