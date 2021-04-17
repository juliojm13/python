from random import randint


def get_jokes(number):
    global nouns
    global adjectives
    global adverbs
    for i in range(number):
        print(nouns[randint(0, len(nouns)-1)], adverbs[randint(0, len(adverbs)-1)], adjectives[randint(0, len(adjectives)-1)])
        print("jaja")


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(3)

