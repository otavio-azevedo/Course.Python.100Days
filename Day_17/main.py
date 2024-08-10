from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

end_message = f"""\nYou've completed the quiz!
Your final score was: {quiz_brain.score}/{quiz_brain.question_number}"""

print(end_message)
