import random

# Quiz questions, answers, and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. Japan", "B. China", "C. Thailand", "D. India"],
        "answer": "A"
    },
]

# Prize structure for each question
prizes = [100, 200, 500, 1000, 5000]
lifelines_used = {"1. 50-50": False, "2. phone a friend": False, "3. ask the audience": False}

# Helper function to display options
def display_options(options):
    for option in options:
        print(option)

# Lifelines
def fifty_fifty(question_data):
    options = question_data["options"]
    answer = question_data["answer"]
    correct_option = next(opt for opt in options if opt.startswith(answer))
    other_option = random.choice([opt for opt in options if not opt.startswith(answer)])
    print("50-50 Lifeline: Here are two options.")
    print(correct_option)
    print(other_option)

def phone_a_friend(answer):
    print(f"Your friend suggests the answer might be '{answer}'.")

def ask_the_audience(answer):
    print("Audience Poll:")
    print(f"  75% think the answer is '{answer}'")
    print("  15% for another option and 10% divided among the remaining options.")

# Main quiz loop
for i, question_data in enumerate(questions):
    print(f"\nQuestion {i+1} for ${prizes[i]}:")
    print(question_data["question"])
    display_options(question_data["options"])

    # Ask if the player wants to use a lifeline
    if any(not used for used in lifelines_used.values()):
        use_lifeline = input("Do you want to use a lifeline? (yes/no): ").lower()
        if use_lifeline == "yes":
            print("Available lifelines:")
            for name, used in lifelines_used.items():
                if not used:
                    print(f"{name}")
            lifeline_choice = input("Choose a lifeline: ").lower()
            
            if lifeline_choice == "50-50" or 1 and not lifelines_used["1. 50-50"]:
                fifty_fifty(question_data)
                lifelines_used["1. 50-50"] = True
            elif lifeline_choice == "phone a friend" or 2 and not lifelines_used["2. phone a friend"]:
                phone_a_friend(question_data["answer"])
                lifelines_used["2. phone a friend"] = True
            elif lifeline_choice == "ask the audience" or 3 and not lifelines_used["3. ask the audience"]:
                ask_the_audience(question_data["answer"])
                lifelines_used["3. ask the audience"] = True
            else:
                print("Invalid lifeline or already used. Moving on without lifeline.")

    # Get user's answer
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    # Check answer
    if answer == question_data["answer"]:
        print(f"Correct! You've won ${prizes[i]}!\n")
    else:
        print(f"Wrong answer! The correct answer was '{question_data['answer']}'. Game over!")
        break
else:
    print("Congratulations! You've won the game and earned $1,000,000!")
