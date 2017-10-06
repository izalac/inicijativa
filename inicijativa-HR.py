import os, sys
ime = []
inicijativa = []
napomena = []
runda = 0
def promjena(y, inicijativa):
    while True:
        try:
            inic = int(input("Nova inicijativa: "))
        except ValueError:
            continue
        else:
            if inic < inicijativa[y]:
                inicijativa[y] = inic
            break

print("Inicijativa 1.1HR (c) 2017 Ivan Žalac\n")
while True:
    try:
        n = int(input("Broj sudionika: "))
    except ValueError:
        continue
    else:
        break
for i in range (n):
    print("\nSudionik br. " + str(i+1))
    ime.append(input("Ime: "))
    napomena.append(" ")
    while True:
        try:
            inic = int(input("Inicijativa: "))
        except ValueError:
            continue
        else:
            inicijativa.append(inic)
            break

inicijativa, ime = (list(t) for t in zip(*reversed(sorted(zip(inicijativa, ime)))))
while 1:
    runda += 1
    i = 0
    print("\n\nRunda " + str(runda) + "\nNaredbe: (C)ekaj, (I)duća runda, (N)apomena, (U)kloni, (R)eset, (K)raj\nili samo pritisnite Enter za iduće po inicijativi.\n")
    while i < n:
        if inicijativa[i] == -256:
            upit="i"
        else:
            upit = input("Na redu je " + ime[i] + " (" + str(inicijativa[i]) + ") # " + napomena[i] + " # ")
        if upit.lower() == 'c':
            promjena(i, inicijativa)
            inicijativa, ime, napomena = (list(t) for t in zip(*reversed(sorted(zip(inicijativa, ime, napomena)))))
        elif upit.lower() == 'i':
            break
        elif upit.lower() == 'n':
            napomena[i] = input ("Napomena: ")
        elif upit.lower() == 'u':
            inicijativa[i] = -256
            inicijativa, ime, napomena = (list(t) for t in zip(*reversed(sorted(zip(inicijativa, ime, napomena)))))
        elif upit.lower() == 'r':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif upit.lower() == 'k':
            sys.exit()
        else:
            i += 1
