ora={}
beosztas=[]
adat=[]

with open("beosztas.txt", "r") as f:
    for i in f:
        adat.append(i.strip())
        if len(adat)==4:
            ora["tanar"] = adat[0]
            ora["tantargy"] = adat[1]
            ora["osztaly"] = adat[2]
            ora["heti"] = int(adat[3])
            beosztas.append(ora)
            adat=[]
            ora={}

print(beosztas)
print("2. feladat ")
print("A fájlban ",len(beosztas) ,"bejegyzés van.")

print("3. feladat ")
summary=0
for ora in beosztas:
    summary+=ora["heti"]
print("Az iskolában a heti összóraszám: ", summary)

print("4. feladat ")
nev=input("Egy tanár neve=")
sum2=0
for ora in beosztas:
    if ora["tanar"]==nev:
        sum2+=ora["heti"]

print("A tanár heti óraszáma: ", sum2)
of=[]
for ora in beosztas:
    if ora["tantargy"]=="osztalyfonoki" and ora["tanar"] not in of:
        of.append(ora["osztaly"] + "-" +ora["tanar"])

with open("of.txt", "w") as f2:
    for i in of:
        f2.write(i)
        f2.write("\n")
print("6. feladat")
azon=input("Osztály= ")
tantargy=input("Tantárgy= ")
s=0
for ora in beosztas:
    oszt=ora["osztaly"].split(".")
    az=azon.split(".")
    if ora["tantargy"]==tantargy and oszt[0]==azon[0]:
        s+=1
if s<1:
    print("Csoportbontásban tanulják. ")

else:
    print("Osztályszinten tanulják.")


print("7. feladat ")
tanarok=[]
for ora in beosztas:
    if ora["tanar"] not in tanarok:
        tanarok.append(ora["tanar"])

print("Az iskolában", len(tanarok) ,"tanár tanít. ")