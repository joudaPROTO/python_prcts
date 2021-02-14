age = 50

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 69
else:
    price = 48

print(f"your admission cost is {price} AED.\n")


rquested_toppings = ['mushrooms','extra cheese','extra sauce','no pineapples']

if 'no pineapples' in rquested_toppings:
    print("pineapples removed")
if 'extra sauce' in rquested_toppings:
    print("extra sauce added")
if 'tomato' in rquested_toppings:
    print("tomato added")
if 'mushrooms' in rquested_toppings:
    print(f"mushrooms added")

print("\nFinished making your order\n")


#if loop in for loop
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese','extra olives']

for requested_topping in requested_toppings:
    if requested_topping == 'extra olives':
        print(f"sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

#for loop in if loop

avaliable_toppings = ['pineapples','mushrooms','extra olives','extra cheese','extra sauce']
requested_toppings = ['pineapples','mushrooms','french fries','extra olives','extra cheese','extra sauce','ketchup'] #users order

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'extra olives' or requested_topping == 'extra cheese':
            print(f"sorry, we are out of {requested_topping} right now.")
        elif requested_topping in avaliable_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure you want plain pizza?\n")

current_users = ['admin','jouda','tareq','hamza','anas']
new_users = ['sarah','tareq','jouda','ahmed','admin']       #user input

if not new_users:
     print("We need to find some users!")
else:
    for new_user in new_users:
       if new_user == 'admin':
           print(f"hello {new_user.title()}, would you like to see a status letter?")
       elif new_user in current_users:
           print(f"Hi {new_user.title()},welcome back!.")
       else:
           print(f"sorry {new_user.title()}, you have to register first")
