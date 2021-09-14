from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    # print(f"{x['text']}:{x['answer']}")
    question = Question(x['question'], x['correct_answer'])
    question_bank.append(question)

# for x in question_bank:
#     print(x.text)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")