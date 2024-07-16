a,b,c=0,1,2
n=int(input("Enter the number : "))
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b,c=b,c,a+b+c
