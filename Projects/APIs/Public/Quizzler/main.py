from question_model import Question
from quiz_brain import QuizBrain
import requests
import ui

parameters = {
    'amount': 10.,
    'type': 'boolean',
    'category': 18
}
response = requests.get(url='https://opentdb.com/api.php?',params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
interface = ui.QuizzlerInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
