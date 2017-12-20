# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

def clean_message(message):
    """(str) -> str
    
    Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to 
    uppercase.
    
    >>> clean_message('CSc108i s5%^Great')
    'CSCISGREAT'
    >>> clean_message('.,*4Tko')
    'TKO'
    """
    alpha_message = ''
    
    for ch in message:
        if ch.isalpha():
            alpha_message += ch
    #Goes through each character in the message and puts letters in the
    #list.
    
    return alpha_message.upper()

def encrypt_letter(uppercase_letter, keystream_value):
    """"(str, int) -> str
    Precondition: All characters must be uppercase.
    
    Return the encrypted character by applying the keystream value
    (keystream_value)to the character(uppercase_letter).
    
    >>> encrypt_letter('A', 8)
    'I'
    >>> encrypt_letter('K', 1)
    'L'
    """
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    
    for ch in alphabet:
        if uppercase_letter == ch:
            return alphabet[(alphabet.index(ch) + keystream_value) % 26]
    #Takes the index of each character and adds a value to it, making it
    #refer to a different character.

def decrypt_letter(uppercase_letter, keystream_value):
    """"(str, int) -> str
    Precondition: All characters must be uppercase.
    
    Return the decrypted character by applying the keystream value
    (keystream_value) to the character(uppercase_letter).
        
    >>> decrypt_letter('I', 8)
    'A'
    >>> decrypt_letter('L', 1)
    'K'
    """
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

    for ch in alphabet:
        if uppercase_letter == ch:
            return alphabet[(alphabet.index(ch) - keystream_value) % 26] 
    #Takes the index of each character and subtracts a value to it, making 
    #it refer to a different character.    

def swap_cards(deck, index):
    """(list of int, int) -> NoneType
    
    Swap the card at the index with the card that follows it in the deck. 
    The deck is circular: if the card at the index is on the bottom 
    of the deck, that card swaps with the top card.
    
    >>> deck = [1, 2, 3, 4, 5]
    >>> swap_cards(deck, 2)
    >>> deck
    [1, 2, 4, 3, 5]
    
    >>> deck = [1, 2, 3, 4, 5]
    >>> swap_cards(deck, 4)
    >>> deck
    [5, 3, 2, 4, 1]
    """
    if index == (len(deck) - 1):
        deck[index], deck[0] = deck[0], deck[index]
    else:
        deck[index], deck[index + 1] = deck[index + 1], deck[index]

def move_joker_1(deck):
    """(list of int) -> NoneType
    Precondition: JOKER1 must be in deck.
    
    Find JOKER1 in the deck and swap it with the card that follows it. 
    The deck as circular.
    
    >>> deck = [1, 2, 27, 3, 4, 5]
    >>> move_joker_1(deck)
    >>> deck
    [1, 2, 3, 27, 4, 5]
    
    >>> deck = [1, 2, 3, 4, 5, 27]
    >>> move_joker_1(deck)
    >>> deck 
    [27, 2, 3, 4, 5, 1]
    """
    swap_cards(deck, deck.index(JOKER1))

def move_joker_2(deck):
    """(list of int) -> NoneType
    Precondition: JOKER2 must be in deck.
    
    Find JOKER2 in the deck and move it two cards down. Treat the deck as 
    circular.
    
    >>> deck = [1, 28, 2, 27, 3, 4, 5]
    >>> move_joker_2(deck)
    >>> deck
    [1, 2, 27, 28, 3, 4, 5]
    
    >>> deck = [1, 2, 27, 3, 4, 5, 28]
    >>> move_joker_2(deck)
    >>> deck
    [2, 28, 27, 3, 4, 5, 1]
    """
    swap_cards(deck, deck.index(JOKER2))
    swap_cards(deck, deck.index(JOKER2))
    #Function is repeated twice to move the card down twice.

def triple_cut(deck):
    """(list of int) -> NoneType
    Precondition: JOKER1 and JOKER2 must be in deck.
    
    Find the two jokers in the deck. Then move everything above the first 
    joker to the bottom of the deck and everything below the second joker 
    to the top of the deck.
    
    >>> deck = [1, 28, 2, 27, 3, 4, 5]
    >>> triple_cut(deck)
    >>> deck
    [3, 4, 5, 28, 2, 27, 1]
    """
    if deck.index(JOKER2) < deck.index(JOKER1):
        above_joker = deck[0 : deck.index(JOKER2)]
        below_joker = deck[deck.index(JOKER1) + 1 : ]
    else:
        above_joker = deck[0 : deck.index(JOKER1)]
        below_joker = deck[deck.index(JOKER2) +1 : ]
    #Find the card values that are above and below JOKER1 and JOKER2.
    
    for num in above_joker:
        deck.remove(num) 
    deck.extend(above_joker)
    #Remove the card values above the first joker and place them at the
    #bottom.
    
    below_joker.reverse()
    for num in below_joker:
        deck.remove(num)
        deck.insert(0, num)
    #Remove the card values below the second joker and place them at the
    #top

