list=[2,4,5,15,18,19]
re=[]
print(list)
for i in list:
    if i%2!=0:
        re.append(i)
print("after removing even numbers:",re)