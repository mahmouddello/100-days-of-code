# 1 - Ask for Question
# 2 - checking if answers is correct
# 3 - checking if we're in the end of quiz
class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    # 3
    def still_has_question(self):
        return self.question_number < len(self.question_list)  # Return True if quiz didn't end

    # 2
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong.")
        print(f'Correct answer : {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print()  # new line

    # 1
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1  # Once we got hold the previous number we increase by 1 for print formatting.
        user_answer = input(f'Q.{self.question_number}: {question.text} (True/False)?').lower()
        self.check_answer(user_answer, question.answer)
