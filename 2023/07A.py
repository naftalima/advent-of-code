strength_hand_types_dsc = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']
strength_hand_types = strength_hand_types_dsc[::-1]

plays_by_type = {}
for type in strength_hand_types: plays_by_type[type] = []

strength_cards_dsc = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
strength_cards = strength_cards_dsc[::-1]

def get_hand_type(hand: str) -> str:
    unique_count = {}
    for card in hand:
        if card in unique_count:
           unique_count[card] += 1 
        else:
            unique_count[card] = 1
    if len(unique_count) == 1:
        return('Five of a kind')
    elif len(unique_count) == 5:
        return('High card')
    elif len(unique_count) == 4:
        return('One pair')
    elif len(unique_count) == 3:
        cards_qtd = list(unique_count.values())
        if 3 in cards_qtd:
            return('Three of a kind')
        else:
            return('Two pair')
    elif len(unique_count) == 2:
        cards_qtd = list(unique_count.values())
        if 4 in cards_qtd:
            return('Four of a kind')
        else:
            return('Full house')


def solve_draw(hands: list) -> list:
    plays = []
    points = []
    for hand, bid in hands:
        cards = list(hand)
        cards_point = [strength_cards_dsc.index(card) for card in cards]        
        plays.append((hand,bid))
        points.append(cards_point)

    combined = list(zip(points, plays))
    sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
    plays_sorted = [play for _, play in sorted_combined]
    return (plays_sorted)



def get_ranked(plays_bt : dict) -> list:
    rank = []
    for hand_type in strength_hand_types:
        plays = plays_bt[hand_type]
        amount_hands = len(plays)
        if amount_hands > 1 :
            cards_sorted = solve_draw(plays)
            # import pdb; pdb.set_trace()
            for card in cards_sorted:
                rank.append(card)
        elif amount_hands == 1:
            play =  plays[0]
            rank.append(play)

    
    return rank


def get_total_winnings(ranked: list) -> int:
    # adding up the result of multiplying each hand's bid with its rank
    total_winnings = 0
    for rank, hand_info in enumerate(ranked):
        hand, bid = hand_info
        rank = rank+1
        winning = bid*rank 
        print('#', hand, ':', rank, '*', bid, '=', winning)
        total_winnings += winning
        print('total_winnings = ', total_winnings, '\n')
    return(total_winnings)

with open("puzzle-input/camel-cards.txt") as file:
    for line in file:
        hand, bid = line.split()
        bid = int(bid)
        play_info = (hand, bid)

        hand_type = get_hand_type(hand)
        plays_by_type[hand_type].append(play_info)

print(plays_by_type)
plays_ranked = get_ranked(plays_by_type)
print(plays_ranked)
total = get_total_winnings(plays_ranked)
print(total)
