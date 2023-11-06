# A Program to parse text and do some calculations

# Scoring
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# Need total only for player

# A for Rock, B for Paper, and C for Scissors
# X means lose, Y means draw, and Z means you need to win

total = 0
player = ''

with open('input.txt', 'r') as file:
    # Each line is a round and line[0] = Opponent, line[2] = Whether to win
    for line in file:

        # Decide whether to win, lose or draw
        # Outer If Condition Calculates score based on if we draw or win
        # Lose
        if (line[2] == 'X'):
            # Nested If will Calculate score based on what the player plays
            # If Opponent plays Rock, Player will play Scissors to lose...
            if (line[0] == 'A'):
                total += 3
            elif (line[0] == 'B'):
                total += 1
            elif (line[0] == 'C'):
                total += 2
        # Draw
        elif (line[2] == 'Y'):
            total += 3
            if (line[0] == 'A'):
                total += 1
            elif (line[0] == 'B'):
                total += 2
            elif (line[0] == 'C'):
                total += 3
        # Win
        elif (line[2] == 'Z'):
            total += 6
            if (line[0] == 'A'):
                total += 2
            elif (line[0] == 'B'):
                total += 3
            elif (line[0] == 'C'):
                total += 1

print(total)
