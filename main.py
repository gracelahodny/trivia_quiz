
# ask user for number of players
# max 1-2 players
def num_players():
    while True:
        try:
            players = int(input("Enter the number of players (1 or 2): "))
            if players == 1 or players == 2:
                return players
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def player_names():
    def player_names(players):
        names = []
        for i in range(players):
            name = input(f"Enter the name for player {i + 1}: ")
            names.append(name)
        return names

def select_category():
    a = 'Earth Facts'
    b = 'Ocean Facts'
    c = 'Space Facts'
    category = input("Select a category: ()")
        #print options for user to select from
    return category

def main():
    # welcome message for start of game
    print("Welcome to the Trivia Quiz!")
    # create while True to give user option to play or exit with a break
    players = num_players()
        # check for valid number of player input
    player_names = player_names(players)
    category = select_category()
    print(f"Players: {player_names}")
    print(f"Category: {category}")

# call to main()



