bentlevok=[]

with open("ajto.txt")as file:
   for i in file:
       bentlevok.append(i.strip().split())
print(bentlevok)
print("2. feladat")
for i in bentlevok:
    if i[3]=="be":
        print("Az első belépő: ",i[2])
        break
for i in reversed(bentlevok):
    if i[3]=="ki":
        print("Az utolsó kilépő: ",i[2])
        break

id=[]
for i in bentlevok:
    if i[2] not in id:
        id.append(i[2])

hany=[]
id=sorted(id)
db=0
for x in id:
    hany.append(db)
    db=0
    for i in bentlevok:
        if x==i[2]:
            db=db+1
with open("athaladas.txt", "w")as file1:
    for i in range(0,len(hany)):
        file1.write(str(id[i]))
        file1.write(" ")
        file1.write(str(hany[i]))
        file1.write("\n")


print("4. feladat")
db=0
db2=0
bent=[]
for x in id:
    db=0
    db2=0
    for i in bentlevok:
        if x==i[2] and i[3]=="be":
            db=db+1
        if x==i[2] and i[3]=="ki":
            db2=db2+1
    if db!=db2:
        bent.append(x)

print("A végén a társalgóban voltak: ", bent)

print("5. feladat")
max=0
for i in bentlevok:
    if i[3]=="be":
        max=max+1
    if i[3]=="ki":
        max=max-1
max2=0
melyik="a"
for i in bentlevok:
    if i[3]=="be":
        max2=max2+1
    if i[3]=="ki":
        max2=max2-1
    elif max2==max+4:
        print("Például ", i[0]  ,":" ,i[1],"-kor voltak a legtöbben a társalgóban.")
        break

print("6. feladat")

azon=input("Adja meg a személy azonosítóját!")

print("7. feladat")


for i in bentlevok:
    if i[2]==azon and i[3]=="be":
        print(i[0],":",i[1],"-", end="")
    elif i[2]==azon and i[3]=="ki":
        print(i[0],":",i[1])
perc=0
perc2=0
ido=0
for i in bentlevok:
    if i[2] == azon and i[3] == "be":
        perc=int(i[1])

    if i[2] == azon and i[3] == "ki":
        perc2=int(i[1])
        ido+=perc2-perc

print(ido)


if azon in bent:
    print("\nA(z) " ,azon ,". személy összesen ",ido," percet volt bent, a megfigyelés végén a társalgóban volt." )
if azon not in bent:
    print("\nA(z) ",azon,". személy összesen ",ido," percet volt bent, a megfigyelés végén nem volt a társalgóban." )



