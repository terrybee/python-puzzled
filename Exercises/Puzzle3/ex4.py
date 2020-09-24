import random
import itertools

#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']

# left, right, up, down
magician_cards_pos = []
first_card_index = []
hidden_card_index = []
         
#Given 5 cards, Assistant hides an appropriate card
#He/she reads out the remaining four cards after choosing their order carefully!
def AssistantOrdersCards():

    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)

    #Initialization
    cards, cind = [], []

    #Various data structures are filled in
    cards = random.sample(deck, 4)
    for card in cards:
        n = deck.index(card)
        cind.append(n)

    print(cards, cind)

    #Find two cards out of the 4 that have the shortest distance. Guaranteed to exist.
    sortedCardIndices = sorted(cind)
    sortedCardIndices.append(sortedCardIndices[0] + len(deck))
    shortestCardDistance = 13
    firstCardIndex = sortedCardIndices[0]
    for i in range(1, len(sortedCardIndices)):
        secondCardIndex = sortedCardIndices[i]
        cardDistance = secondCardIndex - firstCardIndex
        if cardDistance < shortestCardDistance:
            shortestCardDistance = cardDistance
            if secondCardIndex > 52:
                secondCardIndex = secondCardIndex - 52
            shortestCardPair = [firstCardIndex, secondCardIndex]
        firstCardIndex = secondCardIndex

    # extract remained card
    remainedCards = []
    for card in cind:
        if card not in shortestCardPair:
            remainedCards.append(card)

    first_card_index.append(shortestCardPair[0])
    hidden_card_index.append(shortestCardPair[1])

    #Given the number that needs to be encoded, order the cards appropriately
    encodingCard(remainedCards, shortestCardDistance)

    return

def encodingCard(remainedCards, shortestCardDistance):
    up_down = False
    for e in format(shortestCardDistance, '04b'):
        if e == '0':
            if up_down:
                magician_cards_pos.append('u')
            else:
                magician_cards_pos.append('r')
        else:
            if up_down:
                magician_cards_pos.append('d')
            else:
                magician_cards_pos.append('l')
        up_down = not up_down

    return

#This procedure takes four cards encoded properly and determines the hidden card.
def MagicianGuessesCard():
    binary_distance = ''
    for pos_of_card in magician_cards_pos:
        if pos_of_card == 'u' or pos_of_card == 'r':
            binary_distance = binary_distance + '0'
        else:
            binary_distance = binary_distance + '1'
 
    card_distance = int(binary_distance, 2)

    hidden_index = first_card_index[0] + card_distance
    if hidden_index > 52:
        hidden_index = hidden_index - 52

    print ('Hidden card is:', deck[hidden_index])
    answer_card = deck[hidden_card_index[0]]
    if deck[hidden_index] == answer_card:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed! Hidden card is', answer_card)



AssistantOrdersCards()
MagicianGuessesCard()