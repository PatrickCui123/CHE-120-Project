#Original code imported from Free Python Games (https://grantjenks.com/docs/freegames/#free-games)
#Group Members: Patrick Cui (PC) 21025945, Sam Moore (SM) 21001640, and Aditya Adhvaryu (AA) 21021969
#This is our updated version of the game. Not only is there a new kind of food that subtracts a segment of the snake, all fruits also speed up the snake. 


#Imports the method randrange from the module random (AA)
from random import randrange 
#Imports everything from the turtle module (AA)
from turtle import *

#Imports the square method and the vector class from the freegames module (AA)
from freegames import square, vector

#Create a two dimensional vector a random coordinate 0 (AA)
food = vector(randrange(-15, 15) * 10,randrange(-15, 15) * 10)
#Create a two dimensional vector a random coordinate (AA)
anti_food = vector(randrange(-15, 15) * 10,randrange(-15, 15) * 10)
#Create a list, with 1 vector starting at 10,0 (AA)
snake = [vector(10, 0)]
#Create a two dimensional vector at x = 0 and y = -10 (AA)
aim = vector(0, -10)


#Method for changing the direction of the snake. Sets the aim vector to the parameters of change. (AA)
def change(x, y):
    aim.x = x
    aim.y = y


#Method to check if the snakes head is inside the map boundaries (AA)
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

#Method that moves the snake
def move():
    #Initializes a vector that is a copy of the last element of snake, and moves it in the direction of vector aim. (PC)
    head = snake[-1].copy()
    head.move(aim)

    #Initializes an int. This is used for the timer later on. (PC)
    time = 100

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
        #Makes the snake go ever so slightly faster (PC)
        time -= 1
        #Relocates the food vector to a new, random location (PC)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    #When the snake is not eating, it must maintain its size. snake.pop(0) removes the first element of the array, which corresponds to the tail of the snake. (PC)
    else:
        snake.pop(0)

    #Clears the array (PC)
    clear()

    #If statemnt for if the head vector touches the anti_food vector. (PC)
    if head == anti_food:
        #Remove a segment from the snake. (PC)
        snake.pop()
        #Makes you go faster (PC)
        time -= 5
        #If the snake eats an anti_food when it is only 1 block long, it will cease to exist. (PC)
        if(len(snake) == 0):
            return
        #Relocates the anti_food vector to a new, random location (PC)
        anti_food.x = randrange(-15, 15) * 10
        anti_food.y = randrange(-15, 15) * 10

    #For loop to convert every vector in list snake to be a black square. The red square appended to snake in the first if statement gets turned into a part of the snakes body in this block of code. (PC)
    for body in snake:
        square(body.x, body.y, 9, 'green')

    #draws a green square at the location of the food vector. (SM)
    square(food.x, food.y, 9, 'red')
    #draws a blue square at the location of the anti_food vector. (SM)
    square(anti_food.x, anti_food.y, 9, 'purple')
    #updates the food and anti_food vectors. (SM)
    update()
    #timer that calls the function after a certain amount of miliseconds. It essentially how fast the snake is going. (SM)
    ontimer(move, time)


#Draws the canvas that our snake game will be played on. (SM)
setup(420, 420, 370, 0)
#Hides the turtle (SM)
hideturtle()
#Turns the turtle animation off. (SM)
tracer(False)
#Function that sets the focus on our "turtle" screen to capture events. (SM)
listen()
#These 4 onkeys control your snake, assigning a change in y or x value to each key, forming a WASD control scheme. (SM)
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
#Call the move function. (SM)
move()
#After the move function is executed, the game will finish. (SM)
done()
