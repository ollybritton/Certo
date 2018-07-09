# Certo v1, a text adventure game.

import cmd
import sys
import os
import time
import json
import random
import textwrap

### GLOBAL SETUP VARIABLES ###

# TESTING controls how the game acts and will speed things certain things up for testing purposes.
TESTING = False

# Sets the maximum width that the text can go.
SCREEN_WIDTH = 100

# Sets how fast the text is written on the screen when there is the one letter at a time effect.
DEFAULT_DELAY = [0.1, 0.2]

# Controls if the user should have to hit enter at the end of every line of written text.
DEFAULT_INPUT = False

# Speeds up/slows down all wait times to make gameplay faster. 2 = twice as fast, 0.5 = double speed.
SPEED_MODIFIER = 3

# Defines wether to use the command prompt commands to clear the screen, or just print a bunch of times. Useful for when testing the code using IDLE. The first value is whether to do so, and the second value is the amount of times.
CLEAR_PRINT = [False, 100]

##############################

### BASIC HELPER FUNCTIONS ###


def sleep(wait_time, force=False):
    """
    Waits a certain amount of time, but won't if TESTING variable is set to True and force is False.

    [ wait_time ] !number => The amount of time to wait. Should be a number, so a float or integer.
    [ force ] (False) !bool => If testing mode is enabled, but you still need to wait, force will override that if set to true. Th default is false.
    """

    try:
        wait_time = float(wait_time)

    except:
        raise ValueError(
            "Error trying to convert variable wait_time in sleep function into a float. You put a {}. It needs to be a float or an integer.".format(
                wait_time
            )
        )

    if type(force) is not bool:
        raise ValueError(
            "'force' argument in function sleep should be a bool. You put a {}.".format(
                type(force)
            )
        )

    if TESTING and force is False:
        return

    elif force is True or TESTING is False:
        time.sleep(wait_time / SPEED_MODIFIER)


def display(text, width=SCREEN_WIDTH, end="\r\n"):
    """
    Displays text nicely on a set amount of columns.

    [ text ] !string => A string which contains the text that is to be displayed.
    [ width ] (SCREEN_WIDTH) !integer => An integer which sets the width of the text. The default is SCREEN_WIDTH.
    [ end ] ("\r\n") !string => A string which sets what is printed at the end of a piece of text. The default is "\r\n", which is basically just a newline.
    """

    if type(text) is not str:
        raise ValueError(
            "'text' argument in display function should be a string. You gave a {} value.".format(
                type(text)
            )
        )

    if type(width) is not int:
        raise ValueError(
            "'width' argument in display function should be an integer. You gave a {} value.".format(
                type(width)
            )
        )

    if type(end) is not str:
        raise ValueError(
            "'end' argument in display function should be a string. You gave a {} value.".format(
                type(end)
            )
        )

    text = textwrap.dedent(text).strip()
    print(textwrap.fill(text, width=width), end=end)


