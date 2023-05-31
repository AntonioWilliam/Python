

phrase = str(input('Enter a phrase : ')).strip().lower()

print('Quantas vezes aparece a letra "A" ? ', phrase.count('a'))
print('Em que posição ela aparece a primeira vez ? ', phrase.find('a')+1)
print('Em que posição ela aparece na ultima vez ?', phrase.rfind('a')+1)
