números = [[], []]
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
print('='*60)
números[0].sort()
números[1].sort()
print(f'Os valores pares digitados foram: {números[0]}')
print(f'Os valores ímpares digitados foram: {números[1]}')