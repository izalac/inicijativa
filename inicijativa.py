ime = []
inicijativa = []
runda = 0
print("Inicijativa 1.0 (c) 2017 Ivan Žalac\nCC BY 4.0 - https://creativecommons.org/licenses/by/4.0/\n")
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
    runda+=1;
    print("\n\nRunda ", runda)
    for i in range(0,n):
        print("Na redu je " + ime[i] + " (" + str(inicijativa[i]) + ")")
        input("Enter za nastavak, ctrl+c za prekid...")
