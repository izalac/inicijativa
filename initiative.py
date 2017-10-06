name = []
initiative = []
rnd = 0
print("Inicijativa 1.0 (c) 2017 Ivan Žalac\n")
while True:
    try:
        n = int(input("Number of entries: "))
    except ValueError:
        continue
    else:
        break

for i in range (n):
    print("\nEntry no. " + str(i+1))
    name.append(input("Name: "))
    while True:
        try:
            inic = int(input("Initiative: "))
        except ValueError:
            continue
        else:
            initiative.append(inic)
            break

initiative, name = (list(t) for t in zip(*reversed(sorted(zip(initiative, name)))))

while 1:
    rnd+=1;
    print("\n\nRound ", rnd)
    for i in range(0,n):
        print("Next: " + name[i] + " (" + str(initiative[i]) + ")")
        input("Press Enter to continue, Ctrl+C to break...")
