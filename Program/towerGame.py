"""
Created on ‎May 23rd, ‎2019, ‏‎09:20:00 AM (Thursday)
Author: Lars Quaedvlieg
Contact: Larsquaedvlieg@outlook.com
Copyright: Copyright (C) 2019 Lars Quaedvlieg All rights reserved
License: GNU GPLv3
Version: 1.0

https://www.gnu.org/licenses/gpl-3.0
"""

#Import dependencies
import turtle as t
from random import randint
from time import time

def generate_field():
    '''Generates the field and imports als necessary shapes'''

    #Setup the screen
    window = t.Screen()
    window.setup(640, 540)
    window.title('Towers of Hanoi')

    #Register the shapes
    window.register_shape('./gifs/stuct.gif')
    window.register_shape('./gifs/clicked_stuct.gif')
    window.register_shape('./gifs/unclick_stuct.gif')
    window.register_shape('./gifs/game_title.gif')
    window.register_shape('./gifs/table.gif')
    window.register_shape('./gifs/game_completion.gif')

    #Set background color
    window.bgcolor('#%02x%02x%02x' % (192, 196, 207))

    #Create the design of the field
    turd = t.Turtle()
    turd.hideturtle()
    turd.shape('./gifs/stuct.gif')
    turd.up()

    turd.setx(-200)
    turd.stamp()
    turd.setx(0)
    turd.stamp()
    turd.setx(200)
    turd.stamp()

    turd.shape('./gifs/game_title.gif')
    turd.setx(0)
    turd.sety(200)
    turd.stamp()

    turd.shape('./gifs/table.gif')
    turd.setx(0)
    turd.sety(-195)
    turd.stamp()

def set_blocks(num_blocks):
    '''Generates the blocks'''

    #All blocks will be put in this list
    block_list = []

    #Create i turtles that represent each block as an object
    for i in range(num_blocks):

        #Create a turtle for every block and set it up correctly
        tmp_turd = t.Turtle()
        tmp_turd.speed(2)
        tmp_turd.up()

        #Set the size of the block correctly with a random color
        tmp_turd.shape('square')
        tmp_turd.shapesize(1, 5-(0.45*i))
        tmp_turd.color('black', '#%02x%02x%02x' % (randint(0,255),randint(0,255),randint(0,255)))

        #Set the correct coordinates for the blocks
        tmp_turd.setx(-200)
        tmp_turd.sety(-50+(i*20))

        #Add the block to the list of blocks
        block_list.append(tmp_turd)

    return block_list

def move_block(turtle, stack_number, blocks_in_other_stack):
    '''This function moves the block to a different (specified) stack'''

    #Get current x-coordinate of the block
    if str(stack_number) == '1':
        new_x = -200
    elif str(stack_number) == '2':
        new_x = 0
    elif str(stack_number) == '3':
        new_x = 200

    #Animation of moving the block to a different stack
    turtle.speed(2)
    turtle.sety(150)
    turtle.setx(new_x)
    turtle.sety(-50+(blocks_in_other_stack*20))

def check_click(x, y):
    '''Checks the coordinates of a click on the Turtle screen'''

    #Import needed global variables
    global from_to_stack
    global blocks_per_stack
    global num_moves

    #Enable the clicked visualization of the clicked stack
    turd = t.Turtle()
    turd.hideturtle()
    turd.up()
    turd.shape('./gifs/clicked_stuct.gif')

    #The clicked stack
    tmp_num = 0

    #Check if the click was on the first stack
    if (x >= -260 and x <= -140) and (y >= -90 and y <= -60) and (len(blocks_per_stack['1']['blocks']) > 0 or len(from_to_stack) > 0):

        #Set coordinates of the turtle and set the clicked visualization
        turd.setx(-200)
        turd.sety(-75)
        turd.stamp()

        #Set clicked stack to stack 1
        tmp_num = 1

    #Check if the click was on the second stack
    elif (x >= -60 and x <= 60) and (y >= -90 and y <= -60) and (len(blocks_per_stack['2']['blocks']) > 0 or len(from_to_stack) > 0):

        #Set coordinates of the turtle and set the clicked visualization
        turd.setx(0)
        turd.sety(-75)
        turd.stamp()

        #Set clicked stack to stack 2
        tmp_num = 2

    #Check if the click was on the third stack
    elif (x >= 140 and x <= 260) and (y >= -90 and y <= -60) and (len(blocks_per_stack['3']['blocks']) > 0 or len(from_to_stack) > 0):

        #Set coordinates of the turtle and set the clicked visualization
        turd.setx(200)
        turd.sety(-75)
        turd.stamp()


        #Set clicked stack to stack 3
        tmp_num = 3

    #Check if the stacks clicked is less than 2 and the user clicked on a stack
    if len(from_to_stack) <= 2 and tmp_num != 0:
        
        #Add the clicked stack to the stack list
        from_to_stack.append(tmp_num)

    #Check if the stacks clicked are 2 and the user clicked on a stack
    if len(from_to_stack) == 2 and tmp_num != 0:
        
        #Add a move to the total moves
        num_moves += 1
        #Move the block of the selected stack to the different stack
        move()

