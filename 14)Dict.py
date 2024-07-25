d={1:"Yash",2:"Ajay",3:"Vijay",4:"Karan"}
print(type(d))
print(d.get(1))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(4))
print(d.popitem())
print(d)
d1={5:"Atul",6:"Sanjay",1:"Yash N"}
d.update(d1)
print(d)