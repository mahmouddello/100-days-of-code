import tkinter as tk
import time
from tkinter import END

# window setup
window = tk.Tk()
window.title("Hello Tkinter")
window.minsize(width=500, height=500)

# label
my_label = tk.Label(text="Hello AI Era", font=("Times New Roman", 24, "normal"))
my_label.config(fg="purple")  # we can change too many things using the config() method. check documentation!
my_label.pack()


# Button

def on_click():
    text = entry.get()
    my_label["text"] = text
    print(text)


my_button = tk.Button(text="Click Me!", command=on_click)  # command = event listener when the button got clicked
my_button.pack()

# Entry

# END: is a tkinter constant which represents the point immediately after the last character entered by the user.
# So, when one imports tkinter module (from tkinter import *), Python doesn't show any error.
#
# If you import tkinter as (import tkinter), use tkinter.END else, simply END

entry = tk.Entry(width=50)
entry.insert(END, string="Some text to begin with")
print(entry.get())  # gets text from an entry
entry.pack()

# Multiline textbox

text = tk.Text(height=5, width=30)  # height = number of lines, width = width of the box.
text.insert(END, "Example of multi-line textbox")
text.focus()  # the cursor blink at the text widget.
the_text = text.get("1.0", END)
text.pack()


# Spinbox

def spinbox_used():
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()


# Scale

def scale_used(value):
    print(value)


scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton

def checkbutton_used():
    # prints 1 if on, 0 if off
    print(checked_state.get())


checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
