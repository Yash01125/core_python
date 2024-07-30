class Student:
    def getdata(s, first_name, last_name):
        s.f=first_name
        s.l=last_name
    def putdata(s):
        print("First name:", s.f)
        print("Last name:", s.l)
s1=Student()
s1.getdata("Yash","Mordhara")
s1.putdata()