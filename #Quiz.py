# Quiz
# Greeting Function
print(str("Welcome to the West Ham United Player Quiz"))

# Questions
questions = ("1. Which West Ham Player is currently club captain?",
                       "2. Which trophy was most recently won by West Ham?",
                       "3. What is the name of West Ham's current stadium?",
                       "4. As of the 26/27 season, which league will West Ham play in?",
                       "5. How many FA cups have West Ham won?",
                       "6. How many League Titles have West Ham won?",
                       "7. In what year was West Ham founded?")

answer_choices = (("A. Jarrod Bowen", "B. Tomas Soucek", "C. Callum Wilson", "D. Freddie Potts"),
                   ("A. Championship Play-offs", "B. Premier League", "C. European Cup", "D. European Conference League"),
                   ("A. Boleyn Ground", "B. Upton Park", "C. Olympic Stadium", "D. London Stadium"),
                   ("A. Premier League", "B. Championship", "C. League 1", "D. League 2"),
                   ("A. 0", "B. 1", "C. 2", "D. 3"),
                   ("A. 0", "B. 1", "C. 2", "D. 3"),
                   ("A. 1869", "B. 1895", "C. 1905", "D. 1925"))

answers = ("A", "D", "D", "B", "D", "A", "B")
guesses = []
points = 0
question_number = 0

for question in questions:
    print(question)
    for answer_choice in answer_choices[question_number]:
        print(answer_choice)

    guess = input("Please type your answer (A, B, C or D):")
    guesses.append(guess)
    if guess == answers[question_number]:
        points += 1

        print("Correct")
    else:
        print("Incorrect")
        
    question_number += 1

print("END")
print("You got:", points)

