
std_record={"number":[1,2,3,4],"name":["meru","yash","shubh"],"per":[50.14,73.12,73.76]}

print("--------items---------")
print(std_record.items())
print("--------get---------")
print(std_record.get("name"))
print("--------keys---------")
print(std_record.keys())
print("--------values---------")
print(std_record.values())
print("--------particular value---------")
print(std_record["name"][1])
print("--------pop---------")
'''print(std_record.pop("roll no"))'''
print(std_record.items())
print("--------Zip---------")
t=list(std_record["number"])
s=list(std_record["name"])


ab=zip(t,s)
    

x=dict(ab)
print(x)
'''lst=list(x)
for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
        print(lst[i][j])'''
    

