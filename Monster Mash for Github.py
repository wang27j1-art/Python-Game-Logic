import random

# MONSTER MASH Creator and Battle
print("MONSTER MASH CREATOR AND BATTLE")
print()

#BATTLE FUNCTION
def monster_battle_bash(monster_1, monster_2):
  print("\n--- MONSTER BATTLE BASH! ---")
  print("BATTLE COMMENCE between " + monster_1["name"] + " and " + monster_2["name"] + "!")

  health_1 = random.randint(100, 250)
  health_2 = random.randint(100, 250)
  round_number = 1

  # Simple battle logic based on the number of monster attacks
  while health_1 > 0 and health_2 > 0:
    print("Round", round_number)

    #attack and damage
    attack_1 = random.choice([20, 35, 40, 55, 60, 75])
    attack_2 = random.choice([20, 35, 40, 55, 60, 75])
    health_1 -= attack_2
    health_2 -= attack_1

    #prints battle results
    print(monster_1["name"] + " attacks for " + str(attack_1) + " damage! " + monster_2["name"] + " has " + str(health_2) + " health.")
    print(monster_2["name"] + " attacks for " + str(attack_2) + " damage! " + monster_1["name"] + " has " + str(health_1) + " health.")

    round_number += 1

  # Decide winner
  if health_1 <= 0 and health_2 <= 0:
    return "It's a draw! Both monsters were defeated!"
  elif health_1 <= 0:
    return "The winner is " + monster_2["name"] + "!"
  else:
    return "The winner is " + monster_1["name"] + "!"

# PART 1: The Body (Using Lists)
my_monster_body = ["head", "eyes", "horns", "arms", "legs", "tail", "wings"]

# PART 2: Create the Parts Catalog using dictionaries
print("--- Picking from the Parts Catalog ---")

#The catalog of available monster parts
head_list = ["a head made of honeycomb covered with crawling insects",
            "a head shaped like a cracked lantern that glows inside with eerie light",
            "a head with fish and barnacles embedded in its skull",
            "jagged volcanic glass shards for a face",
            "a head made of storm clouds with lightning flashing inside",
            "a wooden mask grown from tangled roots that bleed sap",
            "a cracked molten rock glowing from within and and constantly dripping magma",
            "a skull carved from ice, with frost coming out of its mouth like smoke",
            "a face where all facia features are upside down",
            "a face formed by perfect cubes and triangles that shift and rearrange",
            "a face that looks like liquid metal, reflecting but never showing its true form",
            "a face that shows muscles on the outside",
            "a face with a mouth that stretches ear to ear, sewn crudely together",
            "multiple, faces layered and overlapping",
            "a smooth porcelain mask-like face",
            "a face that drips like wax, reforming slowly as the monster moves",
            "a carved stone statue head"
]

eyes_list = ["one eye that spirals infinitely forward like a tunnel",
            "a dozen tiny eyes",
            "two wide horizontal slits",
            "one cloudy, half-decayed eyeball",
            "one eye socket full of writhing tiny serpents",
            "two eyes with irises made of segmented worms twisting slowly",
            "one glowing coal for an eyeball, with ash flakes drifting out",
            "three eyes made of cracked ice crystals that refract light",
            "one hollow eye socket with moss and glowing fungi inside",
            "two blazing sun-like eyes that spit sparks when blinking",
            "four eyes where pupils constantly morph between geometric forms",
            "three eyes that reflect everything like a silver mirror but never show what's inside",
            "an eye with iris and pupil flipped vertically",
            "one eye stacked on top of another in the same socket",
            "eyes scattered randomly across the forehead, cheeks, and tongue",
            "two blank white orbs that track movement"
]

horns_list = ["ten coral reef horns",
              "two branch antlers split and gnarled like winter trees",
              "two massive curling horns cracked and covered in runic etchings",
              "three shark fin horns that slice through air and water",
              "two soft feathery moth antennae that sense vibrations",
              "two crab pincher shaped horns",
              "five black glass shards with a faint glow",
              "four molten horns constantly dripping lava",
              "six metallic lightning rods",
              "four transparent quartz horns",
              "four transparent amethyst horns",
              "two clear frost antlers",
              "three braided vine horns of living plant matter",
              "dozens of tiny horn buds growing out from the skull",
              "two horns with moss, fungus, and tiny flowers growing along cracks",
              "one horn that doubles as nests for insects or bats",
              "one jagged golden ring hovering where the horn should be",
              "three horns made of linked, glowing vertebrae",
              "three horns made of linked, glowing shackles",
              "five smoke horns",
              "six reflective mirror horns"
]

arms_list = ["ten joint arms",
            "two arms with obsidian claws",
            "two branch arms split into jagged wooden claws",
            "one arm replaced with a single curved bone blade",
            "three transparent, crystalline arms that refract light into dangerous beams",
            "four melted flesh arms",
            "eight chitin-covered insect limbs",
            "two chain-bound arms dragging cursed chains",
            "six liquid arms shifting between solid and fluid"
]

