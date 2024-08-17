from tkinter import *
import math


def calculate_e():
    num = int(entry.get())
    e_approx = sum(1 / math.factorial(n) for n in range(num))
    return e_approx

def safety_check():
    x = int(entry.get())
    if x > 100:
        display_message.config(text="You have exceeded the allowed amount")
    else:
        display_message.config(text=f"The {x}th digit in e is: {calculate_e():.{x}f}")

#The main GUI panel
mainGUI = Tk()
#Creates a label for mainGUI, with a text in the upper left of the grid
Label(mainGUI, text="Enter an integer").grid(row=0, column=0)
#Creates an entry box or text box
entry = Entry()
#Assigns the entry to a cell in the grid
entry.grid(row=0, column=1)

#creating a button with text
button = Button(text="Calculate e", command=safety_check)
#Assigning button to a cell on the GUI
button.grid(row=1, column=1)

#Sets up the displayed message
display_message = Message(mainGUI, text="", width=400)
display_message.config(bg = 'light blue')
display_message.grid(row=2, column=0, columnspan=2)

#Displays the GUI
mainGUI.mainloop()
