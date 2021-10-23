# Pre release
dailytakings = 0
orders_runtot = -1
order_finished = 0
while orders_runtot != order_finished:
    finished = input('have you finished for they day\n if yes then enter (y)')
    if finished == 'y':
        print ('your daily taking today was ',dailytakings)
        # profit = eval('please enter the profit made today by calculating 10% of daily takings')
        profit = dailytakings * 0.1
        print(f'your profit was {profit}')
        orders_runtot = orders_runtot + 1
    else:
        print('please do not use capitals in this program')

        price = [2,5,5.55,7,7.5,9,11,12,14.5,4.5]

        total_price = 0

        user_order = []

        menu_with_prices = [' french fries | £2.00\n\n', ' 1/4 pound burger | £5.00\n\n',' 1/4 pound cheese burger | £5.55\n\n',' 1/2 pound burger | £7.00\n\n', ' 1/2 pound cheeseburger | £7.50\n\n ','Medium pizza | £9.00\n\n ', 'Medium pizza with extra toppings | £11.00\n\n ' ,'Large pizza | £12.00\n\n', ' Large pizza with extra toppings | £14.50\n\n ' , 'Garlic bread | £4.50\n\n' ]

        menu_with_prices_and_codes = [' 001 | french fries | £2.00\n\n', ' 002 | 1/4 pound burger | £5.00\n\n','  003| 1/4 pound cheese burger | £5.55\n\n',' 004 | 1/2 pound burger | £7.00\n\n', ' 005 | 1/2 pound cheeseburger | £7.55\n\n ',' 006 | Medium pizza | £9.00\n\n ', ' 007 | Medium pizza with extra toppings | £11.00\n\n ' ,' 008 | Large pizza | £12.00\n\n', ' 009 | Large pizza with extra toppings | £14.50\n\n ' , ' 010 | Garlic bread | £4.50\n\n' ]

        print('the first few digits before the order refers to the item code')

        Menu_for_display = [' 0 | french fries | £2.00\n\n', ' 1 | 1/4 pound burger | £5.00\n\n','  2| 1/4 pound cheese burger | £5.55\n\n',' 3 | 1/2 pound burger | £7.00\n\n', ' 4 | 1/2 pound cheeseburger | £7.50\n\n ',' 5 | Medium pizza | £9.00\n\n ', ' 6 | Medium pizza with extra toppings | £11.00\n\n ' ,' 7 | Large pizza | £12.00\n\n', ' 8 | Large pizza with extra toppings | £14.50\n\n ' , ' 9 | Garlic bread | £4.50\n\n' ]

        Menu_for_display = ''.join(Menu_for_display)

        Menu = [' french fries ', ' 1/4 pound burger  ',' 1/4 pound cheese burger ',' 1/2 pound burger', ' 1/2 pound cheeseburger  ','Medium pizza  ', 'Medium pizza with extra toppings ' ,'Large pizza | £12.00', ' Large pizza with extra toppings' , 'Garlic bread ' ]

        Unique_codes = []

        item_codes = [': 0 ',': 1 ',': 2 ',': 3 ',': 4 ',': 5 ',': 6 ',': 7 ',': 8 ',': 9 ']

        print(Menu_for_display)

        while True:
            try:
                order_amount = int(input('please enter the amount of things you would like to purchase( INCLUDE ITEMS WHICH YOU ARE MAKING DOUBLE PURCHASES OF)'))
                break
            except ValueError:
                print('Please enter a number')
        
        for count in range(0,order_amount):
            while True:
                try:            
                    order1 = int(input('please enter the order you would prefer using the item codes, if u later decide you dont want an item enter 0 when asked about quantity'))
                    break
                except ValueError:
                    print('Please enter a number')
            if order1 >= (0) and order1 <= (9) :
                print ('Are you sure you want:\n', (Menu[order1]) + (item_codes[order1]))
                while True:
                    try:
                        quantity = int(input('how many of these do you want?'))
                        break
                    except ValueError:
                        print('Please enter a number')
                pos = order1
                for c in range (quantity):
                    if pos <=len(menu_with_prices_and_codes):
                        user_order.append(menu_with_prices_and_codes[pos])
                if len(user_order)==0:
                    print('we dont have an order')
                else:
                    print('so far thats a',user_order)
                    total_price = total_price + (quantity * (price[order1]))
            else:
                 break
        orders_runtot = orders_runtot + 1
        order_finished = order_finished + 1
        menu_with_prices_and_codes = ''.join(menu_with_prices_and_codes)        
        user_order = ''.join(user_order)       
        print('your order was :\n',user_order)
        print ('the total price of your order is','£',(format(total_price, '.2f')))
        import random
        randy = random.randint(10000,1000000000)
        Unique_codes.append(randy)
        print('your unique code is',randy)
        
    dailytakings= dailytakings + total_price
    print (Unique_codes)
