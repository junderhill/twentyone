from random import shuffle, random
import random


class ShuffledDeck:
    def __init__(self):
        suits = ["hearts", "diamonds", "spades", "clubs"]
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        self.cards = []
        for s in suits:
            for c in cards:
                self.cards.append(c)

        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class TwentyOneGame:
    def __init__(self):
        self.deck = ShuffledDeck()
        self.current_hand = []

        # deal two cards
        for i in range(0, 2):
            self.current_hand.append(self.deck.deal_card())

    # gets closest score to 21
    def current_value_of_hand(self):
        non_ace_value = 0
        number_of_aces = 0
        for card in self.current_hand:
            if isinstance(card, int):
                non_ace_value += card
            elif card != "A":
                non_ace_value += 10
            else:
                number_of_aces += 1

        if number_of_aces == 0:
            return non_ace_value
        else:
            scores = [(non_ace_value + number_of_aces), (non_ace_value + 10 + number_of_aces)]
            scores.sort(reverse=True)

            if scores[0] <= 21:
                return scores[0]
            else:
                return scores[1]

    def hit_me(self):
        self.current_hand.append(self.deck.deal_card())

    def is_game_over(self):
        return self.current_value_of_hand() > 21

    def current_score(self):
        if self.is_game_over():
            return 0
        else:
            return self.current_value_of_hand()
