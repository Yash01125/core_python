file=open("yash.txt","w")
file.write("This is file Management")
file.close()
print("File written successfully.")
print("------------------------------------------------------")
file=open("yash.txt","r")
print(file.read())
file.close()
print("------------------------------------------------------")
file=open("yash.txt","a")
file.write("This File is now appended.")
file.close()
print("File written successfully.")
print("------------------------------------------------------")
file=open("yash.txt","r")
print(file.read())
file.close()
print("------------------------------------------------------")
file=open("yash1.txt","w+")
file.write("This file was Write and read.")
print("Current file lovation:",file.tell())
file.seek(0)
print(file.read())
file.close()
print("------------------------------------------------------")
