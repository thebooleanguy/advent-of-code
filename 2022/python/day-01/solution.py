# Program to Read File and do some Calculations using Arrays, then Sort them

lines = []
# Open file for reading
with open('input.txt', 'r') as file:
    # For loop to save lines into a list
    for line in file:
        lines.append(line)

# Else cant access 0th element because no element
totals = [0]
# For loop to add the totals to another list, seperating by newline
newline_count = 0
for line in lines:
    if line == '\n':
        newline_count += 1
        # Else no element to access and do the addition
        totals.append(0)
        continue
    totals[newline_count] += int(line)

max = [0, 0, 0]
# Repeat 3 times to get top 3 maxes
for i in range(3):
    # For loop to get max
    for total in totals:
        if total > max[i]:
            max[i] = total
    # Remove max from totals list
    totals.remove(max[i])

print(max[0] + max[1] + max[2])
