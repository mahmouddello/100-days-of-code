import tkinter as tk
import pyperclip
from string import ascii_letters, digits, punctuation
from tkinter import messagebox
from random import choice, randint

entries = []
letters, numbers, symbols = list(ascii_letters), list(digits), list(punctuation)


def are_there_empty_entries():
    """
    Checks for the entries if any one of them is empty.

    :return: Bool
    """
    for entry in entries:
        if entry.get().strip(" ") == "":
            return True
    return False


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a strong complicated password
    :return: None
    """
    password_entry.delete(0, tk.END)  # clearing the password entry in case a password has been generated
    r_letters = [choice(letters) for c in range(randint(8, 10))]
    r_symbols = [choice(symbols) for a in range(randint(2, 4))]
    r_numbers = [choice(numbers) for d in range(randint(2, 4))]
    # Random picks from each list
    password = r_numbers + r_letters + r_symbols  # combining lists
    password = "".join(password)  # list -> string
    pyperclip.copy(password)  # copies the password to the clipboard
    password_entry.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    """
    Get the content of the app entries.
    Get the contents of the website entry, email/username entry and password entry.
    If any of the fields is empty, then prompt friendly information about it.
    If all fields are filled, check is fields are not filled with spaces.
    If not, then get confirmation from the user if he wants to save the data.
    """

    # Holding the data from the entries in variables
    website = website_entry.get().strip(" ")
    email = email_entry.get().strip(" ")
    password = password_entry.get().strip(" ")
    # stripping the spaces from the entries

    if are_there_empty_entries():
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty :(")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail:{email} "
                                               f"\nPassword: {password} \n is it ok to save?")
        if is_ok:
            # Saving the data to a file
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
            # clearing (wiping) the data in the website & password entries
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas image
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website: ")
email_label = tk.Label(text="Email/Username: ")
password_label = tk.Label(text="Password: ")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=36)
email_entry = tk.Entry(width=36)
password_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky="we")
email_entry.grid(column=1, row=2, columnspan=2, sticky="we")
password_entry.grid(column=1, row=3, columnspan=2, sticky="we")
entries.append(website_entry)
entries.append(email_entry)
entries.append(password_entry)

# Generate Password Button
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="we")

website_entry.focus()  # focuses the cursor on the website entry
email_entry.insert(index=0, string="youremail@email.com")

window.mainloop()
