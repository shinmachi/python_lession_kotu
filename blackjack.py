import random

RANK, SUIT = 0, 1

def player_op(deck, player_hand, op):
    doubled, ending = False, False
    if op == '1':
        print('[ プレイヤー : スタンド ]')
        doubled, ending = False, True
    elif op == '2':
        print('[ プレイヤー : ヒット ]')
        player_hand.append(deck.pop())
        print_player_hand(player_hand)
        doubled, ending = False, False
    elif op == '3':
        if len(player_hand) == 2:
            print('[ プレイヤー : ダブル ]')
            player_hand.append(deck.pop())
            print_player_hand(player_hand)
            doubled, ending = True, True
        else:
            print('( ダブルはできません。)')

    if get_point(player_hand) > 21:
        print('[ プレイヤーはバストした！]')
        ending = True
    elif get_point(player_hand) == 21:
        print( '21です！')
        ending = True

    return doubled, ending

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
        result += 10 # A = 11, add 10 to the result
    return result

# print_player_hand function
def print_player_hand(player_hand):
    print('プレイヤー (', get_point(player_hand), '):   ')
    for card in player_hand:
        print('[', card[SUIT], card[RANK], ']')
    print()

# print_dealer_hand function
def print_dealer_hand(dealer_hand, uncovered):
    if uncovered:
        print('ディーラー (', get_point(dealer_hand), '):   ')
    else:
        print('ディーラー ( ?? ):   ')
    flag = True
    for card in dealer_hand:
        if  flag or uncovered:
            print('[' , card[SUIT], card[RANK], ']')
            flag = False
        else:
            print('[ * * ]')
    print()


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
        bet = 10
        player_money -= bet

        # print(deck)
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

        #print(player_hand)
        print_player_hand(player_hand)

        #print(dealer_hand)
        print_dealer_hand(dealer_hand, False)

        # プレイヤーターン
        while True:
            op = input('スタンド : 1,  ヒット : 2,  ダブル : 3  > ')
            doubled, ending = player_op(deck, player_hand, op)
            if doubled: # doubled processing
                player_money -= bet
                bet += bet
            if ending: # turn end
                break

        turn += 1
        input('次のターンへ')
    print('ゲームオーバー')

if __name__ == '__main__':
    main()