legs_list = ["two reverse-jointed beast legs",
              "four thick stone legs",
              "four thick metal legs",
              "four thin spider limbs",
              "four goatlike digitigrade hooves",
              "three rootlike legs",
              "five armored Crustacean legs"
]

tail_list = ["a spine tail",
            "a lantern tail",
            "a thorny whipvine tail",
            "a leech tail",
            "a meteor tail",
            "a mirror shard tail",
            "an insect stinger tail",
            "a smoke tail",
            "a serpent for a tail",
            "rootlike tentacle tails blooming eyes and mouths"
]

wings_list = ["tattered bat wings",
              "glass wings",
              "moth wings",
              "feathered wings",
              "bone wings",
              "tentacle wings",
              "smoke wings",
              "lightning shaped like wings",
              "wings with feathers each containing tiny mouths"
]

monster_parts_catalog = {
  "head": head_list,
  "eyes": eyes_list,
  "horns": horns_list,
  "arms": arms_list,
  "legs": legs_list,
  "tail": tail_list,
  "wings": wings_list
}

# Gets the description for your monster's body parts using the .get() method and print them
my_monster_head = random.choice(monster_parts_catalog["head"])
print("Your monster's head:", my_monster_head)

my_monster_eyes = random.choice(monster_parts_catalog["eyes"])
print("Your monster's eyes:", my_monster_eyes)

my_monster_horns= random.choice(monster_parts_catalog["horns"])
print("Your monster's horns:", my_monster_horns)

my_monster_arms = random.choice(monster_parts_catalog["arms"])
print("Your monster's arms:", my_monster_arms)

my_monster_legs = random.choice(monster_parts_catalog["legs"])
print("Your monster's legs:", my_monster_legs)

my_monster_tail = random.choice(monster_parts_catalog["tail"])
print("Your monster's tail:", my_monster_tail)

my_monster_wings = random.choice(monster_parts_catalog["wings"])
print("Your monster's wings:", my_monster_wings)

print()

# PART 3: The Monster's Name and Description
print("--- Giving your Monster a Name ---")

# Create your monster's name using a string variable and print it
monster_name = input("What do you want to name your monster?: ")
print("My monster's name is:", monster_name)

# Creates a "Loud" version of the name by making all letters uppercase
loud_name = monster_name.upper()
print()

# FINAL STEP: Assemble Your Monster from all three parts to create your final description
print("--- Behold Your Monster! ---")

# Use a string join() to create the final description from the list
body_string = ", ".join(my_monster_body)

# Assemble all the pieces into the final description
my_monster_description = (
"The magnificent monster known as " + loud_name + " has been created!\n"
"It has: " + my_monster_head + "; " + my_monster_eyes + "; " + my_monster_horns + "; " + my_monster_arms + "; " + my_monster_legs + "; " + my_monster_tail + "; and " + my_monster_wings + ".\n"
"Its body is composed of the following parts: " + body_string + "."
)
print(my_monster_description)
print()

#MONSTER BATTLE BASH
# creates first monster to battle
my_monster = {
  "name": monster_name,
  "parts": [my_monster_head,
            my_monster_eyes,
            my_monster_horns,
            my_monster_arms,
            my_monster_legs,
            my_monster_tail,
            my_monster_wings
]}

# creates a list of names for the opponent monster
names_list = ["Vorlath the Undoer", "Kael'torr the Thunder-Marrow", "Drosmeth the Hollow Idol", "Ildraun the Verdant Wraith", "Seraphex the Shattered Reflection"]

# generates parts for the opponent monster
opponent_monster_head = random.choice(monster_parts_catalog["head"])
opponent_monster_eyes = random.choice(monster_parts_catalog["eyes"])
opponent_monster_horns = random.choice(monster_parts_catalog["horns"])
opponent_monster_arms = random.choice(monster_parts_catalog["arms"])
opponent_monster_legs = random.choice(monster_parts_catalog["legs"])
opponent_monster_tail = random.choice(monster_parts_catalog["tail"])
opponent_monster_wings = random.choice(monster_parts_catalog["wings"])

# creates a second monster to battle
opponent_monster = {
  "name": random.choice(names_list),
  "parts": [
            opponent_monster_head,
            opponent_monster_eyes,
            opponent_monster_horns,
            opponent_monster_arms,
            opponent_monster_legs,
            opponent_monster_tail,
            opponent_monster_wings
]}

# Describes the opponent monster
print("--- BUT WAIT... IT'S NOT OVER YET! ---")
opponent_monster_description = (
"Another magnificent monster known as " + opponent_monster["name"].upper() + " has come to fight " + loud_name + "!\n"
"It has: " + opponent_monster_head + "; " + opponent_monster_eyes + "; " + opponent_monster_horns + "; " + opponent_monster_arms + "; " + opponent_monster_legs + "; " + opponent_monster_tail + "; and " + opponent_monster_wings + ".\n"
"Its body is composed of the following parts: " + body_string + "."
)
print(opponent_monster_description)

# begins monster battle
print(monster_battle_bash(my_monster, opponent_monster))
