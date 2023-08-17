print ("Rechner")
zahl1 = float (input ("Zahl 1: "))
operator = str (input ("Operator: "))
zahl2 = float (input ("Zahl 2: "))

if operator == '+':
    print (zahl1 + zahl2)
elif operator == '-':
    print (zahl1 - zahl2)
elif operator == '*':
    print (zahl1 * zahl2)
elif operator == '/':
    print (zahl1 / zahl2)
else:
    print ("Falsche Eingabe")



