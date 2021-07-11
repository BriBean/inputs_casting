# author: <Brianna Blue>
# date: <7/8/21>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
symbol_diamond = input('enter a symbol: ')
print("           "+symbol_diamond * 1)
print("          "+symbol_diamond * 3)
print("         "+symbol_diamond * 5)
print("        "+symbol_diamond * 7)
print("       "+symbol_diamond * 9)
print("      "+symbol_diamond * 11)
print("     "+symbol_diamond * 13)
print("      "+symbol_diamond * 11)
print("       "+symbol_diamond * 9)
print("        "+symbol_diamond * 7)
print("         "+symbol_diamond * 5)
print("          "+symbol_diamond * 3)
print("           "+symbol_diamond * 1)
#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
symbol1 = input('enter first symbol here: ')
symbol2 = input('enter second symbol here: ')
print(symbol2 * 6+symbol1 * 1+symbol2 * 6)
print(symbol2 * 5+symbol1 * 3+symbol2 * 5)
print(symbol2 * 4+symbol1 * 5+symbol2 * 4)
print(symbol2 * 3+symbol1 * 7+symbol2 * 3)
print(symbol2 * 2+symbol1 * 9+symbol2 * 2)
print(symbol2 * 1+symbol1 * 11+symbol2 * 1)
print(symbol1 * 13)
print(symbol2 * 1+symbol1 * 11+symbol2 * 1)
print(symbol2 * 2+symbol1 * 9+symbol2 * 2)
print(symbol2 * 3+symbol1 * 7+symbol2 * 3)
print(symbol2 * 4+symbol1 * 5+symbol2 * 4)
print(symbol2 * 5+symbol1 * 3+symbol2 * 5)
print(symbol2 * 6+symbol1 * 1+symbol2 * 6)