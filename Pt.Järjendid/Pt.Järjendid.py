from math import * 
from random import * 
#31/01/23
#3
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=round(max_arv/kogus,2)
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)




#2
slovo=["1", "2", "3", "4", "5", "6", "7", "8"]
osa1=[]
osa2=[]
if len(slovo)%2==0 and len(slovo)>=2:
    n=int(len(slovo)/2)
    for i in range(1, n+1): #1,...n
        osa1.append(slovo[i-1])
    for j in range(n+1,len(slovo)+1): #n+1,... len()
        osa2.append(slovo[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.reverse()
    print(osa2)
else:
    print("Viga")




#2
maakonnad=["Tln", "Narva", "K-Järve", "Ida-Virumaa", "Tartu", "Tartumaa", "Viljandi", "Pärnumaa"]
osa1=[]
osa2=[]
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1, n+1): #1,...n
        osa1.append(maakonnad[i-1])
    for j in range(n+1,len(maakonnad)+1): #n+1,... len()
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.reverse()
    print(osa2)
else:
    print("Viga")
 




#1
index=""
maakonnad=["Tln", "Narva", "K-Järve", "Ida-Virumaa", "Tartu", "Tartumaa", "Viljandi", "Pärnumaa", "Saaremaa"]
while True:
    try:
        index=int(input("Anna index: "))
        if index<99999 and index>10000:
            break
    except:
        print("Anna õige index!")
i=index//10000 #1,2,3,4,5,6,7,8,9
print(f"{index} on {maakonnad[i-1]}") #0,1,2,3,4,5,6,7,8
if i in [1,2,3]:
    print()
else:
    print("Kanna maski, ja andke koju :)")

