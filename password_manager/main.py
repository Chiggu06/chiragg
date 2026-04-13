import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("saved_pass.json") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["username"]}\n Password: {data[website]["password"]}")
            web_entry.delete(0, "end")
        else:
            messagebox.showinfo(title="error", message=f"Credentials of {website} was not found.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website:
            {
        "username": username,
        "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password}")
        if is_okay:
            try:
                with open("saved_pass.json", "r") as df:
                    data = json.load(df)
            except FileNotFoundError:
                with open("saved_pass.json", "w") as df:
                    json.dump(new_data, df, indent=4)
            else:
                data.update(new_data)
                with open("saved_pass.json", "w") as df:
                    json.dump(data, df, indent=4)

            web_entry.delete(0, "end")
            pass_entry.delete(0, "end")
            messagebox.showinfo(message="The credentials were saved!")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = tkinter.Canvas(height = 200, width = 200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = img)
canvas.grid(row=0, column=1)

#Labels
web_label = tkinter.Label(text="Website:")
web_label.grid(row=1, column=0, sticky="W")
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0, sticky="W")
pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0, sticky="W")

#Entries
web_entry = tkinter.Entry(width=21)
web_entry.grid(row=1, column=1, sticky="W")
web_entry.focus()
user_entry = tkinter.Entry(width=39)
user_entry.insert(0 , "chiggu@gmail.com")
user_entry.grid(row= 2, column=1, columnspan=2, sticky="W")
pass_entry = tkinter.Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="W")

#Buttons
search_button = tkinter.Button(text="Search",width= 13,command=search)
search_button.grid(row=1, column=2, sticky="W")
pass_button = tkinter.Button(text="Generate Password", width=13, command=generate)
pass_button.grid(row=3, column=2, sticky="W")
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
