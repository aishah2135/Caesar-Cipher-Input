# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:27:18 2024

@author: aisha
"""

import string #imports string library and allows you to work with strings on a more complex level
print("What the message you would like to encrypt?")
encrypted_message = input()

def caesar_encrypt(message, key):
    
    shift = key % 26 # key is thee number to shift down the alphabet to encrypt 
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    encrypted_message = message.lower().translate(cipher) #encrypts the message will recognize upper and lowercase letters
    
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    message = encrypted_message.translate(cipher) #translation method decrypts the message
    return message

message = encrypted_message #message to encrypt
key = 5 #how many letters to shift down the alphabet to encrypt

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')