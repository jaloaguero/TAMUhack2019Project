#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# solves all equations with one instance of x^n

import math

from tkinter import *

# __author__ = "jalo"
# __date__ = "$Jan 26, 2019 - Jan 27, 2019"

# file variable writes to UserNumber
file = open("UserNumber", "w+")

# master is initialized as the Tk() class
master = Tk()

# output is initialized as Label, which prompts user to input 3 numbers and press Enter
output = Label(master, text = "Please enter 3 pattern numbers separated by spaces. "
                              "When you are done typing in your numbers, press Enter.")

# packs the widgets in a organized manner
output.pack()

# UserInput initialized as
UserInput = Entry(master)
UserInput.pack()

def setToArray(UI):
    UINum = UserInput.get()
    file.write(UINum)
    master.destroy()

UserInput.bind('<Return>', setToArray)

master.mainloop()

file.close()

#=================================================================

# __author__ = "mia"
# __date__ = "$Jan 26, 2019 - Jan 27, 2019"

# file variable reads UserNumber
file = open("UserNumber", "r")

# initialized empty array content
content = []

# for loop to read all elements from the file as float
for val in file.read().split():
    # takes file elements and saves into array content
    content.append(float(val))

# closes file
file.close()

# y_int variable for y intercept of the equation
# intercept is found where x = 0 (array[0] = y_int)
y_int = content[0]

# for loop to subtract y intercept from all elements of the array
for x in range(len(content)):
    content[x] -= y_int

# coefficient will equal content[1]
coefficient = content[1]

# now divide all elements of the array by the coefficient
for x in range(len(content)):
    content[x] = float(content[x] / coefficient)

# temp variable is initialized to the logbase2(content[2])
temp = math.log(content[2], 2)
# i variable is initialized to 1
# i will be used to find the denominator
i = 1
# power variable will hold the exponent
power = temp

# while the (temp * i) rounded to 2 decimal places
# is not an integer, then increment i, power now holds temp * i
while not round(temp * i, 2).is_integer():
    i += 1
    power = temp * i

teststr = ""

# checks the coefficient
# when coefficient == 1
if coefficient == 1:
    teststr += "y = x"
# when coefficient == -1
elif coefficient == -1:
    teststr += "y = -x"
# when coefficient is an integer
elif coefficient.is_integer():
    teststr += "y = " + str(int(coefficient)) + "x"
# when coefficient is not an integer
else:
    teststr += "y = " + str(coefficient) + "x"

# checks the exponent (aka power)
# when the power == 1
if power == 1:
    teststr += " "
# when the power is an integer
elif power.is_integer():
    teststr += "^" + str(int(power)) + " "
# when the power is not an integer
else:
    teststr += "^(" + str(int(round(power, 2))) + "/" + str(i) + ") "

# checks the y intercept
# when y int == 0
if y_int == 0:
    teststr += ""
# when y int < 0 and is an integer
elif y_int < 0 & y_int.is_integer():
    teststr += "- " + str(int(-1 * y_int))
# when y int < 0 and is not an integer
elif y_int < 0 & (not y_int.is_integer()):
    teststr += "- " + str(-1 * y_int)
# when y > 0 and is an integer
elif y_int.is_integer():
    teststr += "+ " + str(int(y_int))
# when y > 0 and is not an integer
else:
    teststr += "+ " + str(y_int)

# final equation has format y = mx^n + b

#========================================================================

# name and declaring of gui window
next = Tk()

# creates a "label", a text box that cannot be interacted with
output = Label(next, text = "Final equation " + teststr)
# this will put the label named 'output' on the window
output.pack()

# same as above
output1 = Label(next, text = "Let's break this down")
output1.pack()

# these are the commands of the buttons when pressed
def ButtonCommand1():
    # this will "print" the output on the window
    output2.pack()
    # this will display the new button
    Button2.pack()

# same but for the second button
def ButtonCommand2():
    # displays output
    output3.pack()

# declares a button, the text of what the button will say, and the command is the function above
Button1 = Button(next, text= "next", command=ButtonCommand1)

# displays button
Button1.pack()

# full_string variable explains y intercept
full_string = "To find the y intercept:\n" \
              "The y intercept is the point where the line/curve crosses the y axis.\n" \
              "The y-intercept is the y-value at x = 0. It is a constant that can raise or lower the curve/line" + \
              "Subtract the y-intercept from each y-value.\n" \
              "After you complete this, click next"

# the declared strings
output2 = Label(next, text=full_string)

# full_string now holds explanation of coefficients
full_string = "Next, we find the coefficient.\n" \
              "We can determine the coefficient of this equation is the new y-value at x = 1. " \
              "This is because a*1^n for any n equals a.\nDivide every y-value by the coefficient\n"

output3 = Label(next, text = full_string)

# declares the second button like the first one
Button2 = Button(next, text= "next", command=ButtonCommand2)

# signifies the end of the gui interface
next.mainloop()

#========================================================================

print("fin")