def write_text(string, letter_by_letter=True, should_input=DEFAULT_INPUT, input_end=" ", width=SCREEN_WIDTH, end="\r\n", delay_settings=DEFAULT_DELAY):
    """
    Prints text one character at a time with a slight delay. Adds a nice effect to the writing.

    [ string ] !string => A string of what to print.
    [ letter_by_letter ] (True) !boolean => Defines whether the text should be printed one letter at a time.
    [ should_input ] (DEFAULT_INPUT) !boolean => Defines whether the user should have to press enter before proceding.
    [ input_end ] (" ") !string => Defines what should be after the text when input mode is enabled.
    [ width ] (SCREEN_WIDTH) !integer => An integer which controls how long the text should be. Default is the SCREEN_WIDTH.
    [ end ] ("\r\n") !string => What gets printed onto the string. The default is "\r\n", or basically just a newline.
    [ delay_settings ] (DEFAULT_DELAY) !list => The first number in the list specifies the time to wait between letters, and the second is the time to wait before a newline. The default is DEFAULT_DELAY.

    """

    if type(string) is not str:
        try:
            string = str(string)
        except:
            raise ValueError(
                "'string' argugument in function write_text should be a string, whereas you gave a {} value.".format(
                    type(string)
                )
            )

    if type(letter_by_letter) is not bool:
        raise ValueError(
            "'letter_by_letter' argument in function write_text should be a boolean. Your argument has the {} type.".format(
                type(letter_by_letter)
            )
        )

    if type(should_input) is not bool:
        raise ValueError(
            "'should_input' argument in function write_text should be a boolean. You gave a {}.".format(
                type(should_input)
            )
        )

    if type(input_end) is not str:
        raise ValueError(
            "'input_end' argument in function write_text should be a string. You gave a {}.".format(
                type(input_end)
            )
        )

    if type(width) is not int:
        raise ValueError(
            "'width' argugument in function write_text should be a string, whereas you gave a {} value.".format(
                type(width)
            )
        )

    if type(end) is not str:
        raise ValueError(
            "'end' argugument in function write_text should be a string, whereas you gave a {} value.".format(
                type(end)
            )
        )

    if type(delay_settings) is not list:
        raise ValueError(
            "'delay_settings' argugument in function write_text should be either a list or None, whereas you gave a {} value.".format(
                type(delay_settings)
            )
        )

    if list(map(lambda x: type(x), delay_settings)) is not [float, float]:
        try:
            delay_settings = list(map(lambda x: float(x), delay_settings))

        except:
            raise ValueError(
                "'delay_settings' argument should be a list of floats, but the value you gave ({}) wasn't.".format(
                    delay_settings
                )
            )

        if len(delay_settings) is not 2:
            raise ValueError(
                "'delay_settings' argument should be a list of floats, but the value you gave ({}) wasn't.".format(
                    delay_settings
                )
            )

    per_character_delay = delay_settings[0]
    per_newline_delay = delay_settings[1]

    if letter_by_letter and not should_input:
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()

            sleep(per_character_delay)

        sys.stdout.write(" ")

        sleep(per_newline_delay)
        sys.stdout.write(end)

        sys.stdout.flush()

    elif letter_by_letter and should_input:
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()

            sleep(per_character_delay)

        sys.stdout.write(input_end)

        sleep(per_newline_delay)

        input()

        sys.stdout.flush()

    else:
        display(string, end=end)


def clear():
    """
    Clears the terminal window.
    If a mac is being used, it runs the "clear" command.
    If a windows machine is being used, it runs the "cls" command.
    If it can't figure out what system is being used, it will print a newline CLEAR_PRINT[1] times.

    However, it can also be overriden if CLEAR_PRINT[0] is set to true.
    """

    if not CLEAR_PRINT[0]:
        try:
            if os.name == "nt":
                # For windows.
                os.system("cls")

            elif os.name == "posix":
                # For mac/linux.
                os.system("clear")

            else:
                # Unknown operating system, just print a newline a bunch of times.
                print("\n" * CLEAR_PRINT[1])

        except:
            # Can't figure out the operating system, safest bet is to just print a newline a bunch of times.
            print("\n" * CLEAR_PRINT[1])

    else:
        # The clearing of screen is overriden, so we just print a newline CLEAR_PRINT[1] times.
        print("\n" * CLEAR_PRINT[1])


def program_close():
    """
    Exits the program nicely.
    """

    print("\n")
    sys.exit(0)

##############################

### CLASS DEFENITIONS ###

## PLAYER & INVENTORY ###


