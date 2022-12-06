#Original code imported from Free Python Games (https://grantjenks.com/docs/freegames/#free-games)
#Group Members: Patrick Cui (PC) 21025945, Sam Moore (SM) 21001640, and Aditya Adhvaryu (AA) 21021969
#This is the original version of the code.
#It's snake. 

#Imports the method randrange from the module random (AA)
from random import randrange
#Imports everything from the turtle module (AA)
from turtle import *

#Imports the square method and the vector class from the freegames module (AA)
from freegames import square, vector

#Create a two dimensional vector at 0,0 (AA)
food = vector(0, 0)
#Create a two dimensional vector a random coordinate (AA)
snake = [vector(10, 0)]
#Create a two dimensional vector at x = 0 and y = -10 (AA)
aim = vector(0, -10)


#Method for changing the direction of the snake. Sets the aim vector to the parameters of change. (AA)
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

#Method to check if the snakes head is inside the map boundaries (AA)
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


#Method that moves the snake
def move():
    #Initializes a vector that is a copy of the last element of snake, and moves it in the direction of vector aim. (PC)
    head = snake[-1].copy()
    head.move(aim)

    #An if statement to check if the head touches the border, touches itself, or a fruit (PC)
    if not inside(head) or head in snake:
        #If it does happen, it makes a new, red square that has the same coordinates as the head of the snake... (PC)
        square(head.x, head.y, 9, 'red') 
        #... and appends the new square to the end of the snake array. If the snake goes out of bounds, the game finishes. If the snake touches food, it will grow in size. (PC)
        update()
        return

    #Adds the head to the body of the snake by appending it to the end of the list (PC)
    snake.append(head)

    #If statement for if the head vector touches the food vector (PC)
    if head == food:
        #Relocates the food vector to a new, random location (PC)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    #When the snake is not eating, it must maintain its size. snake.pop(0) removes the first element of the array, which corresponds to the tail of the snake. (PC)
    else:
        snake.pop(0)

    #Clears the array (PC)
    clear()

    #For loop to convert every vector in list snake to be a black square. The red square appended to snake in the first if statement gets turned into a part of the snakes body in this block of code. (PC)
    for body in snake:
        square(body.x, body.y, 9, 'black')

    #draws a green square at the location of the food vector. (SM)
    square(food.x, food.y, 9, 'red')
    #updates the food vector. (SM)
    update()
    #timer that calls the function after a certain amount of miliseconds. It controls how fast the snake is going. (SM)
    ontimer(move, 100)



#Draws the canvas that our snake game will be played on. (SM)
setup(420, 420, 370, 0)
#Hides the turtle (SM)
hideturtle()
#Turns the turtle animation off. (SM)
tracer(False)
#Function that sets the focus on our "turtle" screen to capture events. (SM)
listen()
#These 4 onkeys control your snake, assigning a change in y or x value to each arrow key. (SM)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Call the move function. (SM)
move()
#After the move function is executed, the game will finish. (SM)
done()
