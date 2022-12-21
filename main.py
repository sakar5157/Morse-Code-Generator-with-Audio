import sys
import winsound

# Morse code dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

# Function to play the Morse code sound
def play_morse(code, dot_duration=100, dash_duration=300):
    for char in code:
        if char == '.':
            winsound.Beep(800, dot_duration)
        elif char == '-':
            winsound.Beep(800, dash_duration)
        else:
            winsound.Beep(800, dot_duration*7)

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase
sentence = sentence.upper()

# Initialize the Morse code string
morse_code = ""

# Convert each character of the sentence to Morse code
for char in sentence:
    if char == " ":
        morse_code += "  "
    else:
        morse_code += MORSE_CODE_DICT[char] + " "

# Print the Morse code
print("Morse code:", morse_code)

# Play the Morse code sound
play_morse(morse_code)
