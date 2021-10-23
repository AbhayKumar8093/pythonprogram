a=int(input("enter ist number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
d=int(input("enter 4st number"))
e=int(input("enter 5nd number"))
sum= a+b+c+d+e
percent=(sum/500)*100
print("total marks=",sum,"percent=",percent)
if percent>=80:
    print("grade of A")
elif percent>=60:
    print("grade of B")
elif percent>=40:
    print("grade of C")
else:
    print("grade of D")

