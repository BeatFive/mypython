#4-13 Buffet
foods= ('cheese','chips','cookies','nuggets','chocolate')
print('Original food list:')
for food in foods:
    print(food)

print('\nModified food list')
foods=('cheese','chips','cookies','fruits','mints')
for food in foods:
    print(food)
# Will occur an error because tuples cannot be changed but we can rewrite the tuple.
foods[0]= ('oreos')

