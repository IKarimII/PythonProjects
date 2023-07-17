from quiz import Question
from data import question_data
from QuizBrain import QuizzBrain

question_bank = []
for i in question_data:
    new_question = Question(i['question'], i['correct_answer'])
    question_bank.append(new_question)
    quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
