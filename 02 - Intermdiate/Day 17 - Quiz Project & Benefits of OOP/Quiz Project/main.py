from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # Retrieving data from the dictionary and passing as argument
    new_q = Question(question['question'], question['correct_answer'])
    question_bank.append(new_q)
    # Creating question object and getting data from the question_data list, then appending it to the question_bank list

# Converting the format of questions to object to grant easy access to the question text and answer.
print(question_bank[0].answer)  # Example of easy access

QuizBrain(q_list=question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Completed the quiz")
print(f'Your final score is {quiz.score}/{len(question_bank)}')