class Player():
    def __init__(self, name, health, mana, xp, inventory, state_information):
        """
        The Player Class:
        - How the current character is stored, with their name, health & mana, inventory and finally information regarding the current state.

        [name] => The character's name.
        [health] => How much health the current character has. It's stored as a list, with the first element being the current health and the second being the max.
        [mana] => Similar to health, how much 'magical health' the character has. Once again, a list with the first element being the current health and the second being the max.
        [xp] => A single integer which stores how many experience points the character has.
        [inventory] => A implementation of the Inventory class which contains information about what the player currently has.
        [state_information] => Information about the current state, ie the location, current effects...etc. It's stored as a dictionary. Also contains information about equiped weapons and armour.
        """

        self.name = name
        self.health = health
        self.mana = mana
        self.xp = xp
        self.state_information = state_information

        self.inventory = inventory

    # === Health Functions === #

    def set_health(self, new):
        # Sets the current health.
        self.health[0] = new

    def set_max_health(self, new):
        # Updates the maximum health a player can have.
        self.health[1] = new

    def add_health(self, addition):
        # Adds a certain number (addition) to the current health. In the event that it's greater than the max health, then it is capped at the health limit.
        self.health[0] += addition

        if self.health[0] > self.health[1]:
            self.health[0] = self.health[1]

    def remove_health(self, subtraction):
        # Removes a certain amount (subtraction) from the health. In the event that it's less than 0, the health is stopped at 0.
        self.health[0] -= subtraction

        if self.health[0] < 0:
            self.health[0] = 0

    def decimal_health_percentage(self):
        # Returns the percentage of the max health that is the current health. In decimal form.
        return float(self.health[0])/float(self.health[1])

    def string_health_percentage(self, dp=0):
        # Returns the percentage of the max health that is the current health in the range 0 to 100. Takes into account a desired amount of decimal places.
        result = str(round(self.decimal_health_percentage()
                           * 100 * (10 ** dp)) / (10 ** dp))

        if dp is 0:
            # Remove trailing ".0" if 0 decimal places are requested.
            result = result[:len(result) - 2]

        return result

    # === Mana Functions === #

    def set_mana(self, new):
        # Sets the current mana.
        self.mana[0] = new

    def set_max_mana(self, new):
        # Updates the maximum mana a player can have.
        self.mana[1] = new

    def add_mana(self, addition):
        # Adds a certain number (addition) to the current mana. In the event that it's greater than the max mana, then it is capped at the mana limit.
        self.mana[0] += addition

        if self.health[0] > self.mana[1]:
            self.mana[0] = self.mana[1]

    def remove_mana(self, subtraction):
        # Removes a certain amount (subtraction) from the mana. In the event that it's less than 0, the mana is stopped at 0.
        self.mana[0] -= subtraction

        if self.mana[0] < 0:
            self.mana[0] = 0

    def decimal_mana_percentage(self):
        # Returns the percentage of the max mana that is the current mana. In decimal form.
        return float(self.mana[0])/float(self.mana[1])

    def string_mana_percentage(self, dp=0):
        # Returns the percentage of the max mana that is the current mana in the range 0 to 100. Takes into account a desired amount of decimal places.
        result = str(round(self.decimal_mana_percentage()
                           * 100 * (10 ** dp)) / (10 ** dp))

        if dp is 0:
            # Remove trailing ".0" if 0 decimal places are requested.
            result = result[:len(result) - 2]

        return result

    # === XP Functions ==# #

    def set_xp(self, new):
        self.xp = new

    def add_xp(self, addition):
        self.xp += addition

    def remove_xp(self, subtraction):
        self.xp -= subtraction


class Inventory():
    def __init__(self, items):
        """
        The Inventory Class:
        - A way of storing the items the player currently has.

        [items] => A list of all the items in a player's inventory, all Item classes.
        """

        self.items = items

    def weapons(self):
        return list(filter(lambda x: type(x) is Weapon, self.items))

    def apparel(self):
        return list(filter(lambda x: type(x) is Apparel, self.items))

    def potions(self):
        return list(filter(lambda x: type(x) is Potion, self.items))

    def food(self):
        return list(filter(lambda x: type(x) is Food, self.items))

    def keys(self):
        return list(filter(lambda x: type(x) is Key, self.items))

    def spells(self):
        return list(filter(lambda x: type(x) is Spell, self.items))


class Item():
    def __init__(self, name, description, item_type, attributes):
        """
        The Item Class:
        - A class that represents an item that the player could possess.

        [name] => The name of the item. For example, "Axe of War" or "Key to Home".
        [description] => A description of the item, aka something that dictates the function of the item.

        [item_type] => The type of the item. These can be:
                       - "weapon" (Weapon class)
                       - "apparel" (Apparel class)
                       - "potion" (Potion class)
                       - "food" (Food class)
                       - "key" (Key class)
                       - "spell" (Spell class)

        [attributes] => The information associated with the item, like how much damage it does or what it unlocks.

        """

        self.name = name
        self.description = description
        self.item_type = item_type
        self.attributes = attributes


