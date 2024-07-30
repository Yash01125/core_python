n=int(input("Enter N:"))
l=[]
for i in range(1,n+1):
    if i%2!=0:
        for t in range(3,int(i/2)+1,2):
            if i%t==0:
                break
        else:
            l.append(i)
print(l)