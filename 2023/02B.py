total_powers = 0

with open("puzzle-input/cards.txt") as file:
    for line in file:
        game, sets = line.split(':')
        game_number = int(game.split()[1])
        max_hand = [0,0,0] # [R,G,B]

        sets = sets.split(';')
        sets = [s.strip() for s in sets]

        for plays in sets:
            plays = plays.split(',')

            for play in plays:
                qty, color = play.strip().split(' ')
                qty = int(qty)
                if 'red' in color: max_hand[0] = max(max_hand[0], qty)
                elif 'green' in color: max_hand[1] = max(max_hand[1], qty)
                elif 'blue' in color: max_hand[2] = max(max_hand[2], qty)
        
        power = max_hand[0] * max_hand[1] * max_hand[2]

        total_powers += power

print(total_powers)