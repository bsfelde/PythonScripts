Array.diff:
#remove all values in list B that are in list A

def array_diff(a, b):
    new = [value for value in a if value not in b]
    return new

-------------------------------------

Facebooks Likes
#list of names, return those names in string 
#following pattern based on amount of names in list

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) <= 1:
        #print names[0]
        return '%s likes this' %(names[0])
    elif len(names) <= 2:
        return '%s and %s like this' %(names[0], names[1])
    elif len(names) <= 3:
        return '%s, %s and %s like this' %(names[0], names[1], names[2])
    elif len(names) >= 4:
        subs = len(names)-2
        return '%s, %s and ' %(names[0], names[1]) + str(subs) + ' others like this'
    else:
        pass

-------------------------------------

PigLatin:
#takes first letter to end of word, plus 'ay'
#except special characters

def pig_it(text):
    pigly = []
    for word in text.split():
        if word[0] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
            pigly.append(word[1:] + word[0] + 'ay')
        elif word[0] not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
            pigly.append(word)
    return ' '.join(pigly)
	
def pig_it(text):
    pigly = [word[1:] + word[0] + 'ay' if word[0] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' else word for word in text.split()]
    return ' '.join(pigly)

-------------------------------------

Find the Vowels:
#returns the position of the vowel in a word

def vowel_indices(word):
    vowels = []
    for i, j in enumerate(word):
        if j.lower() in ('a','e','i','o','u','y'):
            vowels.append(i+1)
            #to make the first letter be index 1
    return vowels

def vowel_indices(word):
    return [i+1 for i,j in enumerate(word) if j.lower() in ('a','e','i','o','u','y')]

-------------------------------------

Mumbling:
#ex) 'abcd' --> 'A-Bb-Ccc-Dddd'

def accum(s):
    new = []
    for i,x in enumerate(s):
        new.append(x.upper()+ (x.lower()*i))
    return '-'.join(new)
    #join letters, separated by a dash

def accum(s):
    return '-'.join([x.upper() + (x.lower()*i) for i,x in enumerate(s)])

-------------------------------------

Decode the Morse:

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decodeMorse(morseCode):
    words = morseCode.replace('   ','  ')
    #separate the morst code into a list
    #turns spaces into blank value
    letters = words.split(' ')
    #splits words into letters
    new = []
    for x in letters:
        if x == '':
            new.append(' ')
        	#to maintain spaces between words
        else:
            new.append(MORSE_CODE[x])
            #function to convert morse code to letter
    return (''.join(new)).strip()
    #remove leading and ending spaces in values

def decodeMorse(morseCode):
    words = morseCode.replace('   ','  ')
    letters = words.split(' ')
    return (''.join([' ' if x == '' else MORSE_CODE[x] for x in letters])).strip()

-------------------------------------

CamelCase Method:
#ex) 'hello world' --> 'HelloWorld'

def camel_case(string):
    return ''.join([x[0].upper() + x[1:] for x in string.split()])

-------------------------------------

WeIrD StRiNg CaSe:
#ex) 'hello world' --> 'HeLlO WoRlD'

def to_weird_case(string):
    weird = []
    for x in string.split():
        letters = []
        for i,m in enumerate(x):
        #find the index per letter 
        #so I can manipulate based on every other letter
            if i % 2 == 0:
                letters.append(m.upper())
            else:
                letters.append(m.lower())
        weird.append(''.join(letters))
        #joins words into nested list
    return ' '.join(weird)
    #separates nested words by spaces

def to_weird_case(string):
    weird = []
    for x in string.split():
        letters = ''.join([m.upper() if i % 2 == 0 else m.lower() for i,m in enumerate(x)])
        weird.append(letters)
    return ' '.join(weird)