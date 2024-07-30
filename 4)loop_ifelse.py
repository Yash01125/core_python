'''
print("if_else")

a=int(input("enter value A:"))
b=int(input("enter value B:"))

if a>b:
    print("a is grater than b")
else:
    print("b is grater than a")
-----------------------------------------    
a=int(input("enter value A:"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")
-----------------------------------------

a=int(input("enter value a:"))
b=int(input("enter value b:"))
c=int(input("enter value c:"))


if a>b:
    if a>c:
        print("a is max")
    else:
        print("b is max")
elif b>c:
    print("b is max")
else:
    print("c is max")

----------------------------------------

rno=int(input("Enter rno:"))
sname=input("Enter student name:")
s1=int(input("Enter marks of sub 1:"))
s2=int(input("Enter marks of sub 2:"))
s3=int(input("Enter marks of sub 3:"))

total=s1+s2+s3
per=total/3

print(per)

if per>=70:
    print("dist")
elif per>=60:
    print("first")
elif per>=50:
    print("second")
elif per>=40:
    print("pass")
else:
    print("fail")

----------------------------------------


print("for loops")

for i in range(10):
    print(i)
print("-----------------------------")

for i in range(3,10):
    print(i)
print("-----------------------------")

for i in range(1,10,2):
    print(i)
print("-----------------------------")

for i in range(10,-1,-1):
    print(i)
print("-----------------------------")

----------------------------------------- 

for i in range(1,10):
    print(" "*(9-i)," *"*i)

for i in range(9,0,-1):
    print(" "*(9-i)," *"*i)
    

j=1
for i in range(65,73):
    print(chr(i)*j)
    j=j+1
'''






