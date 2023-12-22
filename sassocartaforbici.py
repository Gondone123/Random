from numpy import random
print('Benvenuto a Sasso-Carta-Forbici con Python! Sviluppato da Gond / Cosimo')
print('Inserisci il tuo nome:')
giocatore = input()
print('Prego ' + giocatore +', dovrai battere Python!')
variabili = ['sasso','carta','forbici']
p = random.choice(variabili)
while True:
    g = input('Sasso, carta o forbici? ')
    if g == p or g == 'Sasso' and p == 'sasso' or g == 'Carta' and p == 'carta' or g == 'Forbici' and p == 'forbici':
        print('Pareggio! Python aveva scelto ' + p + '!')
        break
    if g == 'sasso' and p == 'forbici' or g == 'Sasso' and p == 'forbici':
        print('Hai vinto! Python aveva scelto ' + p + '!')
        break
    if g == 'carta' and p == 'sasso' or g == 'Carta' and p == 'sasso':
        print('Hai vinto! Python aveva scelto ' + p + '!')
        break
    if g == 'forbici' and p == 'carta' or g == 'Forbici' and p == 'carta':
        print('Hai vinto! Python aveva scelto ' + p + '!')
        break
    if g == 'sasso' and p == 'carta' or g == 'Sasso' and p == 'carta':
        print('Che peccato, hai perso! Python aveva scelto ' + p + '!')
        break
    if g == 'carta' and p == 'forbici' or g == 'Carta' and p == 'forbici':
        print('Che peccato, hai perso! Python aveva scelto ' + p + '!')
        break
    if g == 'forbici' and p == 'sasso' or g == 'Forbici' and p == 'sasso':
        print('Che peccato, hai perso! Python aveva scelto ' + p + '!')
        break
    else:
        print('Non è valido, ritenta!')
print('Fine del gioco! È stato un piacere giocare con te, ' + giocatore + '!')