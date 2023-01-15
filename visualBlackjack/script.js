// Create a deck of cards
let deck = [];
let suits = ['hearts', 'diamonds', 'spades', 'clubs'];
let values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'];

for (let suit in suits) {
  for (let value in values) {
    deck.push(values[value] + ' of ' + suits[suit]);
  }
}

// Shuffle the deck
function shuffle(deck) {
  for (let i = 0; i < deck.length; i++) {
    let randomIndex = Math.floor(Math.random() * deck.length);
    let temp = deck[i];
    deck[i] = deck[randomIndex];
    deck[randomIndex] = temp;
  }
  return deck;
}

deck = shuffle(deck);

// Deal two cards to the player and two cards to the dealer
let playerCards = [deck.pop(), deck.pop()];
let dealerCards = [deck.pop(), deck.pop()];

console.log('Player cards: ' + playerCards.join(', '));
console.log('Dealer cards: ' + dealerCards.join(', '));
