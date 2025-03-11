# Prize structure in the style of Who Wants to Be a Millionaire
prizes = [0, 100, 1000, 10000, 100000, 1000000]  # Prize for each question

# Start the game
print("Welcome to Who Wants to Be a Millionaire!")
print("Answer 5 questions correctly to win $1,000,000!\n")

total_prize = 0  # Track the user's total prize money

# Question 1
print(f"Question 1 for ${prizes[1]}:")
print("Question 1: Where is the Eiffel Tower located?\nA: Paris, B: London, C: New York, D: Berlin")
while True:
    user_input = input("Your choice (A, B, C, or D): ").upper()
    if user_input == "A":
        print("Correct! The Eiffel Tower is located in Paris.")
        total_prize = prizes[1]
        print(f"Correct! You've earned ${prizes[1]}.\n")
        break
    elif user_input in ["B", "C", "D"]:
        print("Incorrect. The Eiffel Tower is in Paris (A).")
        print(f"Incorrect. Your total prize is ${total_prize}.\n")
        print("Game over. Better luck next time!")
        exit()
    else:
        print("Invalid choice. Please choose A, B, C, or D.")

# Question 2
print(f"Question 2 for ${prizes[2]}:")
print("Question 2: What is the chemical symbol for water?\nA: CO₂, B: O₂, C: H₂O, D: NaCl")
while True:
    user_input = input("Your choice (A, B, C, or D): ").upper()
    if user_input == "C":
        print("Correct! The chemical symbol for water is H₂O.")
        total_prize = prizes[2]
        print(f"Correct! You've earned ${prizes[2]}.\n")
        break
    elif user_input in ["A", "B", "D"]:
        print("Incorrect. The correct answer is H₂O (C).")
        print(f"Incorrect. Your total prize is ${total_prize}.\n")
        print("Game over. Better luck next time!")
        exit()
    else:
        print("Invalid choice. Please choose A, B, C, or D.")

# Question 3
print(f"Question 3 for ${prizes[3]}:")
print("Question 3: Who wrote 'Romeo and Juliet'?\nA: Charles Dickens, B: William Shakespeare, C: Mark Twain, D: Jane Austen")
while True:
    user_input = input("Your choice (A, B, C, or D): ").upper()
    if user_input == "B":
        print("Correct! William Shakespeare wrote 'Romeo and Juliet'.")
        total_prize = prizes[3]
        print(f"Correct! You've earned ${prizes[3]}.\n")
        break
    elif user_input in ["A", "C", "D"]:
        print("Incorrect. The correct answer is William Shakespeare (B).")
        print(f"Incorrect. Your total prize is ${total_prize}.\n")
        print("Game over. Better luck next time!")
        exit()
    else:
        print("Invalid choice. Please choose A, B, C, or D.")

# Question 4
print(f"Question 4 for ${prizes[4]}:")
print("Question 4: What is the capital of Japan?\nA: Beijing, B: Seoul, C: Bangkok, D: Tokyo")
while True:
    user_input = input("Your choice (A, B, C, or D): ").upper()
    if user_input == "D":
        print("Correct! The capital of Japan is Tokyo.")
        total_prize = prizes[4]
        print(f"Correct! You've earned ${prizes[4]}.\n")
        break
    elif user_input in ["A", "B", "C"]:
        print("Incorrect. The correct answer is Tokyo (D).")
        print(f"Incorrect. Your total prize is ${total_prize}.\n")
        print("Game over. Better luck next time!")
        exit()
    else:
        print("Invalid choice. Please choose A, B, C, or D.")

# Question 5
print(f"Question 5 for ${prizes[5]}:")
print("Question 5: The Pythagorean theorem relates to which geometric shape?\nA: Triangles, B: Circles, C: Squares, D: Rectangles")
while True:
    user_input = input("Your choice (A, B, C, or D): ").upper()
    if user_input == "A":
        print("Correct! The Pythagorean theorem relates to triangles.")
        total_prize = prizes[5]
        print(f"Correct! You've earned ${prizes[5]}.\n")
        break
    elif user_input in ["B", "C", "D"]:
        print("Incorrect. The correct answer is Triangles (A).")
        print(f"Incorrect. Your total prize is ${total_prize}.\n")
        print("Game over. Better luck next time!")
        exit()
    else:
        print("Invalid choice. Please choose A, B, C, or D.")

# Final result
if total_prize == prizes[5]:
    print("Congratulations! You've answered all questions correctly and won $1,000,000!")