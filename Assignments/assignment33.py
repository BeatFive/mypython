#4-11 My pizzas, your pizza

pizzas=['Pepperoni Pizza','Cheese Pizza','Pineapple Pizza']

friends_pizzas=pizzas[:]

pizzas.append('Chicken Pizza')
friends_pizzas.append('Broccoli Pizza')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nmy friends favourite pizzas are:')
for friends_pizza in friends_pizzas:
    print(friends_pizza)