class Weapon(Item):
    def __init__(self, name, description, attributes):
        """
        Weapon Class:
        - Represents an item which is a weapon. This means it can be used to create damage and is not a direct result of magic, like a spell.

        [attributes] => {
            damage => the amount of damage that the weapon does. Represented as a dice roll, like in DND.
            pickup_message => the message printed on the screen when the user first gets the weapon.
            luck => a value that messes with how likely an action is to proceed. This should correlate with the name. So a weapon called "God-Like Axe" should be luckier than "Shabby Dagger".
            success_action_phrases => a list of phrases that are said when the user successfully makes an action with the weapon.
            failure_action_phrases => a list of phrases that are said when the user doesn't make an attack successfully.
            xp_level => The amount of XP the player should have before recieving the weapon.
        }
        """

        super().__init__(
            name=name,
            description=description,
            item_type="weapon",
            attributes=attributes
        )

    def get_damage(self):
        dice = self.attributes["damage"].split("d")
        results = []

        for i in range(dice[0]):
            results.append(random.randint(1, dice[1]))

        return sum(results)

    def get_pickup_message(self):
        return self.attributes["pickup_message"]

    def get_success_phrase(self):
        return random.choice(self.attributes["success_action_phrases"])

    def get_failure_phrase(self):
        return random.choice(self.attributes["failure_action_phrases"])


class Apparel(Item):
    def __init__(self, name, description, attributes):
        """
        Apparel Class:
        - Represents an item which is used to protect the player. This means that it reduces damage.

        [attributes] => {
            rating => a measure of how well this will stop incoming damage.
            pickup_message => the message printed on screen when the user first gets the armour.
            luck => a value that controls how much damage the armour will repel. Once again, this should correlate to the name of the item.
            success_action_phrases => a list of phrases that are said when the armour/apparel does an especially good job of protecting the player from damage.
            failure_action_phrases => a list of phrases that are said when the armour/apparel does an especially bad job at protecting the player from damage.
            xp_level => The amount of XP the player should have before recieving the apparel/armour.
        }
        """

        super().__init__(
            name=name,
            description=description,
            item_type="apparel",
            attributes=attributes
        )


class Potion(Item):
    def __init__(self, name, description, attributes):
        # TODO: Add potion attributes.

        super().__init__(
            name=name,
            description=description,
            item_type="potion",
            attributes=attributes
        )


class Food(Item):
    def __init__(self, name, description, attributes):
        # TODO: Add food attributes.

        super().__init__(
            name=name,
            description=description,
            item_type="food",
            attributes=attributes
        )


class Key(Item):
    def __init__(self, name, description, attributes):
        # TODO: Add key attributes.

        super().__init__(
            name=name,
            description=description,
            item_type="key",
            attributes=attributes
        )


class Spell(Item):
    def __init__(self, name, description, attributes):
        # TODO: Add spell attributes.

        super().__init__(
            name=name,
            description=description,
            item_type="spell",
            attributes=attributes
        )

#########################

### ENEMIES ###


