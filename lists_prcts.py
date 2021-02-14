racecar = ['speed','RPM','redline','aero']  #basics of lists
print(racecar[0].title())
print(racecar[1].lower())
print(racecar[3].upper())

print(racecar[-1].title())
print(racecar[-2].title())

mymsg  = f"i like to rev my car till it hit the {racecar[-2].title()}"

print(mymsg)

names = ['jouda','tareq','dad','mom']
greeting =f"hi {names[-2].title()}, would you like to come with us?"
print(greeting)

cars = ['lexus','BMW','tesla']
print(cars)

cars[0] = 'toyota'  #modifying elements in a list
print(cars)

cars.insert(1, 'GMC')
cars.insert(0, 'nissan')    #adding elements to a list
print(cars)

del cars[2]                 #delete elements
print(cars)

print(cars.pop())           #print the element on top of the list

popped_cars = cars.pop()
print(cars)                 #remove the element on top of the list
print(popped_cars)          #remember: everytime you use .pop() the element you work on is no longer in the list
#another way to make a list

cars2 = []

cars2.append('honda')
cars2.append('merc')
cars2.append('audi')
cars2.append('nissan')

print(cars2)

#how .pop() can be useful?
last_owned = cars2.pop()
print(f"The last car i owned was a/an {last_owned.title()}.")

first_owned = cars2.pop(0)
print(f"The first car i owned was a/an {first_owned.title()}.")


#romove items using .remove()
#remember everytime you use .pop() that element is removed from the list

too_expensive = 'audi'
cars2.remove(too_expensive)

print(cars2)
print(f"\nA {too_expensive.title()} is too expensive for me.")


#sorting lists
cars3 = ['bmw','audi','toyota','subaru']
cars3.sort()
print(cars3)
cars3.sort(reverse=True)  #or can use cars3.reverse() without sorting
print(cars3)

#sorting lists temoporarily with sorted()
print("the last updated cars3 list")
print(cars3)
print("\nHere is the temoporarily sorted cars3 list")
print(sorted(cars3))
#printing list length
print(len(cars3))
print(f"\ni have {len(cars3)} cars in my carage.")
