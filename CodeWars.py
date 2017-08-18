Array.diff:

Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Solution:
def array_diff(a, b):
    new = [value for value in a if value not in b]
    return new

-------------------------------------

Facebooks Likes

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

def vowel_indices(word):
    vowels = []
    for i, j in enumerate(word):
        if j.lower() in ('a','e','i','o','u','y'):
            vowels.append(i+1)
    return vowels

def vowel_indices(word):
    return [i+1 for i,j in enumerate(word) if j.lower() in ('a','e','i','o','u','y')]

-------------------------------------

Mumbling:

def accum(s):
    new = []
    for i,x in enumerate(s):
        new.append(x.upper()+ (x.lower()*i))
    return '-'.join(new)

def accum(s):
    return '-'.join([x.upper() + (x.lower()*i) for i,x in enumerate(s)])

-------------------------------------

Decode the Morse:

def decodeMorse(morseCode):
    words = morseCode.replace('   ','  ')
    letters = words.split(' ')
    new = []
    for x in letters:
        if x == '':
            new.append(' ')
        else:
            new.append(MORSE_CODE[x])
    return (''.join(new)).strip()

def decodeMorse(morseCode):
    words = morseCode.replace('   ','  ')
    letters = words.split(' ')
    return (''.join([' ' if x == '' else MORSE_CODE[x] for x in letters])).strip()

-------------------------------------

CamelCase Method:

def camel_case(string):
    return ''.join([x[0].upper() + x[1:] for x in string.split()])

-------------------------------------

WeIrD StRiNg CaSe:

def to_weird_case(string):
    weird = []
    for x in string.split():
        letters = []
        for i,m in enumerate(x):
            if i % 2 == 0:
                letters.append(m.upper())
            else:
                letters.append(m.lower())
        weird.append(''.join(letters))
    return ' '.join(weird)

def to_weird_case(string):
    weird = []
    for x in string.split():
        letters = ''.join([m.upper() if i % 2 == 0 else m.lower() for i,m in enumerate(x)])
        weird.append(letters)
    return ' '.join(weird)