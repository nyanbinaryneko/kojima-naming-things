import random

def generate_name():
    nouns = open_file("./corpus/nouns.txt")
    adjectives = open_file("./corpus/adjectives.txt")
    names = open_file("./corpus/names.txt")
    animals = open_file("./corpus/animals.txt")
    names += adjectives + animals
    if random.randint(0, 5) < 2:
        name = metal_gear_solid_name_generator(animals, adjectives)
    else:
        name = f"{random.choice(names).capitalize()} {random.choice(nouns).capitalize()} {random.choice(nouns).capitalize()}man"
    return name

def generate_tweet():
    friends = open_file("./corpus/friends.txt")
    animals = open_file("./corpus/animals.txt")
    name = generate_name()
    sentences = [f"Thinking my next game will have {name} as the main character.", 
    f"hmmm, is {name} a good name? I'm thinking it fits the character and my vision", 
    f"Ah, yes, {name}. They will be played by {random.choice(friends)}.",
    f"{name} will be an {random.choice(animals)} furry played by {random.choice(friends)}.",
    f"Konami wouldn't let me have a character named {name}. They will be in my next game, I promise."]

    return random.choice(sentences)

def open_file(file):
    with open(file) as f:
        lyst = f.readlines()
    lyst = [item.strip() for item in lyst]
    return lyst

def metal_gear_solid_name_generator(animals, adjectives):
    print("making an mgs name")
    return f"{random.choice(adjectives).capitalize()} {random.choice(adjectives).capitalize()}"