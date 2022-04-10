"""
Determine the shift to decode a given Caesar Cipher, then
provides the decoded message.

@author: MDP
"""

from collections import Counter
from operator import indexOf

letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalLetters = 26

# Replace with your cipher text!
message = "Lzak ak s lwkl ewkksyw A zsnw ojallwf xgj eq hjgyjse"

with open("1000-most-common-words.txt") as words:
    wordlist = []
    for word in words:
        wordlist.append(word.strip())

def decode_message(shift):
    keys = {}

    # Lowercase
    for index, letter in enumerate(letters):
        keys.update({letters[index]:letters[(index - shift) % totalLetters]})
    # Uppercase
    for index, letter in enumerate(upper_letters):
        keys.update({upper_letters[index]:upper_letters[(index - shift) % totalLetters]})

    decryptedMessage = []
    for letter in message:
        if letter == ' ': # Just appending spaces unshifted
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(keys[letter]) 
    return ''.join(decryptedMessage)

shift = -1
max_counter = 0
best_shift = -1

while shift < 26:
    shift += 1
    counter = 0
    result = decode_message(shift).lower()
    for word in wordlist:
        if word in result:
            counter += 1
        else:
            continue
    if counter > max_counter:
        max_counter = counter
        best_shift = shift

print("Shift:", best_shift)
print("Decrypted Message:", decode_message(best_shift))