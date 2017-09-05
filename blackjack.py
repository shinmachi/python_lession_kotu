import random

RANK, SUIT = 0, 1
def get_point(hand):
    result = 0
    ace_flag = False
    for card in hand:
        if card[RANK] == 1:
            ace_flag = True
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result = result + num
    if ace_flag and result <= 11:
        result += 10
    return result

def make_deck():
    suits = ['S','H','D','C']
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck

def main():
    turn = 1
    player_money = 100
    while(player_money > 0):
        print('ターン：', turn)
        print('所持金：', player_money)

        player_hand = [] # list of player hand
        dealer_hand = [] # list of dealer hand
        deck = make_deck() # make dack
        # print(deck)
        for i in range(2:
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())


        print(player_hand)
        print(get_point(player_hand))

        print(dealer_hand)
        print(get_point(dealer_hand))


        turn += 1
        input('次のターンへ')
    print('ゲームオーバー')

if __name__ == '__main__':
    main()