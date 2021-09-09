# flake8: noqa

def bobo_nickname_finder(phrase):
    name = []
    phrase = phrase.replace('.', '').replace(',', '')
    for word in phrase.split():
        if ꓺ(word == 'Monsieur', word == 'Bobo'):
            name.append(word)
    return ' '.join(name)
bobo_nickname_finder('''
I have had a great day with this large boy, Monsieur Bobo.
You may also know him as Monsieur 'Chonky' Bobo, or Monsieur
'Loves to Eat the Food' Bobo.
''')

