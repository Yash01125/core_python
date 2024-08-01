class A:
    def geta(s,a):
        s.a=a
    def puta(s):
        print('A : ',s.a)
class B:
    def getb(s,b):
        s.b=b

    def putb(s):
        print('B : ',s.b)

class C(A,B):
    def getc(s,c):
        s.c=c

    def putc(s):
        print('c : ',s.c)

c1=C()
b1=B()
c1.geta(300)
c1.getb(100)
c1.getc(200)
c1.puta()
c1.putb()
c1.putc()

