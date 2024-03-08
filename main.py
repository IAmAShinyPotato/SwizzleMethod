import random

class MultipleChoiceExam:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def generate_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{chr(65 + i)}. {choice}")

    def attempt_solve(self, eliminate_correct_chance=0):
        # Randomly choose an answer
        chosen_answer = random.choice(self.choices)
        print("Attempting to solve...")
        print(f"Randomly chosen answer: {chosen_answer}")

        # Eliminate two incorrect answers that are not the chosen one or the correct one
        incorrect_choices = [choice for choice in self.choices if choice != chosen_answer and choice != self.correct_answer]

        if random.random() < eliminate_correct_chance:
            incorrect_choices.append(self.correct_answer)

        incorrect_eliminated = random.sample(incorrect_choices, min(2, len(incorrect_choices)))
        remaining_choices = [choice for choice in self.choices if choice not in incorrect_eliminated]

        print(f"Eliminating incorrect choices: {incorrect_eliminated}")

        # Switch to one of the remaining choices
        chosen_answer = random.choice(remaining_choices)
        print(f"Switching to the remaining choice: {chosen_answer}")
        return chosen_answer

def run_multiple_choice_exam(question, choices, correct_answer, attempts, eliminate_correct_chance=0):
    correct_count = 0
    total_attempts = attempts

    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}:")
        exam = MultipleChoiceExam(question, choices, correct_answer)
        exam.generate_question()
        attempted_answer = exam.attempt_solve(eliminate_correct_chance)

        if attempted_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect!")

    print(f"\nSummary:")
    print(f"Total attempts: {total_attempts}")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {total_attempts - correct_count}")
    print(f"Percentage correct: {correct_count / total_attempts * 100:.2f}%")

# Parameters
question = "Will Rice ever suck my balls?"
choices = ["Yes", "If Sam Allows It", "No", "No, he'll only itch them"]
correct_answer = "Yes"
attempts = 1000

# Run function
run_multiple_choice_exam(question, choices, correct_answer, attempts, eliminate_correct_chance=0.2)
