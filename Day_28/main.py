from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{'00'}:{'00'}")
    check_mark_txt_label.config(text = "" )
    timer_txt_label.configure(text = "Timer", fg=GREEN )

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #count_down(5)
    global reps
    reps +=1
    
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN * 60)        
        timer_txt_label.configure(text = "Break", fg=RED )
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_txt_label.configure(text = "Break", fg=PINK )
    else:
        count_down(WORK_MIN * 60)
        timer_txt_label.configure(text = "Working", fg=GREEN )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_mins = floor(count / 60)
    count_secs = count % 60
    if count_secs == 0:
        count_secs = "00"
    elif count_secs < 10:
        count_secs = "0" + str(count_secs)

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()

        marks = floor(reps/2)
        check_mark_txt_label.config(text = "✔" * marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "Day_28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text ="00:00", fill = "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_txt_label = Label(text="Timer",  fg = GREEN, bg = YELLOW,  font = (FONT_NAME, 40,"bold"))
timer_txt_label.grid(row=0, column=1)

check_mark_txt_label = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20,"bold"))
check_mark_txt_label.grid(row=3, column=1)

start_btn =Button(text="Start", command= start_timer)
start_btn.grid(row=2, column=0)

reset_btn =Button(text="Reset", command = reset_timer)
reset_btn.grid(row=2, column=2)


window.mainloop()