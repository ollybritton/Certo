#coding=utf-8
import random
from import_path import import_path

import_path("types.py")

# ---
# r.py
# Stores all the functions related to generating random content.
# ---


def number(a, b):
    return random.randint(a, b)

def choice(arr):
    return random.choice(arr)

def damage(level):
    return (5*level)/2 + number(0, 3)

def hero():
    names = ["Achilles", "Alec", "Ajax", "Alexander", "Atlas", "Blaine", "Beowulf", "Bolivar", "Balthasor", "Frederic",
             "Gable", "Gage", "Gabe", "Graydon", "Godric", "Hades", "Hercules", "Hunter", "Ives", "Julius", "Kade", "Kaelan",
             "Khronos", "Luther", "Maximus", "Maxamillion", "Osias", "Perseus", "Saxon", "Tiberius"]

    adjective = ["Bold", "Courageous", "Daring", "Epic", "Fearless", "Gallant", "Grand", "Gusty", "Noble", "Valiant", "Elevated",
                 "Dauntless", "Lion-Hearted", "Unafraid", "Valorous"]

    curr = random.choice(names) + " The " + random.choice(adjective)
    return curr


def villian():
    names = ["Kade", "Kaelan", "Khronos", "Luther", "Maximus", "Maxamillion", "Osias", "Perseus", "Saxon", "Tiberius", "Ash",
             "Bates", "Beast", "Bones", "Bram", "Casper", "Chucky", "Crow", "Damien", "Dexter", "Draco", "Edgar", "Freddy", "Gomez",
             "Hannibal", "Jack", "Lucifer", "Norman", "Poe", "Pugsley", "Rasputin", "Romero", "Salem", "Spike", "Storm", "Thorn", "Vlad"]

    adjective = ["Bad", "Corrupt", "Destructive", "Hateful", "Heinous", "Hideous", "Malevolent", "Malicious", "Nefarious",
                 "Ugly", "Unpleasant", "Vicious", "Villainous", "Wiked", "Foul", "Beastly", "Baneful", "Calamitous", "Harmful",
                 "Wrathful"]


    curr = random.choice(names) + " The " + random.choice(adjective)
    return curr


def NPC():
    names = ["Chloe", "Emily", "Aaliyah", "Emma", "Olivia", "Jennifer", "Hannah", "Kellie", "Jessica", "Lauren", "Sarah", "Lily",
             "Ava", "Mia", "Jasmine", "Isabella", "Sophia", "Grace", "Ella", "Rebecca", "Charlotte", "Abigail", "Amy", "Aaron",
             "Jacob", "Shawn", "Michael", "Daniel", "Alex", "Ryan", "James", "David", "Mattew", "Jack", "Muhammad", "Alexander",
             "Jordan", "Kevin", "Dylan", "Christopher", "Chris", "Blake", "Joshua", "Adam", "Robert", "Joseph", "William", "George"]

    noun = ["Accountant", "Taxer", "Farmer", "Blacksmith", "Alchemist", "Librarian", "Brickmaker", "Lawyer", "Apprecntice", "Priest",
            "Dentist", "Doctor", "Barber", "Merchant", "Nurse", "Musician", "Pharmacists", "Pirate", "Guard", "Servant", "Stonemason",
            "Traveler", "Brewer", "Butcher", "Carpenter"]


    curr = random.choice(names) + " The " + random.choice(noun)
    return curr


def place():
    # (Implementation of https://www.dandwiki.com/wiki/Well_Over_100_Tavern_Names_(DnD_Other)#Totally_Random)

    nouns = "ant;arrow;beaver;beetle;boat;boot;bow;bull;butterfly;calf;castle;cat;chameleon;chipmunk;clam;cow;crow;dagger;dog;dragon;dragonfly;drunk;duck;eagle;ewe;falcon;falls;fish;flagon;flask;fly;foal;forest;fox;frog;goat;goose;gopher;gryphon;gull;hat;hawk;helm;horse;kitten;knight;lady;lion;lizard;lord;louse;manatee;mare;marten;mink;mountain;mouse;octopus;otter;owl;ox;oyster;pint;rat;raven;river;roc;seal;shark;sheep;shield;ship;shot;skeleton;slug;snail;snake;sow;squid;squirrel;stallion;starfish;sword;termite;tiger;toad;tower;trophy;unicorn;vampire;wand;wasp;wench;whale;witch;wolf;worm;wyvern"

    adjectives = "angry;arcane;black;bloody;blue;bright;brown;buried;burning;cheap;crying;cyan;daring;dark;defiled;desperate;discreet;divine;drab;drowning;drunken;easy;enchanted;false;fat;flatulent;flying;foolish;forgotten;fun;giant;gold;gray;green;happy;haunted;heroic;hidden;hiding;hovering;humorous;hungry;hypnotic;illegal;jumping;laughing;lonely;lost;lucky;magical;maroon;married;naked;navy;ochre;orange;peach;petrified;pink;pious;pompous;poor;profane;puce;purple;red;roaring;rolling;running;sacred;sad;sanguine;screaming;sepia;shiny;silent;silver;singing;skinny;sleeping;sleepy;slimy;smelly;sober;special;spoilt;stubborn;suffering;swimming;talking;thieving;tiny;undead;unfortunate;violet;wealthy;white;wooden;yawning;yellow"

    titles = "Ale House;Bar;Beer House;Brew House;Brewery;Club House;Den;Inn;Lodge;Loft;Lounge;Mead House;Pub;Speakeasy;Tavern"

    nouns = nouns.split(";")
    adjectives = adjectives.split(";")
    titles = titles.split(";")

    decider = number(1, 10)

    if decider == 1:
        # Adjective Noun
        return capital_case(choice(adjectives)) + " " + capital_case(choice(nouns))

    elif decider == 2:
        # Adjective Noun Title
        return capital_case(choice(adjectives)) + " " + capital_case(choice(nouns)) + " " + capital_case(choice(titles))

    elif decider == 3:
        # The Adjective Noun
        return "The " + capital_case(choice(adjectives)) + " " + capital_case(choice(nouns))

    elif decider == 4:
        # The Adjective Noun Title
        return "The " + capital_case(choice(adjectives)) + " " + capital_case(choice(nouns)) + " " + capital_case(choice(titles))

    elif decider == 5:
        # Noun & Noun
        return capital_case(choice(nouns)) + " & " + capital_case(choice(nouns))

    elif decider == 6:
        # Noun & Noun Title
        return capital_case(choice(nouns)) + " & " + capital_case(choice(nouns)) + " " + capital_case(choice(titles))

    elif decider == 7:
        # The Noun & Noun
        return "The " + capital_case(choice(nouns)) + " & " + capital_case(choice(nouns))

    elif decider == 8:
        # The Noun & Noun Title
        return "The " + capital_case(choice(nouns)) + " & " + capital_case(choice(nouns)) + " " + capital_case(choice(titles))

    elif decider == 9:
        # Adjective Title
        return capital_case(choice(adjectives)) + " " + capital_case(choice(titles))

    elif decider == 10:
        # The Adjective Title
        return "The " + capital_case(choice(adjectives)) + " " + capital_case(choice(titles))

