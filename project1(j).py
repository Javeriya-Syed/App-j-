print("------------")
print("Apps")
print("------------")
print("1.Calculator")
print("\n2.Extra Number")
print("\n3.Candies")
print("\nEnter Chioce:")
choice=int(input())
if(choice==1):
    print("calculator---you choose \n1.Addition\n2.subraction\n3.Multiplication\n4.Division")
    uchoose=int(input())
    if(uchoose==1):
        a=int(input("Enter first value:"))
        b=int(input("Enter second value:"))
        print(a+b)
    if(uchoose==2):
        a=int(input("Enter first value:"))
        b=int(input("Enter second value:"))
        print(a-b)
    if(uchoose==3):
        a=int(input("Enter first value:"))
        b=int(input("Enter second value:"))
        print(a*b)
    if(uchoose==4):
        a=int(input("Enter first value:"))
        b=int(input("Enter second value:"))
        print(a/b)
if(choice==2):
    print("Extra Number---Here you will find extra number")
    print("Enter three numbers")
    a=int(input())
    b=int(input())
    c=int(input())
    if(a==b):
        print(c)
    if(b==c):
        print(a)
    if(a==c):
        print(b)
if(choice==3):
    print("Candies---Here children will get equal candies")
    n=int(input("Enter number of children:"))
    m=int(input("Enter number of candies:"))
    print("Each will eat",m//n,"pieces")
    print("Candies taken in total are",n*(m//n))
    
    
