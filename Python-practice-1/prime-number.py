a = int(input("enter a number "))
if a > 1:
    for x in range (2, a):
        if(a%x) == 0:
            print("not a prime number")
        else:
            print("prime number")
            break
else:
    print("not a Prime number")