from ast import While
from numpy import random
print('Benvenuto a "Indovina il Numero", developed by Gond')
print('Ciao giocatore! Come ti chiami?')
nome_giocatore = input()
print('Buona fortuna ' + nome_giocatore + '!')
n = random.randint(1, 10)
print('Indovina il numero, da 1 a 10')
while(True):
    n2 = int(input())
    if n2 > n:
        print('Più basso!')
    if n2 < n:
        print('Più grande!')
    if n2 == n:
        print('Esatto! Hai vinto, ' + nome_giocatore + '!')
        break
print('Fine del gioco.')
