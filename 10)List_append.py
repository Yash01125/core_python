lst1=[1,3,2,4,55,567,8,3,356]
lst2=[]

#list even no using list elements
for i in lst1:
    if i %2==0:
        print("%d even"%i)
        lst2.append(i)
print(lst2)

