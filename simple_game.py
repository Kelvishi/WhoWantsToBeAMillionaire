def question_1(choice):
    match choice.upper():
        case "A":
            return True, "Correct! The Eiffel Tower is located in Paris."
        case "B":
            return False, "Incorrect. London is not where the Eiffel Tower is located."
        case "C":
            return False, "Incorrect. New York is not where the Eiffel Tower is located."
        case "D":
            return False, "Incorrect. Berlin is not where the Eiffel Tower is located."
        case _:
            return False, "Invalid choice. Please choose A, B, C, or D."

def question_2(choice):
    match choice.upper():
        case "C":
            return True, "Correct! The chemical symbol for water is H₂O."
        case "A":
            return False, "Incorrect. CO₂ is the chemical symbol for carbon dioxide."
        case "B":
            return False, "Incorrect. O₂ is the chemical symbol for oxygen gas."
        case "D":
            return False, "Incorrect. NaCl is the chemical symbol for salt."
        case _:
            return False, "Invalid choice. Please choose A, B, C, or D."

def question_3(choice):
    match choice.upper():
        case "B":
            return True, "Correct! William Shakespeare wrote 'Romeo and Juliet'."
        case "A":
            return False, "Incorrect. Charles Dickens did not write 'Romeo and Juliet'."
        case "C":
            return False, "Incorrect. Mark Twain did not write 'Romeo and Juliet'."
        case "D":
            return False, "Incorrect. Jane Austen did not write 'Romeo and Juliet'."
        case _:
            return False, "Invalid choice. Please choose A, B, C, or D."

def question_4(choice):
    match choice.upper():
        case "D":
            return True, "Correct! The capital of Japan is Tokyo."
        case "A":
            return False, "Incorrect. Beijing is the capital of China."
        case "B":
            return False, "Incorrect. Seoul is the capital of South Korea."
        case "C":
            return False, "Incorrect. Bangkok is the capital of Thailand."
        case _:
            return False, "Invalid choice. Please choose A, B, C, or D."

def question_5(choice):
    match choice.upper():
        case "A":
            return True, "Correct! The Pythagorean theorem relates to triangles."
        case "B":
            return False, "Incorrect. The Pythagorean theorem does not relate to circles."
        case "C":
            return False, "Incorrect. The Pythagorean theorem does not relate to squares."
        case "D":
            return False, "Incorrect. The Pythagorean theorem does not relate to rectangles."
        case _:
            return False, "Invalid choice. Please choose A, B, C, or D."

# Function to ask a question and handle user input
def ask_question(question_text, question_function):
    print(question_text)
    while True:
        user_input = input("Your choice (A, B, C, or D): ")
        is_correct, result = question_function(user_input)
        if not result.startswith("Invalid"):
            print(result)
            return is_correct  # Return whether the answer was correct
        else:
            print(result)  # Print the error message and prompt again

# Prize structure in the style of Who Wants to Be a Millionaire
prizes = [0, 100, 1000, 10000, 100000, 1000000]  # Prize for each question

# Start the game
print("Welcome to Who Wants to Be a Millionaire!")
print("Answer 5 questions correctly to win $100,000!\n")

total_prize = 0  # Track the user's total prize money

# Ask each question explicitly
print(f"Question 1 for ${prizes[1]}:")
if ask_question(
    "Question 1: Where is the Eiffel Tower located?\nA: Paris, B: London, C: New York, D: Berlin",
    question_1
):
    total_prize = prizes[1]
    print(f"Correct! You've earned ${prizes[1]}.\n")
else:
    print(f"Incorrect. Your total prize is ${total_prize}.\n")
    print("Game over. Better luck next time!")
    exit()

print(f"Question 2 for ${prizes[2]}:")
if ask_question(
    "Question 2: What is the chemical symbol for water?\nA: CO₂, B: O₂, C: H₂O, D: NaCl",
    question_2
):
    total_prize = prizes[2]
    print(f"Correct! You've earned ${prizes[2]}.\n")
else:
    print(f"Incorrect. Your total prize is ${total_prize}.\n")
    print("Game over. Better luck next time!")
    exit()

print(f"Question 3 for ${prizes[3]}:")
if ask_question(
    "Question 3: Who wrote 'Romeo and Juliet'?\nA: Charles Dickens, B: William Shakespeare, C: Mark Twain, D: Jane Austen",
    question_3
):
    total_prize = prizes[3]
    print(f"Correct! You've earned ${prizes[3]}.\n")
else:
    print(f"Incorrect. Your total prize is ${total_prize}.\n")
    print("Game over. Better luck next time!")
    exit()

print(f"Question 4 for ${prizes[4]}:")
if ask_question(
    "Question 4: What is the capital of Japan?\nA: Beijing, B: Seoul, C: Bangkok, D: Tokyo",
    question_4
):
    total_prize = prizes[4]
    print(f"Correct! You've earned ${prizes[4]}.\n")
else:
    print(f"Incorrect. Your total prize is ${total_prize}.\n")
    print("Game over. Better luck next time!")
    exit()

print(f"Question 5 for ${prizes[5]}:")
if ask_question(
    "Question 5: The Pythagorean theorem relates to which geometric shape?\nA: Triangles, B: Circles, C: Squares, D: Rectangles",
    question_5
):
    total_prize = prizes[5]
    print(f"Correct! You've earned ${prizes[5]}.\n")
else:
    print(f"Incorrect. Your total prize is ${total_prize}.\n")
    print("Game over. Better luck next time!")
    exit()

# Final result
if total_prize == prizes[5]:
    print("Congratulations! You've answered all questions correctly and won $1,000,000!")