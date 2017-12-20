"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

#Change these values to the files in the root folder to encypt or decryt.
DECK_FILENAME = 'deck2.txt'
MSG_FILENAME = 'secret1.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    deck_file = open(DECK_FILENAME, 'r')
    message_file = open(MSG_FILENAME, 'r')
    
    deck = cipher_functions.read_deck(deck_file)
    message_list = cipher_functions.read_messages(message_file)
    cipher_message = cipher_functions.process_messages(deck, message_list, MODE)
    
    for line in cipher_message:
        print(line)

    pass

main()
 