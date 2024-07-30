import UDF

while True:
    print("1. Odd Even")
    print("2. Max of Two")
    print("3. Max of Three")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*40)

    choice = input("Enter your choice: ")

    if choice == "1":
        a=int(input("Enter your number:"))
        UDF.oddeven(a)
        print("*" * 60)
    elif choice == "2":
        b=int(input("Enter your 1st number:"))
        c=int(input("Enter your 2nd number:"))
        UDF.maxof2(b,c)
        print("*" * 60)
    elif choice == "3":
        d=int(input("Enter your 1st number:"))
        e=int(input("Enter your 2nd number:"))
        f=int(input("Enter your 3rd number:"))
        UDF.maxof3(d,e,f)
        print("*" * 60)
    elif choice == "4":
        n=int(input("Enter the number for fibonacci: "))
        UDF.fibonaki(n)
        print("*" * 60)
    elif choice == "5":
        n = int(input("Enter Number for prime:"))
        UDF.prime(n)
        print("*" * 60)
    elif choice == "6":
        print("*" * 60)
        break
    else:
        print("Invalid choice")
        print("*"*60)


