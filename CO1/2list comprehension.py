li=[-5,8,10,-4,0,-8,20]
print(li)
newli=[x for x in li if x>0]
print("The positive numbers are:",newli)


n=int(input("Enter the number of numbers: "))
list=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    list.append(a)
print(list)
list1=[x**2 for x in list]
print(list1)

word=input("Enter a word")
vowels=[x for x in word if x in['a','e','i','o','u']]
print("The vowels in the words are:",vowels)


w=input("enter a word:")
ord=[ord(x) for x in w]
print("the ordinal value is:",ord)