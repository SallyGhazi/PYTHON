#Coffee_Machine

# Program Requirements
# 1) Print a report of Resources
# 2) Check for resource and are there enough
# 3) Process coins
# 4) Check transaction is is successful? if not refund money and not give drink
# 5) if successful make coffee and deduct resources.

msg1 = """                   
         Welcome to Python Caffe ☻☻☻
                  / _|/ _|         
         ___ ___ | |_| |_ ___  ___ 
        / __/ _ \|  _|  _/ _ \/ _ \\
       | (_| (_) | | | ||  __/  __/
        \___\___/|_| |_| \___|\___| 
"""
menu = """
     ♣Caffe Menu♣
[Caffe Type]            [Price]
1-Caffe Latte            10$                                                         
2-Caffe Americano        12$                                                         
3-Espresso               15$                                                         
4-Cappuccino             17$                                                         
5-Caffe macchiato        20$  
"""
#=====================list======================================

menu1 = ["Caffe Latte" , "Caffe Americano", "Espresso", "Cappuccino", "Caffe macchiato"]
price1 = [10 , 12 , 15 , 20 ,25]

#======================Variables=================================

coffee_price = 0
total_price = 0
#rest = 0

#======================Functions==================================

def order():
    while True:
        choice = int(input("<<<< Enter the number of the option you want >>>>"))
        if choice == 1:
            price = 12
            return menu1[0]
        elif choice == 2:
            return menu1[1]
        elif choice == 3:
            return menu1[2]
        elif choice == 4:
            return menu1[3]
        elif choice == 5:
            return menu1[4]
        else:
            print("XXX Invalid number XXX"+"\n<<<< Try again >>>>\n"+menu)
            order()

#=====================================================================




#======================================================================
def insert_coins():
    received = int(input("<<<< Pay your bill >>>>"))
    rest = 0
    if received >= total_price:
        rest = received - total_price
        print("<<<< the rest of the money >>>>", rest)
    else:
        print("<<<< The amount is not enough|| your order has been canceled >>>>")
    return received

#================main program=======================
print(msg1 + menu)
print(order())
cups = int(input("<<<< Enter the number of cups you want >>>>"))
total_price = coffee_price * cups
print("Do you want to order ")
ask = input("y/n\n")
if ask == "y":
    order()
else:
    print("<<<< Total Price >>>>", total_price)
    print('Have a good day')