def insert_top_to_bottom(deck):
    """(list of int) -> NoneType
    Precondition: JOKER1 and JOKER2 must be in deck. 
    
    Look at the bottom card of the deck; move that many cards from the 
    top of the deck to the bottom, inserting them just above the bottom 
    card. Special case: if the bottom card is JOKER2, use JOKER1 as the 
    number of cards.
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 
    27, 2, 5, 8, 11, 14, 17, 20, 26]
    
    >>> deck = [27, 4, 7, 10, 13, 16, 19, 22, 25, 6, 1, 3, 9, 12, 15, 18, 
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [27, 4, 7, 10, 13, 16, 19, 22, 25, 6, 1, 3, 9, 12, 15, 18, 21, 24, 27, 
    2, 5, 8, 11, 14, 17, 20, 23, 28]
    """
    if deck[-1] != JOKER2:
        cards_to_move = deck[0 : deck[-1]]
    else:
        cards_to_move = deck[0 : (JOKER1)]
    #Determines if the bottom card is the special case and creates the card
    #values to be moved.
    
    for cards in cards_to_move:
        deck.remove(cards)
        deck.insert(-1, cards)
    #Removes the card values to be moved and places them before the last 
    #index.

def get_card_at_top_index(deck):
    """(list of int) -> int
    Precondition: JOKER1 and JOKER2 must be in deck. 
    
    Return the card at the index of the value of the topcard in the deck. 
    Special case: if the top card is JOKER2, use JOKER1 as the index.

    >>> get_card_at_top_index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    4
    
    >>> get_card_at_top_index([28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6,
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    26
    """
    if deck[0] == JOKER2:
        index_value = deck[JOKER1]
    else:
        index_value = deck[deck[0]]
                       
    return index_value

def get_next_value(deck):
    """(list of int) -> int
    
    Return the next potential keystream value from the values in deck.
    
    >>> get_next_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    """
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    potential_keystream_value = get_card_at_top_index(deck)
    #Calls on previous functions to shuffle the deck and generate a value.
    
    return potential_keystream_value

def get_next_keystream_value(deck):
    """(list of int) -> int
    
    Return a valid keystream value (a number in the range 1-26) from the
    values in deck.
    
    >>> get_next_keystream_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    
    >>> get_next_keystream_value([22, 2, 20, 1, 17, 15, 26, 18, 6, 4, 7,
    10, 13, 16, 19, 14, 23, 25, 5, 8, 11, 24, 27, 3, 28, 12, 21, 9])
    8
    """
    keystream_value = get_next_value(deck)
    
    while keystream_value == JOKER1 or keystream_value == JOKER2:
        keystream_value = get_next_value(deck)
    #Generates a new value if the value is JOKER1 or JOKER2
    
    return keystream_value

def process_message(deck, message, MODE):
    """(list of int, str, str) -> str
    
    Return the encrypted or decrypted message in message depending if MODE
    is 'e' or 'd' from the values in deck.
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck, 'ANXJO!', 'd')
    'PEACE'
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck, 'do a barrel roll!', 'e')
    'OXXIKQCPSZXWW'
    """
    finished_message = ''
        
    for uppercase_letter in clean_message(message):
        keystream_value = get_next_keystream_value(deck)
        if MODE == 'e':
            finished_message += encrypt_letter(uppercase_letter, keystream_value)
        elif MODE == 'd':
            finished_message += decrypt_letter(uppercase_letter, keystream_value)
    #Goes through every character of the message and encrypts or decrypts it.    
    
    return finished_message 

def process_messages(deck, message_list, MODE):
    """(list of int, list of str, str) -> list of str
    
    Return the list of encrypted or decrypted messages from message_list
    depending if MODE is 'e' or 'd' from the values in deck.
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message_list = ['TJJCOMRPUKN', 'TLMRMNHZYQJ', 'BXVYYNYTM']
    >>> process_messages(deck, message_list, 'd')
    ['IAMVENGENCE', 'IAMTHENIGHT', 'IAMBATMAN']
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message_list = ['To the batmobile!', 'da-na-na-na-nana']
    >>> process_messages(deck, message_list, 'e')
    ['EXQOOALETWKTWE', 'BFWUESWQGXWX']
    """
    full_message = []
    
    for message in message_list:
        processing = process_message(deck, message, MODE)
        full_message.append(processing)
    #Goes through every message in the list and encrypts or decrypts the 
    #message, then puts them in a list.
        
    return full_message
    
def read_messages(message_file):
    """(file open for reading) -> list of str
    
    Return and read the contents of the file, message_file, as a list 
    of messages. 
    """
    message_list = []
    message_line = message_file.readlines()
    
    for line in message_line:
        message_list.append(line.strip())  
    
    message_file.close()
    #Reads the lines in the file and puts them in a list of strings.Then, 
    #closes the file.
    
    return message_list

def read_deck(deck_file):
    """(file open for reading) -> list of int
    
    Return and read the contents of the file, deck_file, as a list of 
    integers.
    """
    deck_temp = []
    deck = []
    line = deck_file.readline()   
    
    while line:
        deck_temp.append(line.split())
        line = deck_file.readline() 
    
    deck_file.close()
    #Reads the lines in the file and puts them in a list as a list of
    #lists. Then, closes the file. 
    
    for line in deck_temp:
        deck += line
    #Creates a list of stings from the list of lists.
    
    for i in range(len(deck)):
        deck[i] = int(deck[i]) 
    #Converts the list of strings to a list of integers.
    
    return deck