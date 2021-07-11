# author: <Brianna Blue>
# date: <7/8/21>

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #
first_name = input('first name: ')
last_name = input('last name: ')
print(last_name + ',' + first_name )
#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #
symbol = input('enter symbol: ')
print(symbol * 1)
print(symbol * 2)
print(symbol * 3)
print(symbol * 2)
print(symbol * 1)

#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #
symbol = input('enter symbol: ')
print(symbol * 1)
print(symbol * 2)
print(symbol * 3)
print(symbol * 4)
print(" "+symbol * 3)
print("  "+symbol * 2)
print("   "+symbol * 1)
# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #
num1 = input('num1: ')
num2 = int(input('num2: '))
num3 = float(input('num3: '))
print(num1 * 10)
print(num2 * 10)
print(num3 * 10)
# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #
num = float(input('num: '))
print('the diameter sums up to', num * 2)

# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #
def area_circle(radius):
    area = 3.14 * radius ** 2
    return area
num = int(input('enter a radius: '))
area_circle(num) #put num in the parentheses! then set this whole thing equal to a var!


# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in example.py
name = input('hello!, what\'s your name? ')
print('greetings, ' + name + ', it\'s wonderful to meet you love. my name is AI.\n')

hobby = input('what\'s your favorite hobby? ')
print(hobby +  ',that\'s great! I am a big fan of that. For me, I also like art and writing, it\'s in my nature!\n')

color = input('what\'s your favorite color? ')
print(color + , 'is an amazing color, I personally love basil green and mauve! Very obsecure colors.\n')

summer = input('how is your summer so far? ')
print('That\'s great to hear! I\'m glad it\'s going well for you. My summer is going fine so far as well!\n')

food = input('what is your favorite food item? ')
print(food +  ',very delicious, I agree! One of my favorites are sweet potatoes.\n')

overall = input('how do you think this conversation was? ')
print('this conversation was wonderful! It was great getting to know you and your intrests.\n')

farewell = input('that\'s all I have for now. It was amazing meeting you! Will I see you again soon? ')
print('I\'m excited to see you once again! Take care of yourself darling. Goodbye!')