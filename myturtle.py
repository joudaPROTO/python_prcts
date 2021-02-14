import turtle                   #IMPORTNANT: the name of the file should not include any modules

jouda_turtle = turtle.Turtle()
jouda_turtle.speed(1)

def square():
    jouda_turtle.forward(100)
    jouda_turtle.right(90)
    jouda_turtle.forward(100)
    jouda_turtle.right(90)
    jouda_turtle.forward(100)
    jouda_turtle.right(90)
    jouda_turtle.forward(100)


#square()
#jouda_turtle.forward(150)
#square()

elaphant_weight = 3000
ant_weight = 0.1

for count in range(4):
    square()

#if elaphant_weight > ant_weight:
#    square()
#else:
 #   jouda_turtle.forward(100)

#jouda = "happy"
#while jouda == "happy":
#    jouda_turtle.forward(10)




turtle.done()  #it wil keep the turtle open as lon as i want

