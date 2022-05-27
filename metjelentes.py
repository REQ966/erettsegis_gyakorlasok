adatok=[]

with open("tavirathu13.txt", "r") as file:
    for sor in file:
        adatok.append(sor.rstrip("\n").split())
print(adatok)
print("2. feladat")

kod=str(input("Adja meg egy település kódját! Település: "))

for i in reversed(range(0,len(adatok))):
    if adatok[i][0]==kod:
        print("Az utolsó mérési adat a megadott településről "+adatok[i][1][0:2]+":"+adatok[i][1][2:4]+"-kor érkezett. ")
        break

print("3. feladat")
v1="30"
v2="0"


for i in range(0,len(adatok)):
    if adatok[i][3]<v1:
        v1=adatok[i][3]
    if adatok[i][3]>v2:
        v2=adatok[i][3]
for i in adatok:
    if i[3]==v1:
        print("A legalacsonyabb hőmérséklet:",i[0]  ,i[1][0:2]+":"+i[1][2:4], v1+" fok.")
        break
for i in adatok:
    if i[3]==v2:
        print("A legmagasabb hőmérséklet:",i[0]  ,i[1][0:2]+":"+i[1][2:4], v2+" fok.")
        break
