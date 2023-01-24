import random
from pprint import pprint
import yaml

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
SUCCESS = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


class Card:
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return self.name


class Person(Card):
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
    
    def print_attrs(self):
        pprint(self.attributes)

    def __str__(self):
        return f"{self.name} {self.attributes}"

    
class Object:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def __str__(self):
        return f"{self.name} {self.power}"

class Task:
    def __init__(self, name, difficulties, bonus, result):
        self.name = name
        self.difficulties = difficulties
        self.bonus = bonus
        self.result = result
        
    def __str__(self):
        return f"{self.name} {self.difficulties} {self.bonus}"
        
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
    
    def throw_card_by_name(self, card_name):
        if self.current_player == self.player1:
            for card in self.player1_hand:
                if card.name == card_name:
                    self.player1_hand.remove(card)
                    return print(f"Dropped {card_name}")
        else:
            for card in self.player2_hand:
                if card.name == card_name:
                    self.player2_hand.remove(card)
                    return print(f"Dropped {card_name}")

    def draw_person_card(self, player):
        if len(self.person_cards) > 0:
            card = self.person_cards.pop(0)
            if player == self.player1:
                self.player1_hand.append(card)
            else:
                self.player2_hand.append(card)

    def draw_object_card(self, player):
        if len(self.object_cards) > 0:
            card = self.object_cards.pop(0)
            if player == self.player1:
                self.player1_hand.append(card)
            else:
                self.player2_hand.append(card)

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
        print("Start Game, Shuffling Cards!")
        random.shuffle(self.person_cards)
        random.shuffle(self.object_cards)
        random.shuffle(self.tasks)
        for i in range(1):
            self.draw_person_card(self.player1)
            self.draw_person_card(self.player2)
            self.draw_object_card(self.player1)
            self.draw_object_card(self.player2)
        print(f"{self.player1}")
        for i, p in enumerate(self.player1_hand):
            print(f"{i}: {p}")
        print(f"{self.player2}")
        for i, p in enumerate(self.player2_hand):
            print(f"{i}: {p}")
        while len(self.tasks):
            print("\n------New Round------")
            current_task = self.tasks.pop(0)
            self.draw_person_card(self.current_player)
            self.draw_object_card(self.current_player)
            if self.current_player == self.player1:
                print(f"{self.current_player}'s hand")
                for i, p in enumerate(self.player1_hand):
                    print(f"{i}: {p}")
                hand = self.player1_hand
            else:
                print(f"{self.current_player}'s hand")
                for i, p in enumerate(self.player2_hand):
                    print(f"{i}: {p}")
                hand = self.player2_hand
            person_i = input(f"The task is {current_task}, which person should you bring?")
            obj_i = input("Which object?")
            
            task_completed = False
            
            p, o = None,None
            for c_i, c in enumerate(hand):
                if str(c_i) == person_i:
                    p = c
                if str(c_i) == obj_i:
                    o = c
                
            if isinstance(p, Person) and isinstance(o, Object): 
                print(f"You are trying with {p} and {o}")
                attributes = p.attributes
                power = o.power
                curr_o = o
                curr_p = p
                total_score = {k: v + power for k, v in attributes.items()}
                task_completed = True
                for k, v in current_task.difficulties.items():
                    if total_score.get(k, 0) < v+5:
                        task_completed = False
            else:   
                for p_i, p in enumerate((p for p in hand if isinstance(p, Person))):
                    for o_i, o in enumerate((o for o in hand if isinstance(o, Object))):
                        attributes = p.attributes
                        power = o.power
                        curr_o = o
                        curr_p = p
                        total_score = {k: v + power for k, v in attributes.items()}
                        task_completed = True
                        for k, v in current_task.difficulties.items():
                            if total_score.get(k, 0) < v+5:
                                task_completed = False
                                break
                        if task_completed:
                            break
                    if task_completed:
                        break

            def str_replace(inp):
                    return str(inp).replace("[person]", curr_p.name).replace("[object]", curr_o.name)

            if task_completed:
                if current_task.result['success']:
                    print(SUCCESS + str_replace(current_task.result['success'])+ ENDC)
                else:
                    print(f"{SUCCESS} {current_task.name} mit {curr_p.name} und dem/der {curr_o.name} war ein voller Erfolg! {ENDC}")
            else:
                if current_task.result['fail']:
                    print(FAIL + str_replace(current_task.result['fail']) + ENDC)
                else:
                    print(f"{FAIL} {current_task.name}... mit {curr_p.name} und einer/m {curr_o.name} ja klar, wir alle wissen wie das ausgeht! {ENDC}")
                self.tasks.append(current_task)

            if self.current_player == self.player1:
                self.player1_hand.remove(curr_o)
                self.player1_hand.remove(curr_p)
                self.current_player = self.player2
            else:
                self.player2_hand.remove(curr_o)
                self.player2_hand.remove(curr_p)
                self.current_player = self.player1

    @classmethod
    def load_game_data(cls, file_path):
        with open(file_path, 'r') as file:
            game_data = yaml.safe_load(file)
        player1 = game_data["players"][0]
        player2 = game_data["players"][1]
        game = cls(player1, player2)
        for task in game_data["tasks"]:
            game.add_task(Task(task["name"], task["difficulties"], task["bonus"], task["result"]))
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
    game.play()
    game.print_game()

if __name__ == "__main__":
    main()