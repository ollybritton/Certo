# Certo v1, a super simple text adventure game.

import cmd
import sys
import os
import time
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
        time.sleep(wait_time)


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


def write_text(string, letter_by_letter=True, should_input=DEFAULT_INPUT, input_end=" " width=SCREEN_WIDTH, end="\r\n", delay_settings=None):
    # TODO: Still need to implement the input mode.
    # TODO: Add the feature where it restricts the length of the text to the SCREEN_WIDTH, breaking on words, not letters.
    """
    Prints text one character at a time with a slight delay. Adds a nice effect to the writing.

    [ string ] !string => A string of what to print.
    [ letter_by_letter ] (True) !boolean => Defines whether the text should be printed one letter at a time.
    [ should_input ] (DEFAULT_INPUT) !boolean => Defines whether the user should have to press enter before proceding.
    [ input_end ] (" ") !string => Defines what should be after the text when input mode is enabled.
    [ width ] (SCREEN_WIDTH) !integer => An integer which controls how long the text should be. Default is the SCREEN_WIDTH.
    [ end ] ("\r\n") !string => What gets printed onto the string. The default is "\r\n", or basically just a newline.
    [ delay_settings ] (None) ~!list => If the value is None (the default), it will use the default waits and whatnot. If a list is specified, the first number specifies the time to wait between letters, and the second is the time to wait before a newline.

    """

    if type(string) is not str:
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

    if type(input_end) is not string:
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

    if type(delay_settings) is not list and delay_settings is not None:
        raise ValueError(
            "'delay_settings' argugument in function write_text should be either a list or None, whereas you gave a {} value.".format(
                type(delay_settings)
            )
        )

    if delay_settings is None:
        delay_settings = DEFAULT_DELAY

    elif list(map(lambda x: type(x), delay_settings)) is not [float, float]:
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

    if letter_by_letter:
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()

            sleep(per_character_delay)

        sys.stdout.write(" ")

        sleep(per_newline_delay)
        sys.stdout.write(end)

        sys.stdout.flush()

    else:
        display(string, end=end)


##############################


write_text("You sit in a small forest, and your legs hurt.",
           delay_settings=[0.1, 0.2], letter_by_letter=False
           )

write_text("You don't know how you got there, yet there's a lingering sense of dread that floods through your veins.",
           delay_settings=[0.1, 0.2]
           )
