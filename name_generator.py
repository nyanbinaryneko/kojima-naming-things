import random

def generate_name():
    with open("./corpus/nouns.txt") as f:
        nouns = f.readlines()
    nouns = [noun.strip() for noun in nouns]

    with open("./corpus/adjectives.txt") as f:
        adjectives = f.readlines()
    adjectives = [adjective.strip() for adjective in adjectives]

    return f"{random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()} {random.choice(nouns).capitalize()}man"   