magicians = ['jouda','asaad','tareq']
for magician in magicians:      #dont forget the colon
    print(magician)
    print(f"{magician.title()}, that was a great trick!")

print("Thankyou evryone!")

#using range in for function
for value in range(1,5):
    print(value)
#using range ti make a list
numbers = list(range(1,5))
print(numbers)
even_numbers = list(range(0,11,2)) # range from 0 to 10 and then add 2
print(even_numbers)
odd_numbers = list(range(1,21,2)) #range from 1 to 10 then add 2
print(odd_numbers)

#another ways to print numirical lists

num_list = []
for value in range(1,21,2):
    num_list.append(value)
print(f"\n{num_list}")
print(min(num_list))
print(max(num_list))
print(sum(num_list))

numbers = [values**3 for values in range(3,31)]
print(f"\n{numbers}")

#slicing lists
players = ['jouda','tareq','hamza','anas']
print("here are the players in my team:")
for player in players[1:]:
    print(player.title())

print(f"\n{players[0:3]}")
print(f"\n{players[0:]}")
print(f"\n{players[-3:]}")
print(f"\n{players[:-2]}")

