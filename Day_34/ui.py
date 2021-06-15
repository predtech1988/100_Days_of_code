from  tkinter import *
from quiz_brain import QuizBrain

UI_FONTS = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(bg = THEME_COLOR, padx=20, pady=20)
        self.quiz = quiz_brain
        #------UI Setup------
        self. score_label = Label(text=f"Score: {self.quiz.score}",background=THEME_COLOR, 
                            fg="white", highlightthickness=0) #add scores var
        self.score_label.grid(row = 0, column =1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text((150, 125),text="Some text", 
                            fill=THEME_COLOR, width=280,
                            font=("Arial", 20, "italic"))
        self.canvas.grid(row = 1, column =0, columnspan=2, pady=30)


        #Buttons
        self.ok_btn = Button()
        self.wrong_btn = Button()

        ok_btn_img = PhotoImage(file="./images/true.png")
        wrong_btn_img = PhotoImage(file="./images/false.png")

        self.ok_btn.config(image = ok_btn_img, command= self.true_btn_command)
        self.wrong_btn.config(image = wrong_btn_img, command= self.false_btn_command)

        self.ok_btn.grid(row = 2, column =0, pady=30)
        self.wrong_btn.grid(row = 2, column =1, pady=30)

        #Code
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text) 
        else:
            self.ok_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_text, 
            text=f"There is no new question. \n You are {self.quiz.score} / {len(self.quiz.question_list)} ")
            

    def true_btn_command(self):
        result = self.quiz.check_answer(True)        
        self.score_label["text"] = f"Score: {self.quiz.score}"
        #self.quiz.score
        self.give_feedback(result)
        self.get_next_question()


    def false_btn_command(self):
        result = self.quiz.check_answer(False)
        self.give_feedback(result)
        self.get_next_question()


    def give_feedback(self, result: bool):
        if result:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.change_canvas_background)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.change_canvas_background)

    def change_canvas_background(self):
        self.canvas.configure(bg="white")




