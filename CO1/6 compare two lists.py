lista=[1,2,3,4,5]
listb=[2,4,6,8]
print("elements in list one is ", lista)
print("elements in list two are",listb)
s1=0
s2=0
if(len(lista)==len(listb)):
    print("list have same length")
else:
     print("list have different length")
for i in range(len(lista)):
    s1=s1+lista[i]
print("the sum of first list is",s1)
for i in range(len(listb)):
    s2=s2+listb[i]
print("the sum of list2 is",s2)
if(s1==s2):
    print("sum of lists is same")
else:
    print("the sum of lists is different")
print("the common element in list is:")
for i in lista:
    for j in listb:
        if i==j:
            print(i)