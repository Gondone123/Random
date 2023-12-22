import random
import time

print("Benvenuto su 'Sopravvivi a Marte', by Cosimo/Gond!")
distanza = 0
print("Inserisci il tuo nome: ")
giocatore = input()
time.sleep(2)
print(giocatore + " inizia il suo viaggio su Marte dopo essere atterrato d'emergenza. Deve percorrere 2000 m per essere salvato, ma non sarà facile...")
print("------------------------")

while distanza < 2000: 
    time.sleep(4)
    eventi = ["Tempesta di sabbia! Riuscirà " + giocatore + " a sopravvivere?", "Radiazioni cosmiche! Presto, " + giocatore + " deve trovare riparo!", "Malfunzionamento della tuta spaziale! " + giocatore + " deve ripararla!"]
    probabilità = random.randint(1, 10)
    eventoscelto = random.choice(eventi)
    print(eventoscelto)
    time.sleep(10)
    if probabilità > 3:
        if eventoscelto == eventi[0]:
            print("Tempesta superata!")
        if eventoscelto == eventi[1]:
            print(giocatore + " si è riparato in una caverna e ha superato il pericolo!")
        if eventoscelto == eventi[2]:
            print(giocatore + " ha riparato la tuta spaziale con successo e può proseguire!")
        distanza = min(distanza + random.randint(1, 200), 2000)
        distanza = str(distanza)
        print("Distanza percorsa: " + distanza + " m")
        print("------------------------")
        distanza = int(distanza)
    else:
        distanza = str(distanza)
        if eventoscelto == eventi[0]:
            print(giocatore + " è stato travolto nella tempesta e la sabbia si è infiltrata nella sua tuta spaziale, uccidendolo.")
        if eventoscelto == eventi[1]:
            print("Le dannose radiazioni cosmiche hanno letteralmentre fritto il povero " + giocatore + "!")
        if eventoscelto == eventi[2]:
            print("Il malfunzionamento della tuta ha portato alla perdita di tutto l'ossigeno disponibile, uccidendo " + giocatore + ".")
        print("Risultato: " + distanza + " m")
        break

    if distanza == 2000:
        time.sleep(3)
        print("Congratulazioni, sei stato salvato!")
        SystemExit()





