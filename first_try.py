# Trying out my first user surfaces
# Not working

import tkinter
import time

now = 0

# Function for end of program
def refersh():
    now = time.time()
    main.update()

# Main window
main = tkinter.Tk()

# Button for refresh of window
tkinter.Button(main, text= "Refrsh", command= refersh).pack()

# Create label
lb1 = tkinter.Label(main, text=now)
lb1["font"] = "Courier 16 italic"
lb1["height"] = 2
lb1["width"] = 20
lb1["borderwidth"] = 5
lb1['relief'] = "raised"
lb1['bg'] = "#FFFFFF"
lb1['fg'] = "#000000"
lb1['anchor'] = "w"
lb1.pack()

# Create entry field with calculation

def quad():
    value_entry = e.get()
    try:
        input_value = float(value_entry)
        lb2["text"] = "Result:" + str(input_value * input_value)
    except:
        lb2["text"] = "Please enter a number"

# Input field

e = tkinter.Entry(main).pack()

# Botton for computing of input

bquad = tkinter.Button(main, text= "Quad operation", command= quad).pack()

# Output label

lb2 = tkinter.Label(main, text= "Result:").pack()

# Endless loop

main.mainloop() 