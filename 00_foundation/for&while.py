money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}

for item_name in items:
    print('--------------------------------------------------')
    print('Your wallet contains ' + str(money) + ' yen')
    print(item_name + ' is one ' + str(items[item_name]) + ' yen')

    input_count = input('To buy ' + item_name + ', please enter the number of items: ')
    print('To buy ' + item_name + ', the number of ' + input_count + ' is')

    count = int(input_count)
    total_price = items[item_name] * count
    print('The amount paid is ' + str(total_price) + ' yen')

    if money >= total_price:
        print('You bought ' + item_name + ' ' + input_count + ' pieces')
        money -= total_price

        if money == 0:
            print("Wallet has been bought")
            print("Wallet is empty")
            break
    else:
        if money == 0:
            print('Not enough money')
            print('Could not buy ' + item_name)

print("The remaining money is " + str(money) + " yen")
