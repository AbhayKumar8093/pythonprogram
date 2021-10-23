a=int(input("enter ist number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if (a>b and a<c) or (a<b and a>c):
    print("middle of A:",a)
elif (b>a and b<c) or (b<a and b>c):
    print("middle of B:",b)
else:
    print("middle of C:",c)