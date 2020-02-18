def MorseEncode(sentence):

  CODE = {'A': '.-',  'B': '-...','C': '-.-.', 'D': '-..', 'E': '.','F': '..-.','G': '--.', 'H': '....','I': '..', 'J': '.---','K': '-.-', 'L': '.-..', 'M': '--',  'N': '-.',  'O': '---', 'P': '.--.','Q': '--.-','R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-','W': '.--', 'X': '-..-', 'Y': '-.--','Z': '--..', '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',  '4': '....-',  '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', '9': '----.'  }

  encoded_sentence = ''
  for letter in sentence:
    if letter != ' ':
      letter = CODE[letter]
    encoded_sentence += letter

  return encoded_sentence


# test your function
original = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

encoded = MorseEncode(original)

print(f'the sentence "{original} encoded in Morse becomes "{encoded}"')
