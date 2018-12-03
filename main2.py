import json
data = json.load(open("data.json"))

def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data    :
        return data[word.upper()]
    else:
        return("word not found in dictionary")

word_user = input("Enter a word: ")

print(retrive_definition(word_user))