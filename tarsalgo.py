adatok=[]

with open("ajto.txt", "r") as f:
    for sor in f:
        adatok.append(sor.split())
print("2. feladat")
for i in adatok:
    if i[3]=="be":
        print("Az első belépő: ",i[2])
        break

for i in reversed(range(0,len(adatok))):
    if adatok[i][3]=="ki":
        print("Az utolsó kilépő: ", adatok[i][2])
        break
athaladasok=[]
for i in range(0,101):
    athaladasok.append(0)

szemaz=[]
for i in adatok:
    szemaz.append(int(i[2]))
    athaladasok[szemaz]=athaladasok[szemaz]+1


print(athaladasok)