def move():
    '''Moves the block from one stack to another (technically)'''
    
    #Define global variables
    global from_to_stack
    global blocks_per_stack
    global num_blocks
    global num_moves

    #Set current stack of block and stack that the block will move to
    current_stack = from_to_stack[0]
    stack_number = from_to_stack[1]

    #Check if the user didn't click the same stack two times and (the size of the stack is 0 or the size on the current stack is smaller than it will move to)
    if current_stack != stack_number and (len(blocks_per_stack[str(stack_number)]['blocks']) == 0 or  blocks_per_stack[str(current_stack)]['size'][-1] < blocks_per_stack[str(stack_number)]['size'][-1]):

        #Set the number of blocks in the other stack
        blocks_in_other_stack = len(blocks_per_stack[str(stack_number)]['blocks'])

        #Move the block (this is only the animation)
        move_block(blocks_per_stack[str(current_stack)]['blocks'][-1], stack_number, blocks_in_other_stack)

        #*Actually* move the block to the correct stack
        blocks_per_stack[str(stack_number)]['blocks'].append(blocks_per_stack[str(current_stack)]['blocks'][-1])
        blocks_per_stack[str(stack_number)]['size'].append(blocks_per_stack[str(current_stack)]['size'][-1])

        #Remove the block from the current stack
        del blocks_per_stack[str(current_stack)]['blocks'][-1]
        del blocks_per_stack[str(current_stack)]['size'][-1]

    #Check if the other stacks (not stack 1) are complete [GAME COMPLETION CHECK]
    if blocks_per_stack['2']['size'] == [num_blocks-i for i in range(num_blocks)] or blocks_per_stack['3']['size'] == [num_blocks-i for i in range(num_blocks)]:

        #Setup the completion turtle
        tur = t.Turtle(visible=False)
        tur.up()
        tur.shape('./gifs/game_completion.gif')

        #Calculate the game duration and output the completion notifications
        tur.sety(125)
        tur.stamp()

        duration = round((time()-start_time)/60, 2)
        tur.sety(-175)
        tur.write('Playing time: '+str(duration)+' minutes.\nNumber of moves: '+str(num_moves)+'!', font=('Arial', 13, 'normal'), align="center")

        print('\nNumber of moves: ', str(num_moves)+'.')
        print('Playing time:', duration, 'minutes!')

        #Terminate the screen on click
        t.onscreenclick(lambda x,y: t.bye())

    #Make the stack move list empty again
    from_to_stack = []

    #Setup and make a turtle that makes the stacks look unclicked
    turd = t.Turtle()
    turd.speed(0)
    turd.hideturtle()
    turd.up()
    turd.shape('./gifs/unclick_stuct.gif')

    #Stack 1
    turd.sety(-75)
    turd.setx(-200)
    turd.stamp()

    #Stack 2
    turd.setx(0)
    turd.stamp()

    #Stack 3
    turd.setx(200)
    turd.stamp()


#Actually run the code
if __name__ == '__main__':

    #Get and process the user input
    cont = False
    while not cont:

        #Ask the user the amount of blocks
        num_blocks = input('How many blocks would you like to have (1 to 10 with S to stop)? ')

        #Maximum amount of blocks
        max_blocks = 10

        #Check if the input is within the allowed game settings (or exit)
        if num_blocks.lower() == 's':
            exit()
        elif num_blocks not in [str(i) for i in range(1, max_blocks+1)]:
            print('Invalid input! Please use a number in the range of 1 to 10 or use S to exit the program.')
        else:
            cont = True
            num_blocks = int(float(num_blocks))

        print()

    #Generate the playing field
    generate_field()

    #Define the dictionary that will keep track of each block (turtle object) per stack and their sizes
    blocks_per_stack = {
        '1': {'blocks': set_blocks(num_blocks), 'size': [num_blocks-i for i in range(num_blocks)]},
        '2': {'blocks': [], 'size': []},
        '3': {'blocks': [], 'size': []}
        }

    #Define the list that allows for blocks to move FROM one stack, TO another stack
    from_to_stack = []

    #Define the game statistics
    num_moves = 0
    start_time = time()

    #Run the check_click function when a user clicks on the screen
    t.onscreenclick(check_click)
