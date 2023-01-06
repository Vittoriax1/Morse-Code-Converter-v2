import winsound

def play_morse(text):
    duration = 0.25
    # Initialize an empty list to store the beeps
    beeps = []
    
    # Iterate over each character in the text
    for char in text:
        if char == '.':
            frequency = 1000
        elif char == '-':
            frequency = 2000
        #elif char == ' ':
            #frequency = 0
        else:
            frequency = 0
            duration = 0.25
        
        # Clamp the frequency to the valid range (37-32767 Hz)
        frequency = max(37, min(frequency, 32767))
        
        # Add the beep to the list
        beeps.append((frequency, int(duration * 1000)))
    
    # Play the entire sequence of beeps
    for beep in beeps:
        winsound.Beep(*beep)
            
def text_to_morse(text):

    # Defining the doctionary
    morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' ',  # space character
    '.': '.-.-.-',  # full stop
    ',': '--..--',  # comma
    ':': '---...',  # colon
    '?': '..--..',  # question mark
    '!': '-.-.--',  # exclamation mark
    '\'': '.----.',  # apostrophe
    '-': '-....-',  # hyphen
    '/': '-..-.',  # slash
    '(': '-.--.',  # left parenthesis
    ')': '-.--.-',  # right parenthesis
    '"': '.-..-.',  # quotation mark
    '@': '.--.-.',  # at sign
    }

    # Initialize an empty string to store the morse code translation
    morse_text = ""

    # Split the input text into words
    words = text.split()
    
    # Iterate over each word
    for word in words:
        # Iterate over each character in the word
        for char in word:
            # Convert the character to uppercase
            char = char.upper()
            # Check if the character is a letter or a number
            if char in morse_code:
                # If it is, look up the corresponding Morse code translation in the dictionary and add it to the output string
                morse_text += morse_code[char]
            else:
                # If the character is not a letter or a number, add it as is to the output string
                morse_text += char
        # Add a space between each word
        morse_text += " "
    
    # Return the resulting Morse code translation
    return morse_text

# Banner
intro = '|          Text to Morse Letter Translator        |'
text_len = len(intro)
print('{}'.format('-' * text_len))
print(intro)
print('{}'.format('-' * text_len))
print()

# Input looping
user_input = input('Please enter a sentence to be translated: ')
morse_out = text_to_morse(user_input)
print('Your code for {} is {}'.format(user_input,morse_out))

# Play the Morse code as a series of beeps
play_morse(morse_out)

# Exit message
print('Thanks for translating with us!')
