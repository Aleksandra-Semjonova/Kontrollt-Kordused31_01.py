#1
n=int(input())
for i in range(n):
    print(" /V\\n / V \\n / V V \\n /VV V VV\ ")
for j in range(1,9):
    for i in range(1,9):
        print(i,end="/V\\n / V \\n / V V \\n /VV V VV\ ")
    print()

#4
n= int(input("sisestage suur arv: "))
paaritu= 0 
veider= 0
for i in n: 
    if i % 2 == 0:
        paaritu += 1
    else:
        veider += 1
print(paaritu, veider)

#3
n = random.number(0,100)
print(n)
positivne=0
mitu=0
for i in range(n):
    randomNumber=random.number(-100,100)
    if randomNumber>0:
        positivne +=1
    mitu +=1
print("positivne: ", positivne)

#5
Summa=0
A=int(input("kirjutage number A: "))
B=int(input("kirjutage number B: "))
for i in range(A,B +1):
    Summa +=1
print(Summa)