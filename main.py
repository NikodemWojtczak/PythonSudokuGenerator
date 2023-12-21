import csv
from backtracking_sudoku_generator import BackTrackingSudokuGenerator
import random

bsg = BackTrackingSudokuGenerator()

def generate_100_sudoku_boards():
    list_of_sudoku = []
    while len(list_of_sudoku) != 100:
        tmp = bsg.generate_sudoku()
        if not (tmp in list_of_sudoku):
            list_of_sudoku.append(tmp)
    return list_of_sudoku


def erase_random_numbers(numbers, list_of_sudoku):
    for _ in range(numbers):
        while True:
            randomNumber = random.randint(0, 80)
            if list_of_sudoku[randomNumber] == 0:
                continue
            list_of_sudoku[randomNumber] = 0
            break
    return list_of_sudoku


print("start")

listOfSudokuEasy = generate_100_sudoku_boards()
listOfSudokuMedium = generate_100_sudoku_boards()
listOfSudokuHard = generate_100_sudoku_boards()

for i in range(100):
    listOfSudokuEasy[i] = erase_random_numbers(45, listOfSudokuEasy[i])
    listOfSudokuMedium[i] = erase_random_numbers(54, listOfSudokuMedium[i])
    listOfSudokuHard[i] = erase_random_numbers(63, listOfSudokuHard[i])


with open('listOfSudokuEasy.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(listOfSudokuEasy)

with open('listOfSudokuMedium.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(listOfSudokuMedium)

with open('listOfSudokuHard.csv', 'w', newline='', encoding='utf-8',) as file:
    writer = csv.writer(file)
    writer.writerows(listOfSudokuHard)

print("stop")
