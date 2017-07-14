## Notes
Where I document new ideas and concepts for the game.

+ Item
  + Free item from monster or facilities.
  + Destroy an item or enemy who has gone crazy as a result of it.
  + Transport an item.
  + Create an item.

+ NPC
  + Free an item from a hostile or facility.
  + Guard an NPC on a route somewhere.

+ Message
  + Kill somebody sending a message.

+ Location
  + Free a facility from enemy capture.
  + Destroy a facility.
  + Guard a facility from enemy siege.
  + Crete your own location (would be very difficult)

+ Monster/Hostile
  + Kill a monster.

### XP
Current level is:
`xp/15`

### Progression.
Progression should be on an XP based system, where NPCs and quests dynamically change as the player progresses.

### Events
+ Intro
  + Player should be made to demo all these different types of quests in just the intro.
  + For example, you attempt to get an item from an NPC, but they already placed it into a facility. Then you must attack the facility in order to get the item.

### Sounds
We need sounds for the following:
+ A Correct Input ("correct.wav")  
+ An Incorrect Input ("incorrect.wav")
+ Hit ("hit.wav")
+ Swoosh ("swoosh_1.wav", "swoosh_2.wav")
+ Heal ("heal.wav")
+ Death ("death.wav")
+ Win ("win.wav")
+ Power up/Level up ("level.wav")
+ Item in list ("click.wav")
<!-- + Mumur for speak ()
+ Evil Laugh () -->
+ XP gain ("xp.wav")

### Damage
Battles are fun when they're hard, and are matched to your skill.
So, the damage for any weapon or spell is: `(5*level)/2 + number(0, 3)`
And the health is: `15 + health + number(0, 3)`, which is calculated every level-up.
