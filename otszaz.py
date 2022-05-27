penztar=[]
kosar={}
with open("penztar.txt") as file:
    for i in file:
        if i.strip() == "F":
            penztar.append(kosar)
            kosar={}
        else:
            if i.strip() not in kosar:
                kosar[i.strip()] = 1
            else:
                kosar[i.strip()] +=1


print("2. feladat")
print("A fizetések száma: ",len(penztar))

print("3. feladat")
print("Az első vásárló" ,len(penztar[0]), "darab árucikket vásárolt")

print("4. feladat ")
sorszam=int(input("Adja meg egy vásárlás sorszámát!"))
arucikk=input("Adja meg egy árucikk nevét!")
darabszam=int(input("Adja meg a vásárolt darabszámot!"))

print("5. feladat")
sor=0
for i in penztar:
    sor+=1
    if arucikk in i:
        print("Az első vásárlás sorszáma:", sor)
        break
sor=len(penztar)+1
for i in reversed(penztar):
    sor-=1
    if arucikk in i:
        print("Az utolsó vásárlás sorszáma:", sor)
        break
db=0
for i in penztar:
    if arucikk in i:
        db+=1

print(db ,"vásárlás során vettek belőle. ")

def ertek(darabszam):
    db=0
    ertek2=0
    while db<darabszam:
        ertek2+=500-50*db
        db+=1
    return ertek2


print("6. feladat")
print(darabszam,f'darab vételekor fizetendő: {ertek(darabszam)}')
print("7. feladat ")
for aru in penztar[sorszam-1]:
    print(f"{penztar[sorszam-1][aru]} {aru} ")
db=0

with open("osszeg.txt" , "w") as file2:
    for i in penztar:
        file.write(f"{penztar[i]} {ertek(len(penztar[i]))} ")

