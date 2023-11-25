import tkinter as tk


def convert():
    miles = int(mile_entry.get())
    to_km = round(miles * 1.6)
    dynamic_label.config(text=str(to_km))


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles Entry

mile_entry = tk.Entry(width=7)
mile_entry.grid(row=0, column=1)

# Mile label
mile_label = tk.Label(text="Mile")
mile_label.grid(row=0, column=2)

# is equal to label
equal_to = tk.Label(text="is equal to")
equal_to.grid(row=1, column=0)

# dynamic_label

dynamic_label = tk.Label()
dynamic_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

# calculate_button


calculate_btn = tk.Button(text="Calculate", command=convert)
calculate_btn.grid(row=2, column=1)

window.mainloop()
