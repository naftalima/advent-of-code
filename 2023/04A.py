total = 0

with open("puzzle-input/cards4.txt") as file:
    for line in file:
        game, numbers = line.split(':')
        winning_numbers, have_numbers =  numbers.split('|')
        have_numbers = have_numbers.strip().split()
        winning_numbers = winning_numbers.strip().split()

        points = 0
        for i in have_numbers:
            for j in winning_numbers:
                if i == j :
                    points += 1

        if points != 0:  total +=  (2**(points-1))

print(total)


