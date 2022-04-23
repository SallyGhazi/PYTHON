coffee = '''                                                                   
                      ~~~~~~                                                   
           -----------------------------------                                         
           ---           ^     ^           ---                                        
              ---    Coffee Machine     ---                                    
                 ---                ---
                   ----------------                                              
'''
menu = '''                                                                     
1-Caffe Latte      10$                                                         
2-Caffe Americano  12$                                                         
3-Espresso         15$                                                         
4-Cappuccino       17$                                                         
5-Caffe macchiato  20$                                                         
'''

#list = ["Caffe Latte","Caffe Americano","Espresso","Cappuccino","Caffe macchiato"]
print("Welcome to Python Caffe. How may I help you? "+coffee+menu)
#choice = int(input("<<<< Choose the type of coffee you want>>>>\n<<<< Enter the number of the option you want >>>>"))
coffee_price = 0
total_price = 0
rest = 0
x=5
while True:
    choice = int(input("<<<< Choose the type of coffee you want>>>>\n<<<< Enter the number of the option you want >>>>"))
    if 1 <= choice <= 5:
        if choice == 1:
            coffee_price = 10
        elif choice == 2:
            coffee_price = 12
        elif choice == 3:
            coffee_price = 15
        elif choice == 4:
            coffee_price = 17
        elif choice == 5:
            coffee_price = 20
    else:
        print("Invalid number")
        break
return choice

cups = int(input("<<<< Enter the number of cups you want >>>>"))
total_price = coffee_price * cups
print("<<<< Total Price >>>>", total_price)
print('Have a good day')
received = int(input("<<<< Pay your bill >>>>"))
if received >= total_price:
    rest = received - total_price
    print("<<<< the rest of the money >>>>", rest)
else:
    print("<<<< The amount is not enough|| your order has been canceled >>>>")
