num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: ', num)
print('Unidades: {} '.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))