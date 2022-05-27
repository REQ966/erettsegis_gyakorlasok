epizod={}
adatok=[]
epizodok=[]

with open("lista.txt", "r") as f:
    for i in f:
        adatok.append(i.strip())
        if len(adatok)==5:
            epizod["datum"] =adatok[0]
            epizod["nev"] =adatok[1]
            epizod["resz"] =adatok[2]
            epizod["hossz"] =int(adatok[3])
            if  adatok[4]=="1":
                epizod["latta"]=True
            else:
                epizod["latta"]=False
            epizodok.append(epizod)
            adatok=[]
            epizod={}

print(epizodok)
db=0
print("2. feladat")

for epizod in epizodok:
    if "NI" not in epizod["datum"]:
        db+=1
print("A listában ",db, "db vetítési dátummal rendelkező epizód van.")
db=0
for epizod in epizodok:
    if epizod["latta"]==True:
        db+=1
print("3. feladat ")

print("A listában lévő epizódok ", round(100/len(epizodok)*db,2),"%-át látta. ")

print("4. feladat ")
ido=0
for epizod in epizodok:
    ido+=epizod["hossz"]
nap=(ido/60)/24
print(nap)

print("5. feladat ")
datum=input("Adjon meg egy dátumot! Dátum= ")

for epizod in epizodok:
    if epizod["datum"]<=datum and epizod["latta"]==False:
        print(epizod["resz"],"  ",epizod["nev"])

def hetnapja(ev, ho, nap) :
     napok = ("v", "h", "k", "sze","cs", "p", "szo")
     honapok = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
     if ho < 3:
         ev = ev -1
     hetnapja == napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
     return hetnapja
print("7. feladat")
napja=input("Adja meg a hét egy napját (például cs)! Nap= ")
aznapi=set()
for epizod in epizodok:
    if "NI" not in epizod["datum"]:
        epizod_datum=epizod["datum"].split(".")
        epizod_napja=hetnapja(int(epizod_datum[0]),int(epizod_datum[1]),int(epizod_datum[2]))
    if napja==epizod_napja:
        aznapi.add(epizod["nev"])
if len(aznapi):
    for elem in aznapi:
        print(elem)
else:
    print("Az adott napon nem kerül adásba sorozat.")

