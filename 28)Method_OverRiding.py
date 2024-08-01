class A:
    def show(self):
        print('A')

class B(A):

    def show(self):
        super().show()
        print('B')

class C(B):

    def show(self):
        super().show()
        print('C')


c1=C()
c1.show()
