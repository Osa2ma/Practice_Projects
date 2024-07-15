from tkinter import *
from tkinter import messagebox
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] +[choice(symbols) for _ in range(nr_symbols)]+[choice(numbers) for _ in range(nr_numbers)]


    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get())==0:
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website_entry.get(),message=f"These are the details entered: \nEmail: {email_username_entry.get()} \npassword:{password_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt",'a') as file:
                file.write(f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
            email_username_entry.delete(0,"end")
            password_entry.delete(0,"end")
            website_entry.delete(0,"end")
    
    
    






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, columnspan=2)


website_label = Label(text="Website:", bg="white")
email_username_label = Label(text="Email/Username:", bg="white")
password_label = Label(text="Password:", bg="white")
website_label.grid(row=1, column=0, sticky="e")
email_username_label.grid(row=2, column=0, sticky="e")
password_label.grid(row=3, column=0, sticky="e")


website_entry = Entry(width=35)
email_username_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")
website_entry.focus()
email_username_entry.insert(0,"yourusualusedemail@gmail.com")


gen_password = Button(text="Generate Password", bg="white",command=generate)
add_button = Button(text="Add", width=36, bg="white",command=save)
gen_password.grid(row=3, column=2, sticky="w")
add_button.grid(row=4, column=1, columnspan=2)

# Configure grid row and column weights to make the UI look better
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(4, weight=1)

window.mainloop()
