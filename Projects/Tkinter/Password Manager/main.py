from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for cha in range(nr_numbers)]
    password_list += [random.choice(numbers) for ch in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_entry.get().title()
    if website_entry.get() == '' or pass_entry == '':
        messagebox.showwarning(title="K's Password Manager", message="Please fill out all the boxes")
    else:
        proceed = messagebox.askokcancel(title="K's Password Manager",
                                         message=f"Website:{website}\nEmail:{email_entry.get()}\nPassWord: {pass_entry.get()}\n\nWould you like to save?")
        if proceed:
            with open(file="data.json", mode='r') as data_file:
                data_dict = {website: {'Email': email_entry.get(), 'Password': pass_entry.get()}}
                try:
                    data = json.load(data_file)
                    data.update(data_dict)
                except:
                    with open(file="data.json", mode='w') as data_file:
                        json.dump(data_dict, data_file, indent=4)
                    website_entry.delete(0, END)

                    messagebox.showinfo(title="K's Password Manager", message="Info Has Been Successfully saved")
                else:
                    with open(file="data.json", mode='w') as data_file:
                        json.dump(data, data_file, indent=4)
                finally:
                    website_entry.delete(0, END)
                    pass_entry.delete(0, END)
                    messagebox.showinfo(title="K's Password Manager", message="Info Has Been Successfully saved")


def find_pass():
    website = website_entry.get().title()
    try:
        with open(file='data.json', mode='r') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showwarning("no pass or email saved before\nPlease Save a Password First")
    try:
        messagebox.showinfo(title="K's Password Manager",
                            message=f"Website:{website}\nEmail:{data[website]['Email']}\n Password: {data[website]['Password']}")
    except:
        messagebox.showwarning(title="K's Password Manager", message="Email and Pass don't exist for that Website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20, bg='#222831')
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg='#222831', highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg='#222831', fg="#00ADB5", font=('Comic Sans ', 10, 'bold'))
website_label.grid(row=1, column=0)

email_label = Label(text="Emai/Username: ", fg="#00ADB5", bg='#222831', font=('Comic Sans', 10, 'bold'))
email_label.grid(row=2, column=0)

Pass_label = Label(text="Password:", fg="#00ADB5", bg='#222831', font=('Comic Sans', 10, 'bold'))
Pass_label.grid(row=3, column=0)

website_entry = Entry(width=32, bg="#393E46", fg="#EEEEEE")
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = Button(width=14, text="Search", bg="#393E46", fg="#EEEEEE", command=find_pass)
website_button.grid(row=1, column=2)

email_entry = Entry(width=50, bg="#393E46", fg="#EEEEEE")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "@gmail.com")

pass_entry = Entry(width=32, bg="#393E46", fg="#EEEEEE")
pass_entry.grid(row=3, column=1)

pass_gen_button = Button(text="Generate Password", bg="#393E46", fg="#EEEEEE", command=gen_pass)
pass_gen_button.grid(row=3, column=2)

add_button = Button(width=40, text="Add", bg="#393E46", fg="#EEEEEE", highlightthickness=0, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
