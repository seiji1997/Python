apple_price = 200
money = 1000

input_count = input('Enter the number of apples you want to purchase: ')
count = int(input_count)
total_price = apple_price * count

print('You are purchasing ' + str(count) + ' apples')
print('Total payment is ' + str(total_price) + ' yen')

if money > total_price:
    print("Bought " + str(count) + " apples")
    print("Remaining balance is " + str(money - total_price) + " yen")
    
elif money == total_price:
    print("Bought " + str(count) + " apples")
    print("Wallet is now empty")
    
else:
    print("Insufficient funds")
    print("Could not buy apples")
