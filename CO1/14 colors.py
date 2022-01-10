c1=['red','blue','yellow']
c2=['green','blue']
print(c1)
print(c2)
for i in range(len(c1)):
    if c1[i] not in c2:
        print("the colour is:",c1[i])