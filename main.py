
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
https://www.natgeokids.com/uk/discover/geography/general-geography/ocean-facts/

Modules: csv
'''

import csv

def main():
    '''
    Main function to run the Trivia Quiz Game.
    This function displays a welcome message and continuously prompts the user to select a category for the quiz.
    It reads questions from a CSV file based on the selected category and presents them to the user one by one.
    The user's answers are checked, and points are awarded for correct answers. The user's score is displayed
    after each question, and the final score is shown at the end of the quiz. The user is given the option to
    play again or exit the game.
    '''
    # Display welcome message
    print(f"{'':-^125}")
    print(f"{'Welcome to the Trivia Quiz Game!':^125}")
    print(f"{'':-^125}")
    
    # Prompt user to select a category
    while True:
        category = select_category()
        questions = read_questions_from_csv('trivia_quiz.csv', category)   # read questions from CSV file
    
    # If no questions are available for the selected category, prompt user to select a different category
        if not questions:            
                print("\nNo questions available for the selected category. Please select a different category.")
                continue
    
    # initialize score and question index
        score = 0           
        i = 0

    # iterate through questions
        for question in questions:              
            i = display_question(i, question)               # display question to user
            user_answer = get_user_answer()
            if check_answer(question, user_answer):         # check if user answer is correct
                print("\nCorrect! You earn 25 points.")     # award points for correct answers
                score += 25
            else:
                print(f"\nIncorrect. The correct answer was {question[5]}.")
            if question != questions[-1]:
                print(f"Your current score is: {score}")    # display current score
                input("\nPress Enter to continue...")
                print(f"{'':-^125}")

        print(f"\n\nCongratulations! You have completed the quiz!")     # display completion message
        input("\nPress Enter to reveal your final score...")    
        print(f"\nYour final score is: {score}")                        # display final score
    
        if not play_again():                            # ask user if they want to play again or exit the game
            break


# 1. Select category
def select_category():
    '''
    Prompts the user to select a category from a list of options and returns the selected category.
    The function displays three categories: Ocean, Periodic Table, Space.
    It then prompts the user to enter their choice as 'a', 'b', or 'c'. If the user enters an invalid choice,
    they are prompted to enter a valid choice until a valid input is provided.
    The selected category as a lowercase string ('a', 'b', or 'c') is returned.
    '''
    print("\nPlease select a category:\n")                                      # Display category options to the user
    print(f"{'':<5}a. Ocean")
    print(f"{'':<5}b. Periodic Table")
    print(f"{'':<5}c. Space")
    category = input("\nEnter your choice (a, b, or c): ").lower()              # Prompt the user to enter their choice
    while category not in ['a', 'b', 'c']:                                          # Validate user input
        category = input("Invalid input. Please enter a, b, or c: ").lower()        # prompt again if invalid
    return category                                                             # Return the selected category

# 2. Read questions from CSV file
def read_questions_from_csv(filename, category):
    '''
    Reads questions from a CSV file and filters them based on the specified category.
    The function reads questions from the specified CSV file and filters them based on the selected category.
    The category is specified as a lowercase string ('a', 'b', or 'c') and is used to filter the questions.
    The function returns a list of filtered questions based on the specified category.
    Each question is represented as a list of strings.
    Returns an empty list if the category does not match 'a', 'b', or 'c'.
    '''
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)                    # each row in file is a list of strings
        questions = list(reader)                        # all questions in file stored as a list of lists

    if category == 'a':
        filtered_questions = [question for question in questions if question[6].lower() == 'ocean']
    elif category == 'b':
        filtered_questions = [question for question in questions if question[6].lower() == 'chem']
    elif category == 'c':
        filtered_questions = [question for question in questions if question[6].lower() == 'space']
    else:
        filtered_questions = []          # returns empty list if category does not match 'a', 'b', or 'c'
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