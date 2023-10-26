# Create a Move_Tutor Class that inherits from the Pokemon parent class.
# This class should have a list attribute (move_list) that holds pokemon moves which should be populated with an api call to the PokeApi moves section (just like we did with abilities and types in the Pokemon class example). Finally create a class method that teaches your pokemon up to 4 moves. This method should take in a user input to what move they would like to teach and do a membership inside the move_list. If the move exists inside the move_list the pokemon can learn that move and append to the final taught_moves list.

import requests

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.move_list = []
        self.taught_moves = []
        self.get_move_list()

    def get_move_list(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}/")
        if r.status_code == 200:
            data = r.json()
        else:
            print(f"Please check the spelling of your Pokemon and try again: {r.status_code}")
            return
        self.move_list = [move["move"]["name"] for move in data["moves"]]

    def show_moves(self):
        print(f"Available moves for {self.name.title()}: {self.move_list}")

class Move_Tutor(Pokemon):
    def teach_move(self):
        while len(self.taught_moves) < 4:
            new_move = input(f"Enter the move you want to teach {self.name.title()} (or type 'done' to finish): ").lower()
            if new_move == 'done':
                break
            if new_move in self.move_list:
                self.taught_moves.append(new_move)
                print(f"{self.name.title()} has learned {new_move}!")
            elif new_move in self.taught_moves:
                print(f"{self.name.title()} already knows {new_move}.")
            else:
                print(f"{new_move} is not a move that can be taught to {self.name}.")


charmander = Move_Tutor("charmander") 
charmander.show_moves()
charmander.teach_move()

print(f"{charmander.name.title()} knows the following moves: {charmander.taught_moves}")


# pikachu.teach_move()

# pikachu.show_moves()