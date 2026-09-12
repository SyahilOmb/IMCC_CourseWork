a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

if a > b and a > c:
    print("a",a)
elif b > a and b > c:
    print("b",b)
elif c > a and c > b:
    print("c",c)
elif a == b or b==c or c==a:
    print("same numbers in input")
else: 
    print("invalid")