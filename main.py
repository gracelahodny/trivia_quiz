
'''
Team Members: Grace Lahodny and Alexandra Tovar
Date: 12/9/2024
CptS 111, Fall 2024
Project Name: Trivia Quiz Game
Description:    This program is a trivia quiz game that reads questions from a CSV file and asks the user to answer them. 
                The user can select a category and answer questions from that category. 
                The user earns 25 points for each correct answer and the final score is displayed at the end of the quiz. 
                The user can choose to play again and choose another category, or exit the game.
Sources:        
https://thefactfile.org/earth-facts/
https://science.nasa.gov/solar-system/solar-system-facts/
https://www.natgeokids.com/uk/discover/science/space/ten-facts-about-space/
https://science.nasa.gov/mercury/
https://www.earthandspaceexpeditioncenter.org/12-space-facts-for-kids/


Modules: csv
'''
# add comments
# add docstrings
# finish chemistry and ocean questions
# add test cases
    # screenshot test cases
# add sources to header
# check spelling
# remove extra files that aren't needed


import csv

def main():

    print(f"{'':-^125}")
    print(f"{'Welcome to the Trivia Quiz Game!':^125}")
    print(f"{'':-^125}")
    
    while True:
        category = select_category()
        questions = read_questions_from_csv('trivia_quiz1.csv', category)
        
        if not questions:
                print("\nNo questions available for the selected category. Please select a different category.")
                continue

        score = 0
        i = 0

        for question in questions:
            i = display_question(i, question)
            user_answer = get_user_answer()
            if check_answer(question, user_answer):
                print("\nCorrect! You earn 25 points.")
                score += 25
            else:
                print(f"\nIncorrect. The correct answer was {question[5]}.")
            if question != questions[-1]:
                print(f"Your current score is: {score}")
                input("\nPress Enter to continue...")
                print(f"{'':-^125}")

        print(f"\n\nCongratulations! You have completed the quiz!")
        input("\nPress Enter to reveal your final score...")
        print(f"\nYour final score is: {score}")
    
        if not play_again():
            break


# 1. Select category
def select_category():
    print("\nPlease select a category:\n")
    print(f"{'':<5}a. Ocean")
    print(f"{'':<5}b. Periodic Table")
    print(f"{'':<5}c. Space")
    category = input("\nEnter your choice (a, b, or c): ").lower()
    while category not in ['a', 'b', 'c']:
        category = input("Invalid input. Please enter a, b, or c: ").lower()
    return category

# 2. Read questions from CSV file
def read_questions_from_csv(filename, category):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)    # each row in file is a list of strings
        questions = list(reader)        # all questions in file stored as a list of lists

    if category == 'a':
        filtered_questions = [question for question in questions if question[6].lower() == 'ocean']
    elif category == 'b':
        filtered_questions = [question for question in questions if question[6].lower() == 'chem']
    elif category == 'c':
        filtered_questions = [question for question in questions if question[6].lower() == 'space']
    else:
        filtered_questions = []
    return filtered_questions

# 3. Display question to user
def display_question(i, question):
    print(f"\n{f'Question {i+1}:':<13}{question[0]:<60}\n")
    print(f"{'':<5}a. {question[1]}")
    print(f"{'':<5}b. {question[2]}")
    print(f"{'':<5}c. {question[3]}")
    print(f"{'':<5}d. {question[4]}")
    i += 1
    return i

# 4. Get user answer
def get_user_answer():
    answer = input("\nPlease enter your answer (a, b, c, or d): ").lower()
    while answer not in ['a', 'b', 'c', 'd']:
        answer = input("Invalid input. Please enter a, b, c, or d: ").lower()
    return answer

# 5. Check if user answer is correct
def check_answer(question, user_answer):
    return user_answer == question[5]

# 6. Ask user if they want to play again
def play_again():       # add case for invalid response
    response = input("\nAwesome job! Would you like to play again? (yes or no): ").lower()
    return response == 'yes'

if __name__ == "__main__":
    main()