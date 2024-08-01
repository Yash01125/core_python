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

class D(A):
    def getd(s,d):
        s.d=d

    def putd(s):
        print('D : ',s.d)


b1=B()
c1=C()
d1=D()

b1.geta(100)
b1.getb(200)
b1.puta()
b1.putb()

c1.geta(600)
c1.getc(700)
c1.puta()
c1.putc()

d1.geta(1000)
d1.getd(2000)
d1.puta()
d1.putd()
