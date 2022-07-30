punctuation = "?!.,' "
alphabet = 'abcdefghijklmnopqrstuvwxyz'
random_text = "VVQGY TVVVK ALURW FHQAC MMVLE HUCAT WFHHI PLXHV UWSCI GINCM"
import collections
import re

def ceasar_decoder(message, shift):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            translated_message += alphabet[(letter_index + 10) % len(alphabet)]
        else:
            translated_message += letter
    return translated_message

def ceasar_encoder(message, shift):
    message = message.lower()
    encoded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            encoded_message += alphabet[(letter_index - 10) % len(alphabet)]
        else:
            encoded_message += letter
    return encoded_message

def ceasar_brute_force(coded_message):
    translated_message = ""
    shift = 1
    while shift < 27:
        for letter in coded_message:
            if not letter in punctuation:
                letter_index = alphabet.find(letter)
                translated_message += alphabet[(letter_index + shift) % len(alphabet)]
            else:
                translated_message += letter
        print(translated_message + "\n")
        shift += 1
        translated_message = ""
aaa
def decode_vigenere_ciper(coded_message, keyword):
    translated_message = ""
    #used as index for filling the coded_message
    i = 0
    #counts up in order to get the index of the coded string
    j = 0
    #fills up the code string to latch the length of the message
    while len(coded_message) > len(keyword):
        keyword += keyword[i]
        i += 1

    for letter in coded_message:
        if not letter in punctuation:
            #saves the index of the letter in the lower case alphabet
            letter_index = alphabet.find(letter)
            #saves the index of the code letter in the lower case alphabet
            keyword_index = alphabet.find(keyword[j])
            translated_message += alphabet[(letter_index - keyword_index) % len(alphabet)]
        else:
            translated_message += letter
        j += 1
    return translated_message

def encode_vigenere_ciper(coded_message, keyword):
    coded_message = coded_message.lower()
    translated_message = ""
    #used as index for filling the coded_message
    i = 0
    #counts up in order to get the index of the coded string
    j = 0
    #fills up the code string to latch the length of the message
    while len(coded_message) > len(keyword):
        keyword += keyword[i]
        i += 1
    for letter in coded_message:
        if not letter in punctuation:
            #saves the index of the letter in the lower case alphabet
            letter_index = alphabet.find(letter)
            #saves the index of the code letter in the lower case alphabet
            keyword_index = alphabet.find(keyword[j])
            translated_message += alphabet[(letter_index + keyword_index) % len(alphabet)]
        else:
            translated_message += letter
        j += 1
    return translated_message


def calc_index_of_coincidence(text):
    text = text.lower()
    N = len(text) #length of the Textinput
    frequency = collections.Counter(text) #frequency of letters in text
    frequency_sum = 0.0
    for letter in alphabet:
            frequency_sum += frequency[letter] * (frequency[letter] - 1)
    IC = frequency_sum / (N*(N-1))
    return IC



def decode_vigenere_cipher_no_keyword(text):
    translated_message = ""
    text = re.sub(r'[^a-zA-Z]+', '', text)
    text = text.lower()
    shift = 1
    new_list = []
    while shift < 27:
        for letter in text:
            if not letter in punctuation:
                letter_index = alphabet.find(letter)
                translated_message += alphabet[(letter_index + shift) % len(alphabet)]
            else:
                translated_message += letter
        shift += 1
        print(translated_message)
        new_list.append(calc_index_of_coincidence(translated_message))
        translated_message = ""
    return new_list

print(decode_vigenere_cipher_no_keyword(random_text))
