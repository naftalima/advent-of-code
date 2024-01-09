def is_hand_valid(hand: list):
    r,g,b = hand
    if r > 12 : return False
    if g > 13: return False
    if b > 14: return False
    return True

valid_games = 0
with open("puzzle-input/cards.txt") as file:
    for line in file:
        game, sets = line.split(':')
        game_number = int(game.split()[1])

        sets = sets.split(';')
        sets = [s.strip() for s in sets]

        valid_play = True

        for plays in sets:
            plays = plays.split(',')

            hand = [0,0,0] # [R,G,B]
            for play in plays:
                qty, color = play.strip().split(' ')
                qty = int(qty)
                if 'red' in color: hand[0] = qty
                elif 'green' in color: hand[1] = qty
                elif 'blue' in color: hand[2] = qty
            
            if not is_hand_valid(hand):
                valid_play=False
        if valid_play:
            valid_games += game_number

print(valid_games)
            
                