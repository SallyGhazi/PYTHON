# <<<<<< Coffee_Machine >>>>>>

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
# =====================list======================================
menu1 = ["Caffe Latte", "Caffe Americano", "Espresso", "Cappuccino", "Caffe macchiato"]
price = [10, 12, 15, 20, 25]
coffee_price = 0
total_price = 0
print(msg1 + menu)
choice = int(input("<<<< Enter the number of the option you want >>>>\n"))
# =====================function======================================
def insert_coins():
    received = int(input("<<<< Pay your bill >>>>"))
    rest = 0
    if received >= total_price:
        rest = received - total_price
        print("<<<< the rest of the money >>>>", rest)
    else:
        print("<<<< The amount is not enough|| your order has been canceled >>>>")
    return rest

# ================main program=======================
while True:
    if choice == 1:
        print(menu1[0], "  ", price[0], "$")
        coffee_price = price[0]
        break
    elif choice == 2:
        print(menu1[1], "  ", price[1], "$")
        break
    elif choice == 3:
        print(menu1[2], "  ", price[2], "$")
        break
    elif choice == 4:
        print(menu1[3], "  ", price[3], "$")
        break
    elif choice == 5:
        print(menu1[4], "  ", price[4], "$")
        break
    else:
        print("XXX Invalid number XXX" + "\n<<<< Try again >>>>\n" + menu)

cups = int(input("<<<< Enter the number of cups you want >>>>"))
total_price = coffee_price * cups
print("<<<< Total Price >>>>", total_price)
print(insert_coins())
print('Have a good day')