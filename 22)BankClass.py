class Bank:
    def openaccount(s,acno,acname,balance):
        s.acno=acno
        s.acname=acname
        s.balance=balance
        print("Hello",acname,"your account number is",acno,"and your balance is Rs.",balance)

    def deposit(s, amount):
        s.balance += amount
    def withdraw(s, amount):
        if amount <=s.balance:
            s.balance-=amount
        else:
            print("Insufficient Balance")
    def chkbalance(s):
        print("Current balance is Rs.",s.balance)


s1=Bank()
s1.openaccount(111,"Yash Mordhara",50000)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*40)

    choice=int(input("Please choose an option:"))

    if choice==1:
        amount=int(input("Enter amount to deposit:"))
        s1.deposit(amount)
        print("*" * 60)
    elif choice==2:
        amount=int(input("Enter amount to withdraw:"))
        s1.withdraw(amount)
        print("*" * 60)
    elif choice==3:
        s1.chkbalance()
        print("*" * 60)
    elif choice==4:
        print("*" * 60)
        break
    else:
        print("Invalid choice")
        print("*" * 60)