from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_name = website_label_input.get()
    email = email_name_input.get()
    user_password = password_input.get()
    new_data = {
        website_name: {
            "email": email,
            "password": user_password
        }
    }
    if len(website_name) == 0 or len(email) == 0 or len(user_password) == 0:
        messagebox.showinfo(
            title="OOPS", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name, message=f"These are the details entered \nEmail:{email} \n Password: {user_password}\n Is it ok to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    # saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                delete_entry()


def delete_entry():
    website_label_input.delete(0, 'end')
    password_input.delete(0, 'end')


#--------------------------SEARCH DETAILS -------------------------#

def find_password():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message='No Data File Found')
    else:
        website_name = website_label_input.get()
        if website_name in data:
            messagebox.showinfo(
                title="YOUR DETAILS", message=f"Website: {website_name} \n password: {data[website_name]['password']}")
        else:
            messagebox.showinfo(
                title="OOPS", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
pad_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pad_lock)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label_input = Entry(width=21)
website_label_input.grid(column=1, row=1, columnspan=1)
website_label_input.focus()
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)


email_name = Label(text="Email/Username:")
email_name.grid(column=0, row=2)
email_name_input = Entry(width=40)
email_name_input.grid(column=1, row=2, columnspan=2)
email_name_input.insert(0, 'obipedro@gmail.com')

password = Label(text="Password:")
password.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(width=35, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
