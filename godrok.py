godor=[]

with open("melyseg.txt", "r") as file:
    for i in file:
        godor.append(int(i.strip()))


print("1. feladat ")
print("A fájl adatainak száma:", len(godor) )

print("2. feladat ")
tavertek=int(input("Adjon meg egy távolságértéket! "))
print(f"Ezen a helyen a felszín", godor[tavertek]  ,"méter mélyen van. ")
print("3. feladat ")

db=0
for i in godor:
    if i==0:
        db+=1
maradek=db/len(godor)*100
print("Az érintetlen terület aránya ", round(maradek,2) , "%")
csakgodor=[]
godrocskek=[]

for i in range(1,len(godor)):
    if godor[i-1]==0 and godor[i]!=0:
        godrocskek.append(godor[i])
    if godor[i-1]!=0 and godor[i]!=0:
        godrocskek.append(godor[i])
    if godor[i-1]!=0 and godor[i]==0:
        csakgodor.append(godrocskek)
        godrocskek=[]

with open("godrok.txt.txt", "w") as f2:
    for i in csakgodor:
        f2.write(str(i))
        f2.write("\n")

print("5. feladat ")
print("A gödrök száma: ", len(csakgodor))
print("6. feladat ")
print("a)")
if godor[tavertek]==0:
    print("Az adott helyen nincs gödör.")

veg=0
i=tavertek
while godor[i]!=0:
    i+=1
veg=i

kezdo=0

i=tavertek
while godor[i]!=0:
    i-=1
kezdo=i+2

print("A gödör kezdete: " ,kezdo ," méter, a gödör vége: ",veg," méter." )

for i in range(kezdo,veg):
    if godor[i]<godor[i+1]:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")
