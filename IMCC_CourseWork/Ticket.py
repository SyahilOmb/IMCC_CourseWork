Age = int(input("Enter age :"))
price = 100
if(Age <= 12):
    discount = price * 0.10
    price = price - discount
    print(price)
else:
    print("price is same ", price)