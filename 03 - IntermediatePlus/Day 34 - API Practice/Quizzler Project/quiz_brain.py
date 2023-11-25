import html


# Note ⚠:
# The data we're retrieving from the API contains HTML escape characters.
# To unescape these characters, we need to use the built-in HTML module in Python and apply
# the unescape function in the quiz_brain.py file to the question text that the user is receiving.
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # unescape the html entities in question text that we're receiving from the API response.
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text} (True/False): "
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False
        #
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
