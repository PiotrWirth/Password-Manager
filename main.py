from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if email == "" or website == "":
        messagebox.showerror(
            title="Error", message="You have left some fields empty!")
    else:
        try:
            with open("passwords.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    try:
        with open("passwords.json", mode="r") as data_file:
            data = json.load(data_file)
            website = entry_website.get()
            try:
                messagebox.showinfo(
                    title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
            except:
                messagebox.showerror(
                    title="No data", message=f"No {website} found!")
    except FileNotFoundError:
        messagebox.showerror(
            title="File not found", message="File not created or empty.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

password_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=("Courier", 12, "bold"))
label_website.grid(column=0, row=1)

entry_website = Entry(width=50)
entry_website.focus()
entry_website.insert(END, string="")
entry_website.grid(column=1, row=1, sticky="ew")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="ew")

label_email = Label(text="Email/Username:", font=("Courier", 12, "bold"))
label_email.grid(column=0, row=2)

entry_email = Entry(width=50)
entry_email.insert(END, string="test@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, sticky="ew")

label_password = Label(text="Password:", font=("Courier", 12, "bold"))
label_password.grid(column=0, row=3)

entry_password = Entry(width=21)
entry_password.insert(END, string="")
entry_password.grid(column=1, row=3, sticky="ew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", width=58, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
