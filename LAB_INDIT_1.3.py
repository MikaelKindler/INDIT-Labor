# while [Bedinung]:
#    Anweisungen...
#if [Bedinung] :
Zahl1 = int(input("Gib Zahl ein:"))
while Zahl1==0:
    print("Erste zahl darf nicht 0 sein")
    Zahl1 = int(input("Gib erneut eine Zahl ein:"))
else:
    Zahl2 = int(input("Gib noch eine Zahl ein:"))
    print("Summe der Zahlen ist:", Zahl1 + Zahl2)
    print("Differenz der Zahlen ist:", Zahl1 - Zahl2)
    print("Multiplikation ist:", Zahl1  * Zahl2)