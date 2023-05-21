class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def display_question(self):
        current_question = self.get_current_question()
        print(f"Question {self.current_question_index + 1}: {current_question.text}")

        for i, choice in enumerate(current_question.choices):
            print(f"{i + 1}. {choice}")

    def handle_answer(self, user_answer):
        current_question = self.get_current_question()

        if current_question.check_answer(user_answer):
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")

        self.current_question_index += 1

    def display_score(self):
        print(f"Your score: {self.score}/{len(self.questions)}")


# Sample questions
questions = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin"], 1),
    Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus"], 1),
    Question("What is the largest ocean on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"], 1),
]

# Create a quiz instance
quiz = Quiz(questions)

# Start the quiz
while quiz.current_question_index < len(quiz.questions):
    quiz.display_question()
    user_answer = input("Your answer (enter the number): ")
    quiz.handle_answer(int(user_answer))

# Display the final score
quiz.display_score()
