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
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Neptune"],
        "answer": "C"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
        "answer": "B"
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["A. 1905", "B. 1912", "C. 1920", "D. 1930"],
        "answer": "B"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["A. Brain", "B. Liver", "C. Skin", "D. Lungs"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Claude Monet", "D. Leonardo da Vinci"],
        "answer": "D"
    }
]

# Prize structure for each question
prizes = [100, 200, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
lifelines_used = {"50-50": False, "phone a friend": False, "ask the audience": False}

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

def ask_the_audience(question_data):
    correct_answer = question_data["answer"]
    correct_percentage = random.randint(60, 80)
    remaining_percentage = 100 - correct_percentage
    other_percentages = random.sample(range(0, remaining_percentage), 3)
    other_percentages.sort()
    
    percentages = [other_percentages[0],
                   other_percentages[1] - other_percentages[0],
                   other_percentages[2] - other_percentages[1],
                   remaining_percentage - other_percentages[2]]
    
    options_with_percentages = []
    for i, option in enumerate(question_data["options"]):
        if option.startswith(correct_answer):
            options_with_percentages.append((option, correct_percentage))
        else:
            options_with_percentages.append((option, percentages.pop(0)))
    
    print("Audience Poll:")
    for option, percentage in options_with_percentages:
        print(f"  {option}: {percentage}%")

# Main quiz loop
for i, question_data in enumerate(questions):
    print(f"\nQuestion {i+1} for ${prizes[i]}:")
    print(question_data["question"])
    display_options(question_data["options"])

    # Offer the option to back out
    back_out = input(f"Do you want to answer the question, use a lifeline, or back out with ${prizes[i-1] if i > 0 else 0}? (answer/lifeline/back out): ").lower()
    
    if back_out == "back out":
        print(f"Congratulations! You chose to back out and take home ${prizes[i-1] if i > 0 else 0}.")
        break

    elif back_out == "lifeline" and any(not used for used in lifelines_used.values()):
        print("Available lifelines:")
        lifeline_map = {"1": "50-50", "2": "phone a friend", "3": "ask the audience"}
        for key, name in lifeline_map.items():
            if not lifelines_used[name]:
                print(f"{key}. {name}")

        lifeline_choice = input("Choose a lifeline (1, 2, 3 or name): ").lower()
        
        if (lifeline_choice == "1" or lifeline_choice == "50-50") and not lifelines_used["50-50"]:
            fifty_fifty(question_data)
            lifelines_used["50-50"] = True
        elif (lifeline_choice == "2" or lifeline_choice == "phone a friend") and not lifelines_used["phone a friend"]:
            phone_a_friend(question_data["answer"])
            lifelines_used["phone a friend"] = True
        elif (lifeline_choice == "3" or lifeline_choice == "ask the audience") and not lifelines_used["ask the audience"]:
            ask_the_audience(question_data)
            lifelines_used["ask the audience"] = True
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
