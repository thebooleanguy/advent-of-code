# A Program to parse text and do some calculations

# Scoring
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# Need total only for player

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

total = 0

with open('test.txt', 'r') as file:
    # Each line is a round and line[0] = Opponent, line[2] = Player
    for line in file:

        # Outer If Condition = Logic for score based on what the player chooses
        # Not necessarily a win
        # Nested If Condition decides the score for winnings and draws
        if (line[2] == 'X'):
            total += 1
            # Win
            if (line[0] == 'C'):
                total += 6
            # Draw
            if (line[0] == 'A'):
                total += 3
        if (line[2] == 'Y'):
            total += 2
            if (line[0] == 'A'):
                total += 6
            if (line[0] == 'B'):
                total += 3
        if (line[2] == 'Z'):
            total += 3
            if (line[0] == 'B'):
                total += 6
            if (line[0] == 'C'):
                total += 3

print(total)
