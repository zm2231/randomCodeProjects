import random

def calculate_hand(hand):
    # Calculate the hand value
    hand_value = 0
    aces = 0
    for card in hand:
        if card[1] == 'Ace':
            aces += 1
            hand_value += 11
        elif card[1] in ['King', 'Queen', 'Jack']:
            hand_value += 10
        else:
            hand_value += int(card[1])
    # Adjust for Aces
    while hand_value > 21 and aces > 0:
        hand_value -= 10
        aces -= 1
    return hand_value

# Create a deck of cards
deck = [
    ('Spades', 'Ace'), ('Spades', '2'), ('Spades', '3'), ('Spades', '4'),
    ('Spades', '5'), ('Spades', '6'), ('Spades', '7'), ('Spades', '8'),
    ('Spades', '9'), ('Spades', '10'), ('Spades', 'Jack'), ('Spades', 'Queen'),
    ('Spades', 'King'),
    ('Hearts', 'Ace'), ('Hearts', '2'), ('Hearts', '3'), ('Hearts', '4'),
    ('Hearts', '5'), ('Hearts', '6'), ('Hearts', '7'), ('Hearts', '8'),
    ('Hearts', '9'), ('Hearts', '10'), ('Hearts', 'Jack'), ('Hearts', 'Queen'),
    ('Hearts', 'King'),
    ('Clubs', 'Ace'), ('Clubs', '2'), ('Clubs', '3'), ('Clubs', '4'),
    ('Clubs', '5'), ('Clubs', '6'), ('Clubs', '7'), ('Clubs', '8'),
    ('Clubs', '9'), ('Clubs', '10'), ('Clubs', 'Jack'), ('Clubs', 'Queen'),
    ('Clubs', 'King'),
    ('Diamonds', 'Ace'), ('Diamonds', '2'), ('Diamonds', '3'), ('Diamonds', '4'),
    ('Diamonds', '5'), ('Diamonds', '6'), ('Diamonds', '7'), ('Diamonds', '8'),
    ('Diamonds', '9'), ('Diamonds', '10'), ('Diamonds', 'Jack'),
    ('Diamonds', 'Queen'), ('Diamonds', 'King')
]

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

player_value = calculate_hand(player_hand)
dealer_value = calculate_hand(dealer_hand)

# Allow the player to hit or stand
while True:
    print(f'Your hand: {player_hand} ({player_value})')
    print(f'Dealer\'s hand: {dealer_hand[0]}')
    action = input('Would you like to hit or stand? ')
    if action == 'stand':
        break
    elif action == 'hit':
        # Deal another card to the player
        player_hand.append(deck.pop())
        player_value = calculate_hand(player_hand)
        if player_value > 21:
            print('You bust!')
            break

# Implement the dealer's turn
while True:
    print(f'Dealer\'s hand: {dealer_hand} ({dealer_value})')
    if dealer_value < 17:
        # Dealer hits
        dealer_hand.append(deck.pop())
        dealer_value = calculate_hand(dealer_hand)
        if dealer_value > 21:
            print('Dealer busts!')
            break
    else:
        # Dealer stands
        break

# Determine the winner
if player_value > 21:
    print('Dealer wins!')
elif dealer_value > 21:
    print('You win!')
elif player_value > dealer_value:
    print('You win!')
elif dealer_value > player_value:
    print('Dealer wins!')
else:
    print('It\'s a tie!')
