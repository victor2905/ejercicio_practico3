print("**************************************")
print("Sistema para verificar el número mayor")
print("**************************************\n")
numero_uno = int(input("Defina el primer número: "))
numero_dos = int(input("Defina el segundo número: "))
numero_tres = int(input("Defina el tercer número: "))

if numero_uno > numero_dos and numero_uno > numero_tres:   
    print("Numero mayor es: ",numero_uno)
elif numero_dos > numero_tres:
    print("Numero mayor es: ",numero_dos)
else:
    print("Numero mayor es: ",numero_tres)

"""if numero_dos > numero_uno and numero_dos > numero_tres:
    print("Numero mayor es: ",numero_dos)
elif numero_uno > numero_tres:
    print("Numero mayor es: ",numero_uno)
else:
    print("Numero mayor es: ",numero_tres)

if numero_tres > numero_uno and numero_tres > numero_dos:
    print("Numero mayor es: ",numero_tres)
elif numero_uno > numero_dos:
    print("Numero mayor es: ",numero_uno)
else:
    print("Numero mayor es: ",numero_dos)"""


