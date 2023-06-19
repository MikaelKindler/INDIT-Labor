import random

try:
    Zahl1 = int(input("Gib die erste Zahl ein: "))
    Zahl2 = int(input("Gib die zweite Zahl ein: "))
    Ergebnis = Zahl1/Zahl2
    print("das Ergbenis ist:",Ergebnis)
except ValueError:
     print("ungültige Eingabe! Bitte gib eine ganze Zahl ein.")
except ZeroDivisionError:
    print("Fehler! Division durch Null ist nicht erlaubt.")
except Exception as e:
    print("Ein unbekannter Fehler istt aufgetreten:", str(e))
    
    