def weapon(level):
    weapons = ["Gauntlets", "Sword", "Knife", "Dagger", "Pickaxe", "Axe", "Shortsword", "Mace", "Spear", "Longbow", "Bow", "Crossbow"]
    adjectives = []

    if level == 1:
        adjectives = ["Rusty", "Wooden", "Broken", "Busted", "Collapsed", "Cracked", "Crushed", "Mutilated", "Ruptured", "Shattered", "Smashed"]


    elif level == 2:
        adjectives = ["Brittle", "Stone", "Weak", "Amateur", "Dusty", "Cracked", "Damaged", "Fractured", "Beat-Up", "Used", "Discarded"]


    elif level == 3:
        adjectives = ["Bronze", "Maluable", "Scratched", "Bent", "Repaired", "Passable", "Meh", "Okay", "Acceptable", "Wonky", "Fixed"]


    elif level == 4:
        adjectives = ["Firm", "Clean", "Sturdy", "Iron", "Refurbished", "Mended", "Suitable", "Sharpened", "Pointy", "Decent", "Effective"]


    elif level == 5:
        adjectives = ["Cruel", "Deadly", "New", "Steel", "Accurate", "Edged", "Sharp", "Fresh", "Alright", "Robust", "Good"]


    elif level == 6:
        adjectives = ["Robust", "Mighty", "Strapping", "Fibrous", "Sturdy", "Cutting", "Edged", "Strong", "Perfect", "Brilliant", "Woah"]


    elif level == 7:
        adjectives = ["Intense", "Dazzling", "Perfect", "Shining", "Glistining", "Elegant", "Classy", "Posh", "Titanium", "Diamond", "\'Oh My God\'"]


    elif level == 8:
        adjectives = ["Impecale", "Charming", "Elegant", "Super", "Superb", "Dank", "Precise", "\'Oh God Oh God Oh God\'", "Titanium", "Diamond", "Sublime"]


    elif level == 9:
        adjectives = ["Sublime", "Celestial", "Ghostly", "Incredible", "Bleeding", "Alive", "Heavenly", "Other-Worldly", "Awesome", "Merciful", "\'Oh God Oh God Oh God\'"]


    elif level == 10:
        global Weapon
        # Formats:
        # The <Adjective> <Weapon> Of <Noun>
        # <Adjective> <Weapon>
        # The <Adjective> <Weapon>
        # <Weapon> Of The <Adjective> <Noun>
        # The <Weapon> Of The <Adjective> <Noun>

        nouns = ["Moon", "Sun", "Dawn", "Sunset", "Life", "Death", "Sky", "Star", "Heaven", "Clouds", "Thunder", "Lightning", "Fire", "Water", "Earth", "Wind", "Mars", "Mercury", "Neptune", "Jupiter", "Saturn"]
        adjectives = ["Celestial", "Etheral", "Eternal", "Angelic", "Divine", "Immortal", "Otherworldy", "Spiritual", "Supernatrual", "Blessed", "Holy", "Elysian", "Supernal", "Transcendental", "Transmundane", "Seraphic", "Empyral", "Almighty", "Genius", "Godly", "Exquisite", "Ghostly", "Unworldly", "Unsubstantial", "Tenous"]
        name = ""

        decider = number(1, 5)
        if decider == 1:
            name = "The " + choice(adjectives) + " " + choice(weapons) + " Of " + random.choice(nouns)

        elif decider == 2:
            name = choice(adjectives) + " " + choice(weapons)

        elif decider == 3:
            name = "The " + choice(adjectives) + " " + choice(weapons)

        elif decider == 4:
            name = choice(weapons) + " Of The " + choice(adjectives) + " " + choice(nouns)

        elif decider == 5:
            name = "The " + choice(weapons) + " Of The " + choice(adjectives) + " " + choice(nouns)

        return Weapon(name, damage(level))


    return Weapon(choice(adjectives) + " " + choice(weapons), damage(level))


print(weapon(10))
print(globals())
# def spell(level):
