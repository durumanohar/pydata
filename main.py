import json
data = json.load(open("data.json"))

def retrive_definition(word):
    if word in data:
        return data[word]
    else:
        return("word not found in dictionary")

word_user = input("Enter a word: ")

print(retrive_definition(word_user))