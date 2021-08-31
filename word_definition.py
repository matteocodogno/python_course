import json
from difflib import get_close_matches


def get_definitions(word):
    with open('./resources/data.json', 'r') as file:
        data = json.load(file)

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        similar_word = get_close_matches(word, data.keys(), 1, 0.8)
        if len(similar_word) > 0:
            answer = input(f'Did you mean {similar_word[0]} [Y = yes, N = no]? ').upper()
            if answer == 'Y':
                return get_definitions(similar_word[0])

    return [f'The word "{word}" does not exist. Please double check it.']


user_input = input("Enter a word: ").lower()
definitions = get_definitions(user_input)
for definition in definitions:
    print(definition)
