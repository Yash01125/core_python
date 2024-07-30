class a:
    def ll(s):
        print("class a")
class b(a):
    def ll2(s):
        print("class b")
class c(a):
    def ll3(s):
        print("class 3")
x=c()
x.ll()
x.ll2()
