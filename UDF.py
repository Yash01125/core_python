def oddeven(a):
    if a % 2 == 0:
        print(a,'even number')
    else:
        print(a,'odd number')
#------------------------------------------------------

def maxof2(a,b):
    if a > b:
        print(a,'greater than',b)
    else:
        print(b,'greater than',a)


#------------------------------------------------------
def maxof3(a,b,c):
    if a>b and a>c:
        print(a,'is max')
    elif b>a and b>c:
        print(b,'is max')
    else:
        print(c,'is max')
#------------------------------------------------------
def fibonaki(n):
    a, b, c = 0, 1, 2
    print(a, end=" ")
    while b < n:
        print(b, end=" ")
        a, b, c = b, c, a + b + c
#------------------------------------------------------
def prime(n):
    l = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            for t in range(3, int(i / 2) + 1, 2):
                if i % t == 0:
                    break
            else:
                l.append(i)
    print(l)

'''oddeven(59)
print('------------------------------------------------------')
maxof2(10,20)
print('------------------------------------------------------')
maxof3(10,20,30)
print('------------------------------------------------------')
fibonaki(n = int(input("Enter the number for fibonaki : ")))
print('------------------------------------------------------')
prime(n = int(input("Enter Number for prime:")))
'''