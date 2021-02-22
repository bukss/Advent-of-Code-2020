from aoc_utils import load_input

deck1, deck2 = load_input("\n\n")
deck1 = list(map(int, deck1.splitlines()[1:]))
deck2 = list(map(int, deck2.splitlines()[1:]))

p1_score, p2_score = 0, 0
while deck1 and deck2:
    p1, p2 = deck1.pop(0), deck2.pop(0)
    if p1 > p2:
        deck1.append(p1)
        deck1.append(p2)
    else:
        deck2.append(p2)
        deck2.append(p1)


score1 = sum([(i+1)*c for i,c in enumerate(reversed(deck1))])
score2 = sum([(i+1)*c for i,c in enumerate(reversed(deck2))])
print(max(score1, score2))