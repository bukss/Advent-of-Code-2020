from aoc_utils import load_input

player1, player2 = load_input("\n\n")
player1 = list(map(int, player1.splitlines()[1:]))
player2 = list(map(int, player2.splitlines()[1:]))

def crab_combat(deck1, deck2):
    prev_decks = set()
    while deck1 and deck2:
        decks = (tuple(deck1), tuple(deck2))
        if decks in prev_decks:
            return 1, 0
        else:
            prev_decks.add(decks)

        c1, c2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= c1 and len(deck2) >= c2:
            winner = crab_combat(deck1[:c1], deck2[:c2])[0]
        else:
            winner = {c1: 1, c2: 2}[max(c1, c2)]
        
        if winner == 1:
            deck1.extend([c1, c2])
        elif winner == 2:
            deck2.extend([c2, c1])
    
    score1 = sum([(i+1)*c for i,c in enumerate(reversed(deck1))])
    score2 = sum([(i+1)*c for i,c in enumerate(reversed(deck2))])

    if score1 > score2:
        return 1, score1
    else:
        return 2, score2
        
print(crab_combat(player1, player2))