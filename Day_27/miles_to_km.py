from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=60, pady=60)

# Input
miles_input = Entry(width=8, )
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# is equal to
equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
# miles
km_count_label = Label(text="0")
km_count_label.grid(row=1, column=1)

# Km
km_label = Label(text="Km")
km_label.grid(row=1, column=2)
def calculate():
    mi = int(miles_input.get())
    km_count_label["text"] = round(mi*1.609, 1)

    pass
# Calculate
calculate_btn = Button(text="Calculate", command = calculate)
calculate_btn.grid(row=2, column=1)


window.mainloop()
