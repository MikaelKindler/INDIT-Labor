import random


#Erstellen Sie ein Python-Programm, das per Zufall einen oder mehrere Lotto (6 aus 45)-Tipp(s) erstellt.
# Die Anzahl der Tipps soll bei Start des Programmes frei wählbar sein.

anzahlDerTipps = int(input("Wieviele Tipps möchten Sie machen? "))

# Tipps wiederholen
while anzahlDerTipps >= 1:
    tippschein = [] # Leeren tippschein anlegen

    anzahlZahlenProTipp = 6 # Anzahl der Zahlen festlegen

    # Tippschein befüllen (mit 6 Zahlen)
    while anzahlZahlenProTipp >= 1:
        number = random.randint(1, 45) # Zufallszahl bestimmen
        if number not in tippschein: #überprüfen ob die Zahl schon im Schein ist
            tippschein.append(number) # wenn die Zahl nicht vorkommt wird sie in den Schein mitaufgenommen
            anzahlZahlenProTipp = anzahlZahlenProTipp - 1 # Counter um 1 reduzieren
    tippschein.sort() # Tippschein aufsteigend sortieren
    print(tippschein) # Einen Tippschein ausgeben
    anzahlDerTipps = anzahlDerTipps - 1



