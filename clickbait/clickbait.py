"""MODIFIED Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
A clickbait headline generator for your soulless content farm website.
The original code is available at https://nostarch.com/big-book-small-python-programming"""

import random


def main():
    print()
    print("Clickbait Headline Generator")
    print("+---------------------------+")
    print("Our website needs to trick people into looking at ads!\n")

    # TODO: Call each function and print each headline that is returned.
    
    #TODO: Print a deadline in the middle print statement
    print()
    print()
    print()


# Each of these functions returns a different type of headline:


def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)

    return f"Are Millenials Killing the {noun} Industry?"


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)

    return f"Without This {noun}, {pluralNoun} Could Kill You {when}!"


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)

    return f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}"


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)

    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + "s"
    pluralNoun2 = random.choice(NOUNS) + "s"
    return f"What {pluralNoun1} Don't Want You To Know About {pluralNoun2}"


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + "s"
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return f"{number1} Reasons Why {pluralNoun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == "Their":
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong."

def generateDeadline():
    website = random.choice(SITES)
    when = random.choice(WHEN).upper()

    return "Post this to our {} {} or you're fired!".format(website, when)


# Set up the constants:
OBJECT_PRONOUNS = ["Her", "Him", "Them"]
POSSESIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
STATES = [
    "California",
    "Texas",
    "Florida",
    "New York",
    "Pennsylvania",
    "Illinois",
    "Ohio",
    "Georgia",
    "North Carolina",
    "Michigan",
]
NOUNS = [
    "Athlete",
    "Clown",
    "Shovel",
    "Paleo Diet",
    "Doctor",
    "Parent",
    "Cat",
    "Dog",
    "Chicken",
    "Robot",
    "Video Game",
    "Avocado",
    "Plastic Straw",
    "Serial Killer",
    "Telephone Psychic",
]
PLACES = [
    "House",
    "Attic",
    "Bank Deposit Box",
    "School",
    "Basement",
    "Workplace",
    "Donut Shop",
    "Apocalypse Bunker",
]
WHEN = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]
SITES = ["wobsite", "blag", "Facebuuk", "Googles", "Facesbook", "Tweedie", "Pastagram"]

# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
