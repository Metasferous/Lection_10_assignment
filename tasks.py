"""
1. Write a program that generates 26 text files named A.txt, B.txt,
and so on up to Z.txt.
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains the name of the file
and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
"""
from string import ascii_uppercase as alphabet
from random import randint
import csv


def append_number_to_txt(txt_name: str, number: int):
    file = open(f'{txt_name}.txt', 'a')
    file.write(str(number))
    file.close()


def task_1():
    summary = open('summary.txt', 'w')
    for letter in (alphabet):
        random_number = randint(1, 100)
        append_number_to_txt(letter, random_number)
        current_letter_txt = open(letter + '.txt', 'r')
        summary.write(letter + '.txt :' + current_letter_txt.read() + '\n')
    summary.close()


# task_1()


"""
2. Create a file with some content. As example, you can take this one:
“Lorem ipsum..."
"""

content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'


def task_2():
    with open('first_file.txt', 'w') as file:
        file.write(content)
    with open('first_file.txt', 'r') as first_file:
        with open('second_file.txt', 'w') as second_file:
            second_file.write(first_file.read().upper())


# task_2()


"""
3. Write a program that will simulate user scores in a game.
Create a list with 5 players` names after that simulate 100 rounds for each player.
As a result of the game create a list with the player's name and score (0-1000 range).
And save it to a CSV file.

The file should look like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
...
"""

players = [
    'Wilson',
    'Willow',
    'Wolfgang',
    'Wendy',
    'Woodie'
]


def task_3():
    scores = [['Player', 'Score']]
    for round in range(100):
        for player in players:
            scores.append([player, randint(0, 1000)])
    with open('scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(scores)


task_3()


"""
4. Write a script that reads the data from the previous CSV file
and creates a new file called high_scores.csv
where each row contains the player name and their highest score.
The final score should be sorted by descending to the highest score.

The output CSV file should look like this:
Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345
"""


def task_4():
    scores = []
    with open('scores.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            scores.append(tuple(row))
        players = {player for player, score in scores[1:]}

    highscores = []
    for cur_player in players:
        highscore = max([score for player, score in scores if player == cur_player])
        highscores.append([cur_player, highscore])

    highscores.sort(key=lambda p: p[1], reverse=True)
    highscores = [['Player', 'Highscore']] + highscores
    with open('highscores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(highscores)


task_4()
