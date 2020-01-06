# Comma Code

def list_strings(input_list):
    for i in range(len(input_list)):
        if i < len(input_list) - 1:
            print(input_list[i] + ', ', end = '')
        else:
            print('and ' + input_list[i])

spam = ['apples', 'bananas', 'tofu', 'cats']
list_strings(spam)

# Coin Flip Streaks

import random
numberOfStreaks = 0

experiments = []
for experimentNumber in range(10000):
    trials = []
    for trialNumber in range(100):
        if random.randint(0, 1) == 0:
            trials.insert(trialNumber, 'heads')
        else:
            trials.insert(trialNumber, 'tails')
    experiments.insert(experimentNumber, trials)

    matches = 0
    for trialNumber in range(len(trials)):
        if trials[trialNumber] == trials[trialNumber - 1]:
            matches += 1
        else:
            matches = 0
        if matches == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

y = 0
inner_list = 0
for y in range(len(grid[inner_list])):
    for x in range(len(grid)):
        print(grid[x][y], end = '')
    y += 1
    inner_list += 1
    print()