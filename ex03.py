#Utilizando virgulas e .format{} para cocatenação
n1 = int (input('Digite um valor:'))
n2 = int (input('digite outro valor:'))
s = (n1 + n2)
#print('a soma entre', n1, 'e', n2, 'é igual a', s)
print('A soma ente {} e {} é igual a {}' .format(n1, n2, s))