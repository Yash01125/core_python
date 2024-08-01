class A:
    def geta(s,a):
        s.a=a
    def puta(s):
        print('A : ',s.a)
class B(A):
    def getb(s,b):
        s.b=b

    def putb(s):
        print('B : ',s.b)

class C(A):
    def getc(s,c):
        s.c=c

    def putc(s):
        print('C : ',s.c)

class D(B,C):
    def getd(s,d):
        s.d=d

    def putd(s):
        print('D : ',s.d)

d1=D()

d1.geta(1000)
d1.getb(100)
d1.getc(200)
d1.getd(300)
d1.puta()
d1.putb()
d1.putc()
d1.putd()


