import random

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
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())


        print(player_hand)
        print(dealer_hand)


        turn += 1
        input('次のターンへ')
    print('ゲームオーバー')

if __name__ == '__main__':
    main()