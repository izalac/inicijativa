import os, sys
name = []
initiative = []
note = []
rnd = 0
def inchg(y, initiative):
    while True:
        try:
            inic = int(input("New initiative: "))
        except ValueError:
            continue
        else:
            if inic < initiative[y]:
                initiative[y] = inic
            break
            
print("Inicijativa 1.1EN (c) 2017 Ivan Žalac\n")
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
    note.append(" ")
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
    rnd += 1
    i = 0
    print("\n\nRound " + str(rnd) + "\nCommands: (D)elay, N(E)xt round, (N)ote, (R)emove, re(S)et, (Q)uit\nor just press Enter for next entry.\n")
    while i < n:
        if initiative[i] == -256:
            inp="e"
        else:
            inp = input("Next: " + name[i] + " (" + str(initiative[i]) + ") # " + note[i] + " # ")
        if inp.lower() == 'd':
            inchg(i, initiative)
            initiative, name, note = (list(t) for t in zip(*reversed(sorted(zip(initiative, name, note)))))
        elif inp.lower() == 'e':
            break
        elif inp.lower() == 'n':
            note[i] = input("Note: ")
        elif inp.lower() == 'r':
            initiative[i] = -256
            initiative, name, note = (list(t) for t in zip(*reversed(sorted(zip(initiative, name, note)))))
        elif inp.lower() == 's':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif inp.lower() == 'q':
            sys.exit()
        else:
            i += 1
