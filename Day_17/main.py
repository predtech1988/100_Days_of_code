from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

#question_bank.append(Question("test", True))
#question_1 = Question("test", True)
# print(question_1.text)
# print(question_1.answer)
#print(len(question_bank))


for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have ended the quiz")
print(f"Your final score is: {quiz.score} / {len(question_bank)}")