utasok=[]

with open("utasadat.txt") as f:
    for i in f:
        utasok.append(i.strip().split())
print("2. feladat ")
print("A buszra", len(utasok) ,"utas akart felszállni.")

print("3. feladat" )
db=0
for i in utasok:
    idopont=i[1].split("-")
    if idopont[0]>i[4] and i[3]!="NYP" and i[3]!="RVS" and i[3]!="GYK" and i[3]!="JGY":
        db+=1
    if i[4]=="0":
        db+=1


print("A buszra ",db ,"utas nem szállhatott fel. ")

print("4. feladat")
felszallok=[]
count=0
for x in range(0,30):
    for i in utasok:
        if int(i[0])==x:
            count+=1
    felszallok.append(count)
    count=0

maxi=int(felszallok[0])
index=-1
for i in felszallok:
    index+=1
    if maxi<i:
        maxi=i
        print("A legtöbb utas (",maxi, "fő) a ",index ,". megállóban próbált felszállni.")
        break
print("5. feladat" )
szamlalo=0
szamlalo2=0
for i in utasok:
    if i[3]=="NYP" or i[3]=="RVS" or i[3]=="GYK":
        szamlalo+=1
    if i[3]=="TAB" or i[3]=="NYB":
        szamlalo2+=1

print("Ingyenesen utazók száma:", szamlalo, "fő")
print("A kedvezményesen utazók száma:", szamlalo2, "fő")

def napokszama(e1, h1,n1, e2,h2,n2 ):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    n1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    n2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    napokszama= n2-n1
    return napokszama
lejar=[]
for i in utasok:
    datum=i[1].split("-")
    ev=int(datum[0][0:4])
    ho=int(datum[0][4:6])
    nap=int(datum[0][7:8])
    datum2 = i[4]
    ev2 = datum2[0:4]

    ho2 = datum2[4:6]

    nap2 =datum2[7:8]

    if (napokszama(ev,ho,nap,ev2,ho2,nap2))<=3:
        lejar.append(i[2])
        lejar.append(ev2)
        lejar.append("-")
        lejar.append(ho2)
        lejar.append("-")
        lejar.append(nap2)

print()








