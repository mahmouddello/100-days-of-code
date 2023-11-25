import tkinter as tk
from tkinter import END

# window setup
window = tk.Tk()
window.title("Hello Tkinter")
window.minsize(width=500, height=500)

# Layout managers: pack(), place() and grid()

# Pack Layout Manager:
# The pack() layout manager organizes the widgets in a horizontal or vertical manner.
# It automatically resizes the widgets based on their content and can also fill empty spaces.
# The syntax for using the pack() method is widget.pack(options).
#
# Grid Layout Manager:
# The grid() layout manager organizes the widgets in a grid-like structure.
# It allows the widgets to be placed in specific rows and columns and provides more control over their positioning.
# The syntax for using the grid() method is widget.grid(options).
#
# Place Layout Manager:
# The place() layout manager allows the widgets to be placed at a specific pixel position on the GUI.
# It is useful for creating complex layouts, but it requires more precise positioning and resizing of the widgets.
# The syntax for using the place() method is widget.place(options).

# label
my_label = tk.Label(text="Hello AI Era", font=("Times New Roman", 24, "normal"))
my_label.config(fg="purple")  # we can change too many things using the config() method. check documentation!
my_label.grid(row=0, column=0)  # place layout manager


def on_click():
    print("Hello AI Era")


my_button = tk.Button(text="Click Me!", command=on_click)  # command = event listener when the button got clicked
my_button.grid(column=1, row=1)

# Entry
entry = tk.Entry(width=50)
entry.insert(END, string="Some text to begin with")
print(entry.get())  # gets text from an entry
entry.grid(row=2, column=2)

window.mainloop()