class Enemy():
    def __init__(self, name, description, health, mana, hardness, attacks, buffs, state_information):
        """
        The Enemy Class:
        - Represents an enemy that a player might fight. Different from a player in a number of ways.

        [name] => The name of the enemy, stored as a string.
        [description] => A description of the enemy, stored as a string.
        [health] => A measure of how many more damage the enemy can take before dying. Stored as a list with two items,the first being the current amount of health, and the second the maxium amount of health.
        [mana] => Similar to health, how much "magical health" the enemy has. Once again, a list with two items, the first the current amount of mana and the second being the maximum amount of mana.
        [hardness] => A measure of how difficult the enemy is to fight. This influences the base reaction times that are given, and a higher number shortens the time allowed.
        [attacks] => Similar to an inventory, but instead a list of attacks, not weapons.
        [buffs] => Similar to an inventory, stores things that might buff the enemy, for example it healing itself.
        [state_information] => Stores additional information about the current state of the enemy.
        """

        self.name = name
        self.description = description
        self.health = health
        self.mana = mana

        self.hardness = hardness

        self.attacks = attacks
        self.buffs = buffs

        self.state_information = state_information

    # === Health Functions === #

    def set_health(self, new):
        # Sets the current health.
        self.health[0] = new

    def set_max_health(self, new):
        # Updates the maximum health an enemy can have.
        self.health[1] = new

    def add_health(self, addition):
        # Adds a certain number (addition) to the current health. In the event that it's greater than the max health, then it is capped at the health limit.
        self.health[0] += addition

        if self.health[0] > self.health[1]:
            self.health[0] = self.health[1]

    def remove_health(self, subtraction):
        # Removes a certain amount (subtraction) from the health. In the event that it's less than 0, the health is stopped at 0.
        self.health[0] -= subtraction

        if self.health[0] < 0:
            self.health[0] = 0

    def decimal_health_percentage(self):
        # Returns the percentage of the max health that is the current health. In decimal form.
        return float(self.health[0])/float(self.health[1])

    def string_health_percentage(self, dp=0):
        # Returns the percentage of the max health that is the current health in the range 0 to 100. Takes into account a desired amount of decimal places.
        result = str(round(self.decimal_health_percentage()
                           * 100 * (10 ** dp)) / (10 ** dp))

        if dp is 0:
            # Remove trailing ".0" if 0 decimal places are requested.
            result = result[:len(result) - 2]

        return result

    # === Mana Functions === #

    def set_mana(self, new):
        # Sets the current mana.
        self.mana[0] = new

    def set_max_mana(self, new):
        # Updates the maximum mana an enemy can have.
        self.mana[1] = new

    def add_mana(self, addition):
        # Adds a certain number (addition) to the current mana. In the event that it's greater than the max mana, then it is capped at the mana limit.
        self.mana[0] += addition

        if self.health[0] > self.mana[1]:
            self.mana[0] = self.mana[1]

    def remove_mana(self, subtraction):
        # Removes a certain amount (subtraction) from the mana. In the event that it's less than 0, the mana is stopped at 0.
        self.mana[0] -= subtraction

        if self.mana[0] < 0:
            self.mana[0] = 0

    def decimal_mana_percentage(self):
        # Returns the percentage of the max mana that is the current mana. In decimal form.
        return float(self.mana[0])/float(self.mana[1])

    def string_mana_percentage(self, dp=0):
        # Returns the percentage of the max mana that is the current mana in the range 0 to 100. Takes into account a desired amount of decimal places.
        result = str(round(self.decimal_mana_percentage()
                           * 100 * (10 ** dp)) / (10 ** dp))

        if dp is 0:
            # Remove trailing ".0" if 0 decimal places are requested.
            result = result[:len(result) - 2]

        return result

    # === Hardness Functions === #

    def hardness_multiplier(self):
        return 1.0 - self.hardness

    def adjusted_time(self, time):
        return time * self.hardness_multiplier()


class Attacks():
    def __init__(self, attacks):
        """
        The Attacks Class:
        Stores the different attacks (things that do damage in a way) that an enemy can perform.

        [attacks] => A list of the different types of attack the enemy can do.
        """

        self.attacks = attacks


class EnemyWeapon():
    def __init__(self, name, description, damage, success_action_phrases, failure_action_phrases, luck):
        """
        The EnemyWeapon class:
        - Stores an attack which involves a melee weapon that can be used by an enemy to a player.

        [name] => The name of a weapon, represented by a string.
        [description] => The description of the weapon that the enemy is using. Written from the player's point of view.
        [damage] => The amount of damage the weapon does, represented by a dice roll string. For example, "1d6" or "12d20".
        [success_action_phrases] => Phrases which describe to the player what happens when an attack using the weapon is a success.
        [failure_action_phrases] => Phrases which describe to the player what happens when an attack using the weapon fails.
        [luck] => A numerical value that influences how likely an attack is to succeed using this weapon.
        """

        self.name = name
        self.description = description

        self.damage = damage
        self.success_action_phrases = success_action_phrases
        self.failure_action_phrases = failure_action_phrases

        self.luck = luck

    def get_damage(self):
        dice = self.damage.split("d")
        results = []

        for i in range(dice[0]):
            results.append(random.randint(1, dice[1]))

        return sum(results)

    def get_success_phrase(self):
        return random.choice(self.success_action_phrases)

    def get_failure_phrase(self):
        return random.choice(self.failure_action_phrases)


class EnemySpell():
    # TODO: Create EnemySpell class.
    pass


class Buffs():
    def __init__(self, buffs):
        """
        The Buffs Class:
        Stores the different buffs the enemy can give to itself, such as healing.

        [buffs] => A list of the different buffs.
        """

        self.buffs = buffs

        # TODO: Create buffs for healing and whatnot.

#########################

### PARSING ###


def parse_json(path):
    with open(path, "r") as f:
        return json.loads(f.read())


