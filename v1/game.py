# Certo v1, a super simple text adventure game.

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
DEFAULT_INPUT = True

# Speeds up/slows down all wait times to make gameplay faster. 2 = twice as fast, 0.5 = double speed.
SPEED_MODIFIER = 10

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
        [state_information] => Information about the current state, ie the location, current effects...etc. It's stored as a dictionary.
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
            damage => the amount of damage that the weapon does.
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
        return self.attributes["damage"]

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


class Inventory():
    def __init__(self, items):
        """
        The Inventory Class:
        - A way of storing the items the player currently has.

        [items] => A list of all the items in a player's inventory, all Item classes.
        """

        self.items = items

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


def parse_json_item_list_to_list(path):
    data = parse_json(path)
    result = []

    for item in data["items"]:
        result.append(parse_dict_to_class(item))

    return result

###############

### PROGRAM START ###


if __name__ == "__main__":
    try:
        # Should call a single function, main().
        weapons = (parse_json_item_list_to_list("data/weapons.json"))

        write_text(weapons[0].name + ":")
        write_text(weapons[0].description)

        print("")

        write_text("'{}'".format(weapons[0].get_pickup_message()))
        write_text("'{}'".format(weapons[0].get_success_phrase()))
        write_text("'{}'".format(weapons[0].get_failure_phrase()))

        print("")

        write_text("=================")

        print("")

        write_text(weapons[1].name + ":")
        write_text(weapons[1].description)

        print("")

        write_text("'{}'".format(weapons[1].get_pickup_message()))
        write_text("'{}'".format(weapons[1].get_success_phrase()))
        write_text("'{}'".format(weapons[1].get_failure_phrase()))

    except KeyboardInterrupt:
        program_close()

#####################
