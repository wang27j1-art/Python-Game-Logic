import random

# --------------------------------------------------------------------------
# SPACE DUEL LAB
print("STARSHIP CREATOR AND SPACE DUEL")

#BATTLE FUNCTION
def starship_duel(ship_a, ship_b):
    print("\n--- STARSHIP DUEL! ---")
    print("BATTLE COMMENCE between " + ship_a["name"] + " and " + ship_b["name"] + "!")
          
    health_a = random.randint(750, 2000)
    health_b = random.randint(750, 2000)
    round_number = 1

    # Simple battle logic based on the number of ship attacks.
    while health_a > 0 and health_b > 0:
        print("Round", round_number)

        #attack and damage
        damage_a_to_b = max(0, ship_a["power"] - ship_b["defense"])
        damage_b_to_a = max(0, ship_b["power"] - ship_a["defense"])
        

        #stops game if both ships deal 0 damage
        if damage_a_to_b == 0 and damage_b_to_a == 0:
            print("ERROR: Can't start game because both ships deal 0 damage.")
            break


        #subtracts damage from starship health
        health_a -= damage_b_to_a
        health_b -= damage_a_to_b


        # prints battle results
        print(ship_a['name'] + " fires, dealing " + str(damage_a_to_b) + " damage! " + ship_b["name"] + " Hull: " + str(health_b))
        print(ship_b['name'] + " fires, dealing " + str(damage_b_to_a) + " damage! " + ship_a["name"] + " Hull: " + str(health_a))

        round_number += 1

    #Decide winner
    if health_a <= 0 and health_b <= 0:
        print("It's a draw! Both ships were blown up.")
    elif health_a <= 0:
        print("The winner is " + ship_b["name"] + "!")
    else:
        print("The winner is " + ship_a["name"] + "!")
        
# PART 1: The Ship (Using Lists)
# Your ship's body starts with a basic sequence of parts.
# Use list methods to add, remove, and reorder parts.

print()

# Creates an initial list of ship parts and print the list.
my_starship_parts = ["core", "weapons"]

print("--- Picking from the Parts Catalog ---")

# The catalog of available monster parts
ship_cores = ["a Quantum Singularity Core",
              "a Fusion Nexus Core",
              "an Antimatter Reactor"
              "a Solar Helix Core",
              "a Dark Matter Heart",
              "a Chrono Core",
              "an Aether Crystal Core",
              "a Void Engine",
              "a Biofusion Core",
              "a Neural Symbiote Core",
              "a Spore Hive Core",
              "a Nanoforge Core",
              "a Phase Resonator Core",
              "an EMP Pulse Core",
              "a Warp Flux Core",
              "a Stellar Forge Core",
              "an Entropy Core",
              "an Eternal Engine",
              "a Celestial Choir Core",
              "an Omega Seed Core"
              ]

weapon_types = ["Pulse Cannons",
                "Railguns",
                "Beam Lasers",
                "a Focused Burst (charged plasma)",
                "Missile Salvos",
                "Torpedoes",
                "EMP Projectors",
                "Virus Launchers",
                "Drone Swarms",
                "a Tether Beam",
                "Gravity Manipulators",
                "a Quantum Torment",
                "Boarding Modules",
                "a Signature Cascade",
                "Adaptive Ammo Systems",
                "Sonic Cannons",
                "Resonance Cannons",
                "a Reality Rend"
             ]
             
             

starship_catalog = {
    "core": ship_cores,
    "weapons": weapon_types
}

# TODO: Get the description for the "core" and "weapons" by using
# the .get() method and print them
my_starship_core = random.choice(starship_catalog["core"])
print("1. Your starship's core:", my_starship_core)

my_starship_weapons = random.choice(starship_catalog["weapons"])
print("2. Your starship's weapons:", my_starship_weapons)
print()

# PART 3: The Monster's Name and Description (Using Strings)
print("--- Giving Your Starship a Name ---")

# Create your monster's name using a string variable and print it
starship_name = input("What do you want to name your starship?: ")
print("3. My starship is:", starship_name)

# TODO: Find the length of your monster's name and print it
name_length = len(starship_name)
print("4. The length of the name is:", name_length)

# TODO: Create a "Loud" version of the name by making all letters uppercase
# Print the "Loud" version of name
loud_name = starship_name.upper()
print('5. A "loud" version of the name is:', loud_name)
print()