def parse_dict_to_class(data):
    if data["type"] == "weapon":
        return Weapon(
            name=data["name"],
            description=data["description"],
            attributes={
                "damage": data["attributes"]["damage"],
                "pickup_message": data["attributes"]["pickup_message"],
                "luck": data["attributes"]["luck"],
                "success_action_phrases": data["attributes"]["success_action_phrases"],
                "failure_action_phrases": data["attributes"]["failure_action_phrases"],
                "xp_level": data["attributes"]["xp_level"]
            }
        )

    if data["type"] == "apparel":
        return Apparel(
            name=data["name"],
            description=data["description"],
            attributes={
                "rating": data["attributes"]["rating"],
                "pickup_message": data["attributes"]["pickup_message"],
                "luck": data["attributes"]["luck"],
                "success_action_phrases": data["attributes"]["success_action_phrases"],
                "failure_action_phrases": data["attributes"]["failure_action_phrases"],
                "xp_level": data["attributes"]["xp_level"]
            }
        )

    if data["type"] == "enemy":
        return Enemy(
            name=data["name"],
            description=data["description"],
            health=[data["health"], data["health"]],
            mana=[data["mana"], data["mana"]],
            hardness=data["hardness"],
            attacks=Attacks([]),
            buffs=Buffs([]),
            state_information={}
        )


def parse_json_item_list_to_list(path):
    data = parse_json(path)
    result = []

    for item in data["items"]:
        result.append(parse_dict_to_class(item))

    return result

###############

### FIGHT FUNCTIONS ###


def fight(player, enemy):
    """
    Triggers a fight between a player and an enemy.

    Fights are quite unique in this game. The enemy's chance of succeeding are based purely on chance, but the player's are measured in their ability to think under pressure.

    There are three types of questions:
    + Math - Questions like "59 + 23".
    + Memory - Questions like "What was that number I just showed you?"
    + Spelling - Questions like "How do you spell that word I just showed you?"

    The player is timed in how long it takes them to answer. If they take a long time to answer, it's likely their action won't succeed. If they do so very quickly, then they do.

    There are several actions that the player can perform inside a fight. These are:
    + Inpect - Find out the enemy's true health, instead of just an indicator like "It's pretty beat up."
    + Attack/Fight - Use the currently equiped weapon/spell to try and do some damage to the enemy.
    + Heal - Attempt to restore one's own health.
    + Equip - Equip a different spell/weapon.
    + Use - Attempt to use a potion or something similar.
    """

#######################

### TESTING FUNCTIONs ###


def print_weapon(weapon, write_mode=False):
    if not write_mode:
        display("Name: {}".format(weapon.name))
        display("Description: {}".format(weapon.description))

        print("")

        display("Pickup Message: '{}'".format(
            weapon.attributes["pickup_message"]))
        display("Successful Action: '{}'".format(weapon.get_success_phrase()))
        display("Pickup Message: '{}'".format(weapon.get_failure_phrase()))

        print("")

        display("Luck: {}".format(weapon.attributes["luck"]))
        display("XP Level: {}".format(weapon.attributes["xp_level"]))

    else:
        write_text("Name: {}".format(weapon.name))
        write_text("Description: {}".format(weapon.description))

        print("")

        write_text("Pickup Message: '{}'".format(
            weapon.attributes["pickup_message"])
        )

        write_text("Successful Action: '{}'".format(
            weapon.get_success_phrase())
        )

        write_text("Pickup Message: '{}'".format(weapon.get_failure_phrase()))

        print("")

        write_text("Luck: {}".format(weapon.attributes["luck"]))
        write_text("XP Level: {}".format(weapon.attributes["xp_level"]))
        write_text("Name: {}".format(weapon.name))
        write_text("Description: {}".format(weapon.description))

        print("")

        write_text("Pickup Message: '{}'".format(
            weapon.attributes["pickup_message"])
        )

        write_text("Successful Action: '{}'".format(
            weapon.get_success_phrase())
        )

        write_text("Pickup Message: '{}'".format(weapon.get_failure_phrase()))

        print("")

        write_text("Luck: {}".format(weapon.attributes["luck"]))
        write_text("XP Level: {}".format(weapon.attributes["xp_level"]))

### PROGRAM START ###


if __name__ == "__main__":
    try:
        # Should call a single function, main().
        enemies = (parse_json_item_list_to_list("data/enemies.json"))

        for e in enemies:
            print(e)
            print("\n")

    except KeyboardInterrupt:
        program_close()

#####################
