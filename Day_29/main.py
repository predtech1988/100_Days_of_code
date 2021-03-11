from tkinter import *
from tkinter import messagebox
import passwd_gerator as ps
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password_input.delete(0, END)
    password_input.insert(0,ps.get_random_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = website_input.get()
    name = email_name_input.get()
    passwd =password_input.get()
    data = f" {site} | {name} | {passwd} \n"

    if (len(site) == 0 or len(passwd) == 0):
        messagebox.showerror(title="Error", message="Name or password missing!")
        return

    is_saving = messagebox.askokcancel(title=site, message="Do you want to save it?")
    if is_saving:
        with open("Day_29/saved.txt", "a+") as f:
            f.write(data)
        website_input.delete(0, END)
        password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Row 0
canvas = Canvas(width=200, height=200) #, highlightthickness=0
logo_img = PhotoImage(file = "Day_29/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row=0, column=1)

#Row 1
website_txt_label = Label(text = "Website:")
website_txt_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

#Row 2
email_name_txt_label = Label(text = "Email/Username:")
email_name_txt_label.grid(row=2, column=0)

email_name_input = Entry(width=35)
email_name_input.insert(0, "angela@gmail.com")
email_name_input.grid(row=2, column=1, columnspan = 2)

#Row 3
password_txt_label = Label(text = "Password")
password_txt_label.grid(row=3, column =0)

password_input = Entry(width=17)
password_input.grid(row=3, column =1)

generate_password_btn = Button(text="Generate Password", command=gen_password)
generate_password_btn.grid(row=3, column =2)

#Row 4
add_password_btn =Button(text="Add", width =36, command = save_password)
add_password_btn.grid(row=4, column = 1, columnspan = 2)





window.mainloop()