# FINAL STEP: Assemble Your Monster from all three parts
# to create the final description!
print("--- Behold Your Starship! ---")

# Use a string join() to create the final body description from the list
starship_parts_string = ", ".join(my_starship_parts)

# Assemble all the pieces into a final description
my_starship_description = (
    "The magnificent starship known as " + loud_name + " has been created!\n"
    "It has " + my_starship_core + " and " + my_starship_weapons + ".\n"
    "Its body is composed of the following parts: " + starship_parts_string + ".")


print(my_starship_description)

#SPACE DUEL BASH

names_list = ["Valorwing",
              "Nova Lance",
              "Starbreaker",
              "Radiant Dawn",
              "Celestia Prime",
              "Dauntless Voyager",
              "Eclipse Vanguard",
              "Aurora's Edge",
              "Odyssey's Flame",
              "Starlance",
              "Quantum Horizon",
              "Helios Array"
              "Photon Spear",
              "Neural Dawn",
              "Spectra-9",
              "Lumen Ark",
              "Ionis Vector",
              "Zero-Point Runner",
              "Datawind",
              "Chronos Relay",
              "Oblivion Fang",
              "Crimson Vortex",
              "Dread Nova",
              "Warforge Titan",
              "Rift Predator",
              "Ashen Halo",
              "Reaper's Orbit",
              "Infernal Horizon",
              "Voidhammer",
              "Maelstrom Warden",
              "Black Nebula",
              "Silent Comet",
              "Shade Vector",
              "Wraith Serpent",
              "Phantom Pulse",
              "Umbra Wing",
              "Eidolon Veil",
              "Vesper Ghost",
              "Noctis Mirage",
              "Specter's Edge",
              "Aetherion",
              "Nyx-Seed",
              "Orryx Veil",
              "Vyr'thal Core",
              "Luminar Eidolon",
              "Zerathyn Bloom",
              "Ka'Tal Nexus",
              "Echo of Ithra",
              "Seraph Spiral",
              "Voidheart Ascendant",
              "Iron Nomad",
              "Forge Runner",
              "Atlas-12",
              "Hollowstrike",
              "Cobalt Jackal",
              "Salvager's Hope",
              "Rust Halo",
              "Hammerfall",
              "Outrider Delta",
              "Titan's Debt",
              "Aurora Pilgrim",
              "Harmony Reach",
              "Stellar Compass",
              "Unity Ark",
              "Parallax Voyager",
              "Constellation Grace",
              "Frontier Whisper",
              "Nova Shepherd",
              "Celestial Envoy",
              "Eden's Path"]

# creates an array of power amounts for both starships to choose from
power_array = [100, 120, 145, 175, 200]

# creates an array of defense amounts for both starships to choose from
defense_array = [75, 90, 110, 135, 150]

# selects a random power amount for your starship
my_starship_power = random.choice(power_array)

# selects a random power amount for the opponent starship
opponent_starship_power = random.choice(power_array)

# selects a random defense amount for your starship
my_starship_defense = random.choice(defense_array)

# selects a random defense amount for the opponent starship
opponent_starship_defense = random.choice(defense_array)

# creates first starship to battle                                           
my_starship = {
    "name": starship_name,
    "power": my_starship_power,
    "defense": my_starship_defense,
    "systems": [my_starship_core,
              my_starship_weapons
    ]}


# generates parts for the opponent starship
opponent_starship_core = random.choice(ship_cores)
opponent_starship_systems = random.choice(weapon_types)

# creates second starship to battle
opponent_starship = {
    "name": random.choice(names_list),
    "power": opponent_starship_power,
    "defense": opponent_starship_defense,
    "systems": [
        opponent_starship_core,
        opponent_starship_systems,
        ]}

print()

# Creates a description for the opponent starship
print("--- BUT WAIT... IT'S NOT OVER YET! ---")
opponent_starship_description = (
    "Another magnificent starship known as " + opponent_starship["name"].upper() + " has arrived to battle " + loud_name + "!\n"
    "It has " + opponent_starship_core + " and " + opponent_starship_systems + ".\n"
    "Its body is composed of the following parts: " + starship_parts_string + ".")


# prints opponent starship description
print(opponent_starship_description)


# begins starship battle
starship_duel(my_starship, opponent_starship)
