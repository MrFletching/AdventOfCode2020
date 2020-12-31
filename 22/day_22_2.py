#!/usr/bin/env python3

def main():
    player_1, player_2 = read_decks('input.txt')
    
    winner = play_game(player_1, player_2, 1)

    winning_score = calculate_score(player_1 + player_2)

    print(f'Winning Score: {winning_score}')

def play_game(player_1, player_2, game):
    player_1_previous_decks = []
    player_2_previous_decks = []

    game_round = 1

    while player_1 and player_2:
        print()
        print(f'-- Round {game_round} (Game {game}) --')
        player_1_str = ', '.join([str(c) for c in player_1])
        player_2_str = ', '.join([str(c) for c in player_2])
        print(f'Player 1\'s deck: {player_1_str}')
        print(f'Player 2\'s deck: {player_2_str}')

        if already_played(player_1, player_1_previous_decks):
            return 1
        if already_played(player_2, player_2_previous_decks):
            return 1

        player_1_previous_decks.append(player_1.copy())
        player_2_previous_decks.append(player_2.copy())

        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        print(f'Player 1 plays: {card_1}')
        print(f'Player 2 plays: {card_2}')

        if card_1 <= len(player_1) and card_2 <= len(player_2):
            winner = play_game(player_1.copy()[:card_1], player_2.copy()[:card_2], game + 1)
        else:
            if card_1 > card_2:
                winner = 1
            else:
                winner = 2

        print(f'Player 1 wins round {game_round} of game {game}!')
        
        if winner == 1:
            player_1 += [card_1, card_2]
        else:
            player_2 += [card_2, card_1]
        
        game_round += 1
    
    if player_1:
        return 1
    else:
        return 2


def already_played(current_deck, previous_decks):
    for deck in previous_decks:
        if deck == current_deck:
            return True
    return False


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
