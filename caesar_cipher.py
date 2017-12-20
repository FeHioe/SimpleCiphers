def encrypt_letter(letter):
    """ (str, int) -> str

    Precondition: letter is uppercase.

    Encrypt letter by shifting 3 places to the right.

    >>> encrypt_letter('V')
    'Y'
    """

    # Translate to a number in the range 0-25.  'A' translates to 0, 'B' to 1,
    # and so on.
    ord_diff = ord(letter) - ord('A')

    # Apply the right shift; we use % to handle the end of the alphabet.
    # The result is still in the range 0-25.
    new_char_ord = (ord_diff + 3) % 26

    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def decrypt_letter(letter):
    """ (str, int) -> str

    Precondition: letter is uppercase.

    Decrypt letter by shifting 3 places to the left.

    >>> decrypt_letter('Y')
    'V'
    """

    # Translate to a number.
    ord_diff = ord(letter) - ord('A')

    # Apply the left shift.
    new_char_ord = (ord_diff - 3) % 26

    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def create_caesar_cipher(message):
    """ (str) -> str

    Encrypt message using the Caesar cipher with a right shift of 3.

    >>> create_caesar_cipher('NEED MORE SLEEP!  ZZZ...')
    'QHHG PRUH VOHHS!  CCC...'
    >>> create_caesar_cipher('I SOLEMNLY SWEAR THAT I AM UP TO NO GOOD.')
    'L VROHPQOB VZHDU WKDW L DP XS WR QR JRRG.'
    """

    cipher = ''

    for letter in message:
        if letter.isupper():
            cipher = cipher + encrypt_letter(letter)
        else:
            cipher = cipher + letter

    return cipher


def decode_caesar_cipher(message):
    """ (str) -> str

    Decrypt message using the Caesar cipher with a left shift of 3.

    >>> decode_caesar_cipher('QHHG PRUH VOHHS!  CCC...')
    'NEED MORE SLEEP!  ZZZ...'
    """

    cipher = ''

    for letter in message:
        if letter.isupper():
            cipher = cipher + decrypt_letter(letter)
        else:
            cipher = cipher + letter

    return cipher
