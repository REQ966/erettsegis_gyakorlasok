adatok=[]

with open("autok.txt", "r") as file:
    for sor in file:
        adatok.append(sor.rstrip("\n").split(" "))

print("2. feladat ")
for i in reversed(range(0,len(adatok))):
    if adatok[i][5]=="0":
        print( adatok[i][0]+". nap rendszám: "+ adatok[i][2])
        break

print("3. feladat")
nap=input("Nap: ")
print("Forgalom a(z) ", nap ,". napon: ")
for i in adatok:
    if i[0]==nap:
        if i[5]=="0":
            print(i[1]," ",i[2]," " ,i[3], "ki")
        elif i[5] == "1":
            print(i[1], " ", i[2], " ", i[3], "be")

print("4. feladat ")
db=0
db2=0
for i in adatok:
    if i[5]=="0":
        db2+=1
    elif i[5] == "1":
        db += 1

print("A hónap végén ", db2-db," autót nem hoztak vissza.")

print("5. feladat")

for x in range(0,10):
    kezdokm=-1
    vegkm=-1
    rsz="CEG30"+str(x)

    for i in adatok:
        db=i
        if rsz==db[2]:
            if kezdokm==-1:
                kezdokm=int(db[4])
            vegkm=int(db[4])
    print(rsz+" "+str(vegkm-kezdokm)+" km")

print("6. feladat")

print("7. feladat")

x=input("Rendszám: ")

with open(x+"_menetlevel.txt", "w") as file:
    for i in adatok:
        if x==i[2] and i[5]=="0":
            file.write(i[3]+"         "+i[0]+". "+i[1]+"         "+i[4]+" km")
            file.write("\n")

print("Menetlevél kész. ")




