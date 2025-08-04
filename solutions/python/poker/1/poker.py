RANKS = ["A", "K", "Q", "J"] + [str(n) for n in reversed(range(2, 11))]
RANKS_EX = RANKS + ["A"] 
SUITS = ["S", "C", "H", "D"]

class HandStats:
    def __init__(self, hand):
        self.hand = hand
        self.num_s_S = 0
        self.num_s_C = 0
        self.num_s_H = 0
        self.num_s_D = 0
        self.num_r_A = 0
        self.num_r_K = 0
        self.num_r_Q = 0
        self.num_r_J = 0
        self.num_r_10 = 0
        self.num_r_9 = 0
        self.num_r_8 = 0
        self.num_r_7 = 0
        self.num_r_6 = 0
        self.num_r_5 = 0
        self.num_r_4 = 0
        self.num_r_3 = 0
        self.num_r_2 = 0

        for card in hand.split(" "):
            rank = card[0] if len(card) == 2 else card[:2]
            suit = card[1] if len(card) == 2 else card[2:]

            setattr(self, f'num_s_{suit}', getattr(self, f'num_s_{suit}') + 1) 
            setattr(self, f'num_r_{rank}', getattr(self, f'num_r_{rank}') + 1) 

    def is_better(self, other):
        self_hand = self.evaluate()
        other_hand = other.evaluate()

        if self_hand[0] < other_hand[0]:
            return 1
        if self_hand[0] > other_hand[0]:
            return -1
        if self_hand[0] == other_hand[0]:
            for index, value in enumerate(other_hand[1]):
                if self_hand[1][index] < value:
                    return 1
                if self_hand[1][index] > value:
                    return -1   

        return 0

    def evaluate(self):
        has_straight = False
        max_straight = None
        has_same_suit = False
        quad = None
        triplet = None
        pairs = []
        free_cards = []

        for rank_id in range(0,10):
            checks = 0
            for offset in range(5):
                if getattr(self, f'num_r_{RANKS_EX[rank_id+offset]}') > 0:
                    checks += 1
            if checks == 5:
                has_straight = True
                max_straight = rank_id

        for rank_id in range(0, 13):
            if getattr(self, f'num_r_{RANKS[rank_id]}') == 4:
                quad = rank_id
            if getattr(self, f'num_r_{RANKS[rank_id]}') == 3:
                triplet = rank_id
            if getattr(self, f'num_r_{RANKS[rank_id]}') == 2:
                pairs.append(rank_id)
            if getattr(self, f'num_r_{RANKS[rank_id]}') == 1:
                free_cards.append(rank_id)

        for suit in SUITS:
            if getattr(self, f'num_s_{suit}') == 5:
                has_same_suit = True

        if has_straight and has_same_suit:
            return [0, [max_straight]]
        if quad is not None:
            return [1, [quad] + free_cards]
        if triplet is not None and len(pairs) > 0:
            return [2, [triplet, pairs[0]]]
        if has_same_suit:
            return [3, [free_cards]]
        if has_straight:
            return [4, [max_straight]]
        if triplet is not None:
            return [5, [triplet, free_cards[0], free_cards[1]]]
        if len(pairs) == 2:
            return [6, pairs+free_cards]
        if len(pairs) == 1:
            return [7, pairs+free_cards]
        return [8, free_cards]


def best_hands(hands):
    hand_stats = []

    for hand in hands:
        hand_stats.append(HandStats(hand))

    result = [hand_stats[0]]

    for hand in hand_stats[1:]:
        check = hand.is_better(result[0])

        if check == 1:
            result = [hand]
        if check == 0:
            result.append(hand)

    return [x.hand for x in result]