#!/usr/bin/env python3

def main():
    player_1, player_2 = read_decks('input.txt')
    
    while player_1 and player_2:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 > card_2:
            player_1 += [card_1, card_2]
        else:
            player_2 += [card_2, card_1]
    
    winning_player = player_1 + player_2

    winning_score = calculate_score(winning_player)
    print(f'Winning Score: {winning_score}')


def calculate_score(cards):
    score = 0
    for index, card in enumerate(cards):
        score += card * (len(cards) - index)
    
    return score


def read_decks(filename):
    with open(filename) as f:
        data = f.read()
    
    data_split = data.split('\n\n')

    decks = [[],[]]

    for player in range(2):
        raw_cards = data_split[player].rstrip().split('\n')[1:]
        decks[player] = [int(card) for card in raw_cards]

    return decks


if __name__ == '__main__':
    main()
