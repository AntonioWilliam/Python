#Pratic Example Manipulating Text

phrase = 'Any way means De qualquer forma'
print(phrase)

print('What is the fiveth letter ?')
print(phrase[5])

print('Separate the word (Any) ?')
print(phrase[:3])

print('Separate the word (forma) ?')
print(phrase[26:])

print('How many letters are in the phrase ?')
print(len(phrase))

print('How many letters (a) appear in the phrase ?')
print(phrase.lower().count('a'))

print('Change (de qualquer forma) per (enfim) ) ')
print(phrase.lower().replace('de qualquer forma','enfim'))

print('Exist the word (Do) in the phrase ?')
print('Do' in phrase)

print('Exist the word (way) in the phrase ?')
print('way' in phrase)

print('Separate the words ')
print(phrase.split())

print('Show the item [2] of the List')
List= phrase.split()
print(List[2])
