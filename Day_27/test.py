from  tkinter import *

window = Tk()
window.title("GUI test")
window.minsize(width=500, height=300)



#Labels

my_label = Label(text ="Test GUI app")
my_label.grid(row=0, column=0)

input_ = Entry(width=10)
input_.grid(row=2, column=3)

def change_text():
    my_label["text"] = input_.get()

#Butttons
change_text_button = Button(text="Change text", command= change_text)
change_text_button.grid(row=1, column=1)

button_2 = Button(text="Second")
button_2.grid(row=0, column=2)


window.mainloop()

