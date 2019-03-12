import json
data = json.load(open("app1/data.json"))
# type(data)

word = input("Enter a word here : ")

# print(translate[word])


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word is not in our dictionary"


print(translate(word))
