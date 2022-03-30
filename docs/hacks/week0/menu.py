# incorporated swap and matrix into harcoded menu for week 0 activities
import time

"""
Introduction to Console Programming
Writing a function to print a menu
"""
#start adding menu
number1 = 0
number2 = 0
# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Swap' )
    print('5 -- Matrix' )
    print('6 -- Animation' )
    print('7 -- Tree' )
    print('8 -- Exit' )


    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Swap',
    5: 'Matrix',
    6: 'Animation',
    7: 'Tree',
    8: 'Exit',

}

# Print menu options from dictionary key/value pair


#--------------------------------------------------------
#--------------------------------------------------------

def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()
#--------------------------------------------------------
#--------------------------------------------------------

def matrix():
    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    for row in matrix:
        for col in row:
            print(col, end= "")
        print()
#--------------------------------------------------------
#--------------------------------------------------------

#def swap2numbers(a, b):
 #   temp = a
  #  a = b
#  b = temp

def swapnumbers():
    number1 = int(input(" What is the first number you want? : "))
    number2 = int(input(" What is the second number you want? : "))
    print("Before Swapping two Number",(number1, number2))
    # making sure that the inputs stay in order
    if number1 > number2:
        temp = number1
        number1 = number2
        number2 = temp
    
    print("After Swapping two Numbers",(number1, number2))

# code that calls the function to swap
# used input so that users can play around with numbers and see how swaps + keeps in order
#--------------------------------------------------------
#--------------------------------------------------------
def create_tree(rows):
  for i in range(0, rows+1):
        for j in range(0, rows-i):
            print(end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()
## code added after week 0, implimentation through solutions page
def grow_tree():
  rows = int(input("Enter height of the tree:  "))
  create_tree(rows)
  spaces = lambda a: int(a-2) + a % 2
  moveRt = " " * spaces(rows)
  for i in range(3):
      print(moveRt, end="###")
      print()
#--------------------------------------------------------
#--------------------------------------------------------  
# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "\    /\ ")
    print(sp + " )  ( ')")
    print(SHIP_COLOR, end="")
    print(sp + "(  /  )")
    print(sp + " \(__)|")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)
#--------------------------------------------------------
#--------------------------------------------------------

# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    global number1
    global number2
    while True:
        try:
            option = int(input('Enter your choice 1-7: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            elif option == 4:
                swapnumbers(number1, number2)
            # Exit menu
            elif option == 5:
                matrix()
            elif option == 6:
                ship()
            elif option == 7:
                grow_tree()
            elif option == 8:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')
          

if __name__=='__main__':
    # print_menu1()
    print_menu2()