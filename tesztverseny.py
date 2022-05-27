t=[]
with open("valaszok.txt", "r", ) as f:
    helyes = f.readline().strip()
    for egysor in f:
        versenyzo = egysor.strip().split()
        t.append(versenyzo)

print("1. feladat: Az adatok beolvasása")

print("2. feladat: A vetélkedőn", len(t), " versenyző indult. ")
id = "AB123" #input("3. feladat: A versenyző azonosítója = ")
valasz=""
print("3. feladat: A versenyző azonosítója = ",id)
for i in t:
    if i[0]==id:
        print(i[1], "  (a versenyző válasza)")
        y = valasz.replace("",i[1])

print("4. feladat: ")
print(helyes, " (a helyes megoldás)")

for i in range(0,len(helyes)):
    if helyes[i] == y[i]:
        print("+" ,end="")
    else:
        print(" ",end="")
print("  (a versenyző helyes válaszai)")
db=0

sorszam = int(input("5. feladat: A feladat sorszáma = "))
sorszam=sorszam-1

for i in t:
    if i[1][sorszam] == helyes[sorszam]:
        db+=1

print("A feladatra ", db ," fő, a versenyzők ",round(db/len(t)*100,2),"%-a adott helyes választ. ")

f2=open("pontok.txt", "w")
for i in t:
    for x in range(0,13):
        pontok=0
        while x<5:
            if i[1][x]==helyes[x]:
                pontok+=3
        while x<11:
            if i[1][x]==helyes[x]:
                pontok+=4
        while x<14:
            if i[1][x]==helyes[x]:
                pontok+=5
        while x==13:
            if i[1][x]==helyes[x]:
                pontok+=6
        f2.write(i[0] , " ", pontok)
        f2.close()


