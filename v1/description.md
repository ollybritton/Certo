# Certo v1
The very baseline test of the idea. This is basically just my pure thought written down on a page describing how I want to do things.

===
## Creatures & Items Stored
Currently I've opped for a simple JSON file representing a character or item, but that means I need to hard-code a lot of the values like weapons and manually associate them with the character. Instead, I could make a cross link between the two so you would have something like:

```
{
    "type": "enemy",
    "items": [{
        "type": "enemy",
        "name": "Cave Bat",
        "description": "A bat that lingers in a cave.",
        "health": 10,
        "mana": 0,
        "hardness": 0,
  ===>  "weapons": ["data/weapons.json:Bat Claw"]
    }]
}
```
This would create minimal hard-coded values and it would make the creation process a lot easier.

## Combat
### Idea 1: Under Pressure
The player is asked a series of questions and has to answer them in a certain time limit. If they do it in time, they succeed in their action.

This creates a sense of tension and urgency, like there would be in a real battle, and is easily scalable for harder enemies by just reducing the time they have.

For example:

        Ok, remember "5 3 8 7".
        *the screen is cleared*
        What was the number? 

The question topics that I can think of are:

+ Maths
+ Memory
+ Spelling

#### Actual Implementation
Each enemy has a hardness value associated with it. This is a decimal number and it works like so:
Call *x* the hardness value. The time limit for a question is equal to `1-x * (base time)`. This is basically decreasing the `base time` by a percentage of `x`.

For example, if the question **"What's 58+34?"** has a `base time` of 5 seconds and the creature/enemy the player was fighting had a hardness of `0.2`, the `5` seconds becomes `4`. This is because `1 - 0.2 = 0.8`, and `0.8 * 5` is `4`.

## Roadmap
1. Implement a class for enemies and their types.
2. Create a battle mechanic which boils down to one single function, fight(player, enemy).
3. Create a map data structure and implement player location.
4. Implement a location data structure and a way of naviagting locations.
5. Make a game.