#3-10 Every Funtion
language=['Cantonese','Arabic','English','Malay']
print(language)
print(f'this is the list in an alphebeticle sorted order:\n{sorted(language)}')
print(language)
print(f"I don't learn {language.pop(0)}")
print(language)
language.insert(2,'Spanish')
print(f'But I would love to learn {language[2]}!')
print(language)
print(f'but I dont learn {language[2]} and {language[0]}!')
del language[2]
del language[0]
print(language)
print('I really enjoy Japanese and Russian songs!')
language.append('Russian')
language.append('Japanese')
print(language)
language.copy()
print(language.sort(reverse=True))
print(language)
print('And there is the list in reverse Alphabetical order')



