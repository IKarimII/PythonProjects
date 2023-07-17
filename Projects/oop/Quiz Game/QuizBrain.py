class QuizzBrain:
    def __init__(self, q_list):
        self.quiz_num = 0
        self.quiz_list = q_list
        self.score = 0
        self.total_quest = 0

    def still_has_questions(self):
        if self.quiz_num < len(self.quiz_list):
            return True
        else:
            print("Final score: ", self.score, '/', len(self.quiz_list))

    def next_question(self):
        new_question = self.quiz_list[self.quiz_num]
        self.quiz_num += 1

        user_answer = input(f"Q.{self.quiz_num}: {new_question.question}   |True or False?   >")
        self.check_answer(user_answer, new_question.answer)
        print('\n')

    def check_answer(self, user_answer, quiz_answer):
        if user_answer.lower() == quiz_answer.lower():
            self.total_quest +=1
            self.score += 1
            print("You Got it Right")
            print(self.score, '/', self.total_quest)

        else:
            print(f"You Got It WRONG\nThe correct answer was: {quiz_answer}")
            self.total_quest += 1
            print(self.score, '/', self.total_quest)
