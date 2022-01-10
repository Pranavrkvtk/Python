n=int(input("eneter the no of colours:"))
colors=[]
for i in range(n):
    a=input("enter the colour:")
    colors.append(a)
print(colors)
print("the first clour is:",colors[0])
print("the last colour is:",colors[-1])