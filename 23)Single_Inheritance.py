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


b1=B()
b1.geta(10)
b1.getb(20)
b1.puta()
b1.putb()