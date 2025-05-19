import turtle

print("Hello, World!")
ttl1 = turtle.Turtle()

def ondpress():
    ttl1.forward(50)

try:    
    d = open("laserCoords.txt", 'r')
except FileNotFoundError:
    ttl1.pencolor((1.0, 0, 0))
    print("bozo")



main_window = turtle.Screen()
main_window.onkeyrelease(ondpress, "d")
ttl1.forward(50)
main_window.listen()
main_window.mainloop()
my_password = "Humpty Dumpty sat on a wall, Humpy Dumpty had a great fall, and all the king's horses and all the king's men couldn't put Humpty Dumpty back together again innit"
