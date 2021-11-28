from typing import List
from collections import Counter

def likes(names: List[str]) -> str:
    if not names:
        print('nobody likes it')
    elif len(names) == 1:
        print(f"{names[0]} like it!")
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]} like it")
    elif len(names) == 3:
        print(f"{names[0]}, {names[1]} and {names[2]} like it")
    elif len(names) == 4:
        print(f"{names[0]}, {names[1]} and {len(names)-2} other people like it")

likes([]) # => "nobody likes it"
likes(["Peter"]) # => "Peter like it!"
likes(["Peter", "Anna"]) # => "Peter and Anna like it"
likes(["Peter", "Anna", "Mark"]) # => "Peter, Anna i Mark like it"
likes(["Peter", "Anna", "Mark", "Ola"]) # => "Peter, Anna i 2 other people like it"


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    return [x for x in lst_of_words if Counter(x) == Counter(word)]

assert anagrams('listen', ['silent', 'cat', 'litens']) == ['silent', 'litens']
print(anagrams('silent', ['listen', 'cat']))

def create_phone_number(n: List[int]) -> str:
    str1 = ''.join(str(x) for x in n[0:2])
    str2 = ''.join(str(x) for x in n[2:5])
    str3 = ''.join(str(x) for x in n[5:8])
    str4 = ''.join(str(x) for x in n[8:11])

    return f"(+{str1}) {str2}-{str3}-{str4}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])) #(+12) 345-678-901

def to_weird_case(string: str) -> str:
    newString = []
    for i in range(len(string)):
        if i % 2 == 0:
            newString.append(string[i].capitalize())
        else:
            newString.append((string[i].lower()))
    print(''.join(newString))

to_weird_case('String')
to_weird_case('Algorithms and data structures')

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str) -> str:
    words = []
    for morse_word in morse_code.split('   '):
        word = ''.join([MORSE_CODE.get(morse_char) for morse_char in morse_word.strip(' ').split(' ')])
        words.append(word)
    print(' '.join(words))


decode_morse ('.... . -.--   .--- ..- -.. .') # => 'HEY JUDE'
decode_morse(' . ') # => 'E'
decode_morse('...   ---   ...') # => 'S O S'