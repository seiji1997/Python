from food import Food
from drink import Drink

food1 = Food('Sandwich', 500, 330)
food2 = Food('Chocolate Cake', 400, 450)
food3 = Food('Cream Puff', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 300, 180)
drink2 = Drink('Orange Juice', 200, 350)
drink3 = Drink('Espresso', 300, 30)

drinks = [drink1, drink2, drink3]

print('Food Menu')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drink Menu')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Select a food item number: '))
selected_food = foods[food_order]

drink_order = int(input('Select a drink item number: '))
selected_drink = drinks[drink_order]

count = int(input("How many sets would you like to buy? (10% discount for 3 or more): "))

result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print("The total is " + str(result) + " yen")
