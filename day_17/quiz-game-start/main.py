from question_model import Question
from data import question_data

question_bank = []

for x in question_data:
    # print(f"{x['text']}:{x['answer']}")
    question = Question(x['text'], x['answer'])
    question_bank.append(question)

# for x in question_bank:
#     print(x.text)

quiz_brain = []
