from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 120,
                                            text="Question here",
                                            fill="black",
                                            font=("Arial", 20, "italic"),
                                            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.button_correct = Button(image=self.true_image, command=self.check_true)
        self.button_correct.grid(row=2, column=0, pady=20)

        self.button_false = Button(image=self.false_image, command=self.check_false)
        self.button_false.grid(row=2, column=1, pady=20)

        self.label_score = Label(text=f"score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question_text)
        else:
            self.canvas.itemconfig(self.text, text="You have completed all the questions")
            self.button_correct.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_true(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def check_false(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.score += 1
            self.label_score.config(text=f"score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

