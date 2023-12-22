from numpy import random

print('Benvenuto a Il Caso, by Cosimo / Gond')
lista = ['No', 'Sì', 'Forse']
while True:
    print('Inserire una domanda:')
    input()
    print(random.choice(lista))
    print()
    print()