import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    for p in plaintext:
        num = ord(p)
        if num >= ord('A') and num <= (ord('Z') - shift):
            num += shift
        elif num > (ord('Z') - shift) and num <= ord('Z'):
            num = num - 26 + shift
        elif num >= ord('a') and num <= (ord('z') - shift):
            num += shift
        elif num > (ord('z') - shift) and num <= ord('z'):
            num = num - 26 + shift
        ciphertext += chr(num)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for c in ciphertext:
        num = ord(c)
        if num >= (ord('A') + shift) and num <= ord('Z'):
            num -= shift
        elif num >= ord('A') and num < (ord('A') + shift):
            num = num + 26 - shift
        elif num >= (ord('a') + shift) and num <= ord('z'):
            num -= shift
        elif num >= ord('a') and num < (ord('a') + shift):
            num = num + 26 - shift
        plaintext += chr(num)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
