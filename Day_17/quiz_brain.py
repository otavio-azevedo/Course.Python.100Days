class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Current score: {self.score}")
        input_answer = input(f"Q.{self.question_number} {
            current_question.text} (True/False):")

        self.check_answer(input_answer, current_question.answer)

    def still_has_question(self):
        return False if len(self.question_list) <= self.question_number else True

    def check_answer(self, input_answer, correct_anser):
        if input_answer.lower() == correct_anser.lower():
            self.score += 1
            print("Correct...")
            return True
        else:
            print("Incorrect...")
            return False
