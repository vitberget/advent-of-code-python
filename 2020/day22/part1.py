from functools import reduce

with open("puzzle22.txt") as file:
    file_content = file.read()

player1txt, player2txt = file_content.split('\n\n')

player1 = list(map(int, player1txt.splitlines()[1::]))
player2 = list(map(int, player2txt.splitlines()[1::]))

while len(player1) > 0 and len(player2) > 0:
    card1 = player1[0]
    card2 = player2[0]

    player1 = player1[1:]
    player2 = player2[1:]

    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

endresult = player1 + player2
indexes = range(len(endresult), 0, -1)


def multiply(n1, n2):
    return n1 * n2


def plus(n1, n2):
    return n1 + n2


multiplied = list(map(multiply, endresult, indexes))
result = reduce(plus, multiplied)

# print(endresult)
# print(indexes)
# print(multiplied)
print(result)
