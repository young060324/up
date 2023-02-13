# What did you buy? apples
# How many apples did you buy? 3
# What is the price of one apples? 1500
# You bought 3 apples for 4500 KRW.

# What did you buy? bananas
# How many bananas did you buy? 11
# What is the price of one bananas? 800
# You bought 11 bananas for 8800 KRW.

# What did you buy? chocolate
# How many chocolate did you buy? 1
# What is the price of one chocolate? 2200
# You bought 1 chocolate for 2200 KRW.

# What did you buy? coffee
# How many coffee did you buy? 2
# What is the price of one coffee? 2500
# You bought 2 coffee for 5000 KRW.

# What did you buy?
# In total, you spent 20500 KRW

# total = 0
# while True:
#     thing = input("What did you buy? ")
#     if thing == '': # input으로 받은 게 없으면, empty string
#         print("In total, you spent " + str(total) + " KRW.")
#         break
#     many = input("How many " + thing + " did you buy? ")
#     price = input("What is the price of one " + thing + "? ")
#     print("You bought "+ many + " " + thing +" for " + str(int(price)* int(many)) + " KRW. ")
#     total += int(price)* int(many)

# Shopping Calculator V0.2

# What did you buy? apples
# How many apples did you buy? 3
# What is the price of one apples? 1500
# You bought 3 apples for 4500 KRW.
# What did you buy? bananas
# How many bananas did you buy? 11
# What is the price of one bananas? 800
# You bought 11 bananas for 8800 KRW.
# What did you buy? chocolate 
# How many chocolate did you buy? 1
# What is the price of one chocolate? 2200
# You bought 1 chocolate for 2200 KRW.
# What did you buy? coffee
# How many coffee did you buy? 3
# What is the price of one coffee? 2500
# You bought 3 coffee for 7500 KRW.
# What did you buy? 
# Your purchases:
# -------------------------------------------------------------
# apples                               3 x 1500 KRW    4500 KRW
# bananas                             11 x  800 KRW    8800 KRW
# chocolate                            1 x 2200 KRW    2200 KRW
# coffee                               3 x 2500 KRW    7500 KRW
# -------------------------------------------------------------
# Total price:                                        23000 KRW

# apples -> [3, 1500]


purchases = []

while True:
    thing = input("What did you buy? ")
    if thing == '':
        break
    many = input("How many " + thing + " did you buy? ")
    price = input("What is the price of one " + thing + "? ")
    total = int(many) * int(price)
    purchases.append({'name' : thing, 'many' : int(many), 'price' : int(price), 'total' : total})
    print("You bought "+ many + " " + thing +" for " + str(total) + " KRW. ")
    
total_price = 0
for purchase in purchases:
    total_price += purchase['total']

print("Your purchases:")
print("-------------------------------------------------------------")
for purchase in purchases:
    name = purchase['name']
    price = purchase['price']
    many = purchase['many']
    total = purchase['total']
    print(f"{name:<30} {many} x {price:>5} KRW {total:>10} KRW")
print("-------------------------------------------------------------")
print(f"Total price:                                 {total_price:>10} KRW.")
