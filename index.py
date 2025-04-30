def is_vertical(line):
    ((x1, y1), (x2, y2)) = line
    (pair_1, pair_2) = line
    (x1, y1) = pair_1
    (x2, y2) = pair_2
    if x1 == x2 and y1 != y2:
        return True
    else:
        return False

def is_horizontal(line):
    ((x1, y1), (x2, y2)) = line
    (pair_1, pair_2) = line
    (x1, y1) = pair_1
    (x2, y2) = pair_2
    if y1 == y2 and x1 != x2:
        return True
    else:
        return False

def is_degenerated(line):
    ((x1, y1), (x2, y2)) = line
    (pair_1, pair_2) = line
    (x1, y1) = pair_1
    (x2, y2) = pair_2
    if pair_1 == pair_2:
        return True
    else:
        return False

def is_inclined(line):
    ((x1, y1), (x2, y2)) = line
    (pair_1, pair_2) = line
    (x1, y1) = pair_1
    (x2, y2) = pair_2
    if is_vertical(line) == False and is_horizontal(line) == False and is_degenerated(line) == False:
        return True
    else:
        return False

# Проверка

line = (15, 5), (15, -5)
pair_1 = (15, 5)
pair_2 = (15, -5)

print(is_vertical(line))
print(is_horizontal(line))
print(is_degenerated(line))
print(is_inclined(line))
