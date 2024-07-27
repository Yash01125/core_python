# no arguments / no return value

def printline():
    print('*'*50)

printline()

# with argument / no return value

def add(a,b):
    print('Addition:',a+b)

add(10,5)
printline()

# with argument / with return value

def sub(a,b):
    return a-b

print('Subtraction:',sub(10,5))

# defalut argument

def test(a=10,b=20,c=30,d=40):
    print('A:',a,'B:',b,'C:',c,'D:',d)

test(b=100,d=200)