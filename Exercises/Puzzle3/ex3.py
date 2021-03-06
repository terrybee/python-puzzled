import random
import itertools

#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '10_C', 'J_C', 'Q_C', 'K_C',
        'A_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'J_D', 'Q_D', 'K_D',
        'A_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H', 'J_H', 'Q_H', 'K_H',
        'A_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'J_S', 'Q_S', 'K_S']

magician_cards = []
hidden_card = []

# Given 5 cards, Assistant hides an appropriate card
# He/she reads out the remaining four cards after choosing their order carefully!
def AssistantOrdersCards():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck)

    # Initialization
    cards, cind, cardsuits, cnumbers = [], [], [], []

    # Various data structures are filled in
    cards = random.sample(deck, 5)
    # cards = ['J_S', '4_C', 'A_C', '10_D', '10_C']
    print('cards: ', cards)

    for card in cards:
        n = deck.index(card)
        cind.append(n)
        cardsuits.append(n // 13)
        cnumbers.append(n % 13)

    # print(cards, cind, cardsuits, cnumbers)

    # Create cnumber list by same suit list of list
    cnumbers_by_suits = [[] for i in range(4)]
    for i in range(5):
        index = cardsuits[i]
        value = cnumbers[i]
        cnumbers_by_suits[index].append(value)

    # Check distance each elements in samesuits
    pairsuit = None
    min_distance = 13
    pairnumber = None
    for i in range(4):
        cnumbers_in_same_suits = cnumbers_by_suits[i]
        if (len(cnumbers_in_same_suits) < 2):
            continue
        cnumbers_in_same_suits.sort()
        cnumbers_in_same_suits.append(cnumbers_in_same_suits[0] + 13)

        # Get minimum distance of pairs
        left = 0
        for right in range(1, len(cnumbers_in_same_suits)):
            if cnumbers_in_same_suits[right] - cnumbers_in_same_suits[left] < min_distance:
                pairsuit = i
                min_distance = cnumbers_in_same_suits[right] - cnumbers_in_same_suits[left]
                if cnumbers_in_same_suits[right] >= 13:
                    cnumbers_in_same_suits[right] = cnumbers_in_same_suits[right] - 13
                pairnumber = [cnumbers_in_same_suits[left], cnumbers_in_same_suits[right]]
            left = right

    # Find two cards out of the 5 that have the same suit. Guaranteed to exist.
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit and cnumbers[i] in pairnumber:
            cardh.append(i)

    # Figure out which card needs to be hidden and what number to encode
    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remTuples = []
    for i in range(5):
        if i != hidden and i != other:
            remTuples.append((cnumbers[i], cind[i]))

    # Order the three cards in ascending order
    remindices = sortList(remTuples)

    # Given the number that needs to be encoded, order the cards appropriately
    outputNext3Cards(encode, remindices)

    return


# This procedure figures out which card should be hidden based on the distance
# between the two cards that have the same suit.
# It returns the hidden card, the first exposed card, and the distance
def outputFirstCard(numbers, oneTwo, cards):
    encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
    if 0 < encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13

    ##    #The following print statement is just for debugging!
    ##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)
    print('First card is:', cards[other])

    # set hidden & magician cards
    hidden_card.append(cards[hidden])
    magician_cards.append(cards[other])

    return hidden, other, encode


# This procedure orders three cards depending on the number "code" that
# needs to be encoded.
def outputNext3Cards(code, ind):
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print('Second card is:', deck[second])
    print('Third card is:', deck[third])
    print('Fourth card is:', deck[fourth])

    # set magician cards
    magician_cards.append(deck[second])
    magician_cards.append(deck[third])
    magician_cards.append(deck[fourth])


# Sorts elements in tlist in ascending order.
def sortList(tlist):
    # sort and get only index of card
    return [a_tuple[1] for a_tuple in sorted(tlist)]


# This procedure takes four cards encoded properly and determines the hidden card.
def MagicianGuessesCard():
    # print ('Cards are character strings as shown below.')
    # print ('Ordering is:', deck)
    cards, cnums = [], []
    for card in magician_cards:
        cards.append(card)
        n = deck.index(card)
        cnums.append((n % 13) + 0.1 * (n // 13))
        if len(cards) == 1:
            suit = n // 13
            number = n % 13

    # Use the ordering of the last 3 cards to determine distance from 1st card
    if cnums[1] < cnums[2] and cnums[1] < cnums[3]:
        if cnums[2] < cnums[3]:
            encode = 1
        else:
            encode = 2
    elif ((cnums[1] < cnums[2] and cnums[1] > cnums[3])
          or (cnums[1] > cnums[2] and cnums[1] < cnums[3])):
        if cnums[2] < cnums[3]:
            encode = 3
        else:
            encode = 4
    elif cnums[1] > cnums[2] and cnums[1] > cnums[3]:
        if cnums[2] < cnums[3]:
            encode = 5
        else:
            encode = 6

    # Knowing the number and the suit gives the card index and then string
    hiddennumber = (number + encode) % 13
    index = hiddennumber + suit * 13

    print('Hidden card is:', deck[index])
    answer_card = hidden_card[0]
    if deck[index] == answer_card:
        print('You are a Mind Reader Extraordinaire!')
    else:
        print('Sorry, not impressed! Hidden card is', answer_card)


AssistantOrdersCards()
MagicianGuessesCard()
