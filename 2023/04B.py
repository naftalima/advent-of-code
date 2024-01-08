card_instances = {}

count = 0
with open("puzzle-input/cards4.txt") as file:
    for line in file:
        game, numbers = line.split(':')
        game = game.split()[1]
        winning_numbers, have_numbers =  numbers.split('|')
        have_numbers = have_numbers.strip().split()
        winning_numbers = winning_numbers.strip().split()

        if not game in card_instances:  card_instances[game] = 1

        points = 0
        for i in have_numbers:
            for j in winning_numbers:
                if i == j : points += 1

        for k in range(int(game)+1,  int(game)+points+1):
            if str(k) in card_instances:
                card_instances[str(k)] += card_instances[str(game)]
            else: card_instances[str(k)] = card_instances[str(game)]+1

print(card_instances)
res = 0
for _, i in card_instances.items():
    res += i

print(res)