import random
from pprint import pprint
import yaml

class Person:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return self.name
    
class Object:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def __str__(self):
        return self.name

class Task:
    def __init__(self, name, difficulties):
        self.name = name
        self.difficulties = difficulties
        
    def __str__(self):
        return self.name
        
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.tasks = []
        self.person_cards = []
        self.object_cards = []
        self.player1_hand = []
        self.player2_hand = []

    def add_task(self, task):
        pprint(task)
        self.tasks.append(task)
        
    def add_person_card(self, person):
        self.person_cards.append(person)

    def add_object_card(self, obj):
        self.object_cards.append(obj)

    def print_game(self):
        pprint(self.__dict__)
        self.print_person_cards()
        self.print_obect_cards()

    def print_person_cards(self):
        for card in self.person_cards:
            pprint(card.__dict__)

    def print_obect_cards(self):
        for card in self.object_cards:
            pprint(card.__dict__)

    def roll_dice(self):
        return random.randint(1, 6)
    
    def draw_card(self, player):
        if len(self.person_cards) > 0 and len(self.object_cards) > 0:
            if random.random() < 0.5:
                card = self.person_cards.pop(0)
                if player == self.player1:
                    self.player1_hand.append(card)
                else:
                    self.player2_hand.append(card)
            else:
                card = self.object_cards.pop(0)
                if player == self.player1:
                    self.player1_hand.append(card)
                else:
                    self.player2_hand.append(card)
        elif len(self.person_cards) > 0:
            card = self.person_cards.pop(0)
            if player == self.player1:
                self.player1_hand.append(card)
            else:
                self.player2_hand.append(card)
        elif len(self.object_cards) > 0:
            card = self.object_cards.pop(0)
            if player == self.player1:
                self.player1_hand.append(card)
            else:
                self.player2_hand.append(card)

    def play(self):
        print("Start Game")
        for i in range(1):
            self.draw_card(self.player1)
            self.draw_card(self.player2)
        print(f"{self.player1}")
        for i, p in enumerate(self.player1_hand):
            print(f"{i}: {p}")
        print(f"{self.player2}")
        for i, p in enumerate(self.player2_hand):
            print(f"{i}: {p}")
        for i in range(10):
            print("\n------New Round------")
            current_task = self.tasks.pop(0)
            self.draw_card(self.current_player)
            self.draw_card(self.current_player)
            if self.current_player == self.player1:
                print(f"{self.current_player}'s hand: {self.player1_hand}")
                for i, p in enumerate(self.player1_hand):
                    print(f"{i}: {p}")
                hand = self.player1_hand
            else:
                print(f"{self.current_player}'s hand: {self.player2_hand}")
                for i, p in enumerate(self.player2_hand):
                    print(f"{i}: {p}")
                hand = self.player2_hand
            
            task_completed = False
            for p_i, p in enumerate((p for p in hand if isinstance(p, Person))):
                for o_i, o in enumerate((o for o in hand if isinstance(o, Object))):
                    attributes = p.attributes
                    power = o.power
                    curr_o = o
                    curr_p = p
                    p_i_final = p_i
                    o_i_final = o_i
                    total_score = {k: v + power for k, v in attributes.items()}
                    task_completed = True
                    for k, v in current_task.difficulties.items():
                        if total_score.get(k, 0) < v:
                            task_completed = False
                            break
                    if task_completed:
                        break
                if task_completed:
                    break

            if task_completed:
                print(f"{self.current_player} completed the task {current_task.name} using {curr_p.name} and {curr_o.name}")
            else:
                print(f"{self.current_player} failed the task {current_task.name} using {curr_p.name} and {curr_o.name}")
                self.tasks.append(current_task)

            if self.current_player == self.player1:
                del self.player1_hand[p_i_final]
                del self.player1_hand[o_i_final]
                self.current_player = self.player2
            else:
                self.current_player = self.player1
            

    @classmethod
    def load_game_data(cls, file_path):
        with open(file_path, 'r') as file:
            game_data = yaml.safe_load(file)
        player1 = game_data["players"][0]
        player2 = game_data["players"][1]
        game = cls(player1, player2)
        for task in game_data["tasks"]:
            game.add_task(Task(task["name"], task["difficulties"]))
        for person in game_data["person_cards"]:
            game.add_person_card(Person(person["name"], person["attributes"]))
        for obj in game_data["object_cards"]:
            game.add_object_card(Object(obj["name"], obj["power"]))
        return game
        
        

def main():
    player1 = "Hendrik"
    player2 = "Frederike"
    
    file_path = "game_data.yaml"
    game = Game.load_game_data(file_path)   
    #game.add_task(Task("Climb a mountain", 5))
    #game.add_task(Task("Solve a puzzle", 3))
    #game.add_task(Task("Charm a dragon", 4))
    #game.add_person_card(Person("Tom", {"strength": 7, "intelligence": 8, "charm": 6, "luck": 3}))
    #game.add_person_card(Person("Sara", {"strength": 4, "intelligence": 9, "charm": 7, "luck": 5}))
    #game.add_object_card(Object("Axe", 2))
    #game.add_object_card(Object("Book of spells", 4))
    game.play()
    game.print_game()

if __name__ == "__main__":
    main()