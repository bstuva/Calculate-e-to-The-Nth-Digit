from tkinter import *

#The main GUI panel
mainGUI = Tk()
#Creates a label for mainGUI, with a text in the upper left of the grid
Label(mainGUI, text="Enter an integer").grid(row=0, column=0)
#Creates an entry box or text box
entry = Entry()
#Assigns the entry to a cell in the grid
entry.grid(row=0, column=1)



#Displays the GUI
mainGUI.mainloop()
