# Henrika

This is a simple game written in Python that allows two players to compete against each other to complete tasks using a combination of person and object cards.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3
* yaml library

### Installing

Clone the repository and install the required libraries:

git clone https://github.com/mwessley/henrika.git
pip install -r requirements.txt


### Running the game

You can run the game by executing the `game.py` script:

python game.py


## Game rules

- There are two players and each round they take turns rolling the dice.
- At each turn, the player draws one person card and one object card.
- The player can use a combination of one person card and one object card to complete a task.
- The tasks are laid out in a circle on the board in front of the player.
- Each task has a difficulty for each attribute of the person cards (strength, intelligence, agility, charm)
- If a player completes a task, they get a point.
- If a player fails a task, the task is put back in the circle for the next player to try.
- The game ends when all tasks have been completed or all players have had a turn.
- Each task has a bonus when using a specific combination of object and person
- The game data (players, person cards, object cards, tasks) is loaded from a yaml file.

## Game Data

The game data (players, person cards, object cards, tasks) is stored in a yaml file.
You can change the data and add new players, person cards, object cards, and tasks to the yaml file and re-run the game.

## Contributing

If you would like to contribute to the project, please fork the repository and create a pull request with your changes.

## Authors

* **Your Name** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* This game is inspired by a classic board game.

## Next steps

* Add a GUI to the game
* Add more features to the game like different level of tasks, different cards, etc.
* Add support for more than two players
* Add a scoring system to determine the winner
* Add a save and load feature to allow players to save and resume a game later.