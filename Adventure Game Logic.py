import random

# --------------------------------------------------------------------------
# ADVENTURE GAME LOGIC

# Note: This version may contain minor syntax issues.
# It represents my full game design and logic structure.
# Encounter flow, battle system, and exploration are fully outlined.

class Game:
    health = 100
    attack = 20
    defense = 10
    score = 0

    random_outcomes = ["Good", "Bad", "End"]

    enemies = {
        "Echoing Growl": {
            "name": "Stone Maw Beast",
            "attack": 25,
            "defense": 15,
            "health": 80,
            "description": "a hulking creature made of rock and sinew. Its roar shakes the cavern walls. Hard to injure, but slow to move.",
            "health award": 20,
            "attack award": 3,
            "defense award": 2
            },
        "Cave Bandits": {
            "name": "The Black Lantern Gang",
            "attack": 20,
            "defense": 10,
            "health": 60,
            "description": "A group of ruthless thieves who haunt the tunnels, their torches dim to hide ambushes.",
            "health award": 12,
            "attack award": 2,
            "defense award": 1
            },
        "Wild Animal Ambush": {
            "name": "Dire Wolf".
            "attack": 15,
            "defense": 5,
            "health": 50,
            "description": "A massive wolf with silver fur and amber eyes, fierce and territorial.",
            "health award": 8,
            "attack award": 1,
            "defense award": 1
            },
        "Bandit Trap": {
            "name": "Redleaf Invaders",
            "attack": 18,
            "defense": 8,
            "health": 55,
            "description": "Foreign raiders draped in red leaves, using snares and smoke bombs to trap wanderers."
            "health award": 10,
            "attack award": 2,
            "defense award": 1
            },
        "Cursed Clearing": {
            "name": "Spectral Warden",
            "attack": 22,
            "defense": 12,
            "health": 70,
            "description": "A translucent spirit bound to the forest by ancient magic, its hollow eyes judge all who trespass."
            "health award": 15,
            "attack award": 3,
            "defense award": 2
            },
        "Haunted Chamber": {
            "name": "Phantom Knights",
            "attack": 28,
            "defense": 10,
            "health": 85,
            "description": "Once noble guardians, now cursed shadows of armor that fight with ghostly blades."
            "health award": 25,
            "attack award": 4,
            "defense award": 3
            }
        }
            
        
    town_names = ["Briarwood", "Silverhollow", "Stonegate", "Ravenshire",
                  "Windmere", "Ironvale", "Ashford", "Thornbrook",
                  "Moonveil", "Elderglow", "Starhaven", "Mistvale",
                  "Solmere", "Luminara", "Frostveil", "Whisperfen",
                  "Hollowfen", "Blackhollow", "Dreadmoor", "Gloomspire",
                  "Bloodmere", "Wraithcross", "Nightfall",
                  "Puddlewick", "Bumbleton", "Maplehollow", "Sunberry",
                  "Cobblepot", "Meadowbrook", "Twillton"]
        

    town_descriptions = {
        "Briarwood": "A quiet town nestled among thorny brambles, where traders whisper of beasts in the forest.",
        "Silverhollow": "A mining village that glows faintly at night, its silver veins pulsing under the earth.",
        "Stonegate": "A fortified settlement build around a massive stone arch said to guard an ancient secret.",
        "Ravenshire": "Black-feathered ravens circle the rooftops --- locals claim they're guardians, not omens.",
        "Windmere": "Rolling fields surround this breezy town where windmills hum soft, haunting tunes.",
        "Ironvale": "A valley settlement where blacksmiths forge both weapons and legends.",
        "Ashford": "Built upon old ashes, the town thrives again --- resilient and proud.",
        "Thornbrook": "A humble riverside town filled with herbalists and wandering bards.",
        "Moonveil": "Silvery mist drifts through the streets, and moonlight never fades here --- even at dawn.",
        "Elderglow": "Lanterns float mid-air, casting soft gold over cobblestone paths.",
        "Starhaven": "A sanctuary for travelers, where wishes whispered at night often come true.",
        "Mistvale": "Fog curls through every alley --- some say it carries echoes of ancient spirits.",
        "Solmere": "Warm sunlight never leaves this peaceful town, said to be protected by divine magic.",
        "Luminara": "Crystals line the streets, glowing brighter when kind hearts pass by.",
        "Frostveil": "A chilly town where snow never melts and laughter echoes like bells.",
        "Whisperfen": "Even the wind speaks here --- softly warning travelers of their fates.",
        "Hollowfen": "Sunlight rarely reaches this swampy settlement --- only the croak of unseen creatures breaks the silence.",
        "Blackhollow": "Every door is locked by dusk, and not a single light burns after midnight.",
        "Dreadmoor": "Thick fog and distant church bells echo over its flooded streets."
        "Gloomspire": "Tall, leaning towers scrape the clouds, home to reclusive scholars and stranger things.",
        "Bloodmere": "A crimson-stained marsh surrounds this cursed village --- they say the ground drinks deeply.",
        "Wraithcross": "Shadows move on their own, whispering names that haven't been spoken in centuries.",
        "Nightfall": "Eternal twilight cloaks this town, where time itself seems to have stopped.",
        "Puddlewick": "Children splash through cobbled puddles as shopkeepers hum old tunes.",
        "Bumbleton": "The scent of honey and warm bread fills the air --- bees are practically citizens here.",
        "Maplehollow": "Golden leaves dance year-round, and locals greet every traveler like an old friend.",
        "Sunberry": "Baskets of fruit line every stall; laughter is the only currency that matters.",
        "Cobblepot": "Known for its clattering teapots and mismatched houses that lean against each other.",
        "Meadowbrook": "A brook runs through the heart of town, filled with sparkling fish and good luck charms.",
        "Twillton": "Tiny windmills spin in every yard, each painted with a child's favorite story."
        }
        
    
    endgame_prompts = {
        "Echoing Growl": "You were crushed beneath the paws of the Stone Maw Beast as the cavern shook violently.",
        "Cave Bandits": "You were overwhelmed by the Black Lantern Gang, struck down in the shadows of the tunnels.",
        "Collapsing Tunnel": "You were buried under falling rocks when the tunnel collapsed around you.",
        "Wild Animal Ambush": "You were ripped apart by the Dire Wolf before you could escape the forest.",
        "Bandit Trap": "You were caught by the Redleaf Invaders, leaving no chance to survive.",
        "Cursed Clearing": "You were consumed by the magic of the Spectral Warden, disappearing into the cursed clearing.",
        "Treasure Vault": "Youtriggered a deadly trap in the Treasure vault and succumbed to its poison.",
        "Haunted Chamber": "You were cut down by the Phantom Knights, joining their ranks as shadows forever.",
        "Ancient Guardian": "You fell to the Ancient Guardian's strike, crushed under its relentless might.",
        }
        


    def explore_random(cls):
        print("--- Status: Health =", health, "Score =", score, "---")
        choice = int(input("Where do you want to explore? (1 = cave, 2 = forest, 3 = town, 4 = dungeon, 5 = QUIT): ")
        if choice == 1:
            print(explore_cave(cls))
        elif choice == 2:
            print(enter_forest(cls))
        elif choice == 3:
            print(enter_town(cls))
        elif choice == 4:
            print(enter_dungeon(cls))
        else:
            print(end_game(cls))

    def explore_random_again(cls):
        print("You recover and can choose your next adventure.")
        print(explore_random(cls))

    def explore_cave(cls):
        cave_encounters = ["Echoing Growl", "Cave Bandits", "Collapsing Tunnel"]
        one_cave_encounter = random.choice(cls.cave_encounters)
        if one_cave_encounter == "Echoing Growl":
            choice = input("The ground trembles --- something big is moving in the dark. Do you FIGHT, FLEE, or HIDE? ")
            if choice.upper() == "FIGHT":
                print("You light a torch and prepare to strike.")
                print(fight(cls, "Echoing Growl"))
            elif choice.upper() == "FLEE":
                print("You slip back toward the tunnel entrance quietly.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You slip through the tunnels and escape unseen! (+10 score)")
                    cls.score += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You stumble over loose rocks and scrape yourself. (-15 health)")
                    cls.health -= 15
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The beast spots you as you flee. Its roar ends everything.")
                    cls.health = 0
            else:
                print("You snuff your torch and press against the wall until the creature passes.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You hold your breath as the creature passes. The air stills again. (+10 score)")
                    cls.score += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("Your torch flickers --- the beast snarls and swipes at the shadows. (-20 health)")
                    cls.health -= 15
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The beast senses your fear and crushes the wall you hide behind.")
                    cls.health = 0
                    
        elif one_cave_encounter == "Cave Bandits":
            choice = input("Torches flicker ahead --- voices echo down stone walls. Do you FIGHT, FLEE, or SNEAK? ")
            if choice.upper() == "FIGHT":
                print("You launch a surprise attack.")
                print(fight(cls, one_cave_encounter))
            elif choice.upper() == "FLEE":
                print("You retreat before the bandits notice you.")
                outcome = random.choice(cls.random_outcomes):
                    if outcome == "Good":
                        print("You dash through a side tunnel and vanish before they notice. (+20 score)")
                        cls.score += 20
                        print(explore_random_again(cls))
                    elif outcome == "Bad":
                        print("You drop your pouch while running! (-15 score)")
                        cls.score = max(score - 15, 0)
                        if cls.health > 0:
                            print(explore_random_again(cls))
                    else:
                        print("A stray arrow catches you as you turn a corner.")
                        cls.health = 0
                        
            else:
                print("You try to sneak around the bandits' camp unnoticed.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You move silently and overhear plans of hidden treasure. (+25 score)")
                    cls.score += 25
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You bump a lantern, and the camp erupts in chaos! (-25 health)")
                    cls.health -= 25
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("A knife flashes in the dark. You never even see who threw it.")
                    cls.health = 0
        else:
            choice = input("Rocks begin to fall --- the whole cavern is trembling. Do you HOLD, FLEE, or SEARCH? ")
            if choice.upper() == "HOLD":
                print("You try to brace a support beam or push debris away.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You brace a beam and save yourself from the collapse. (+15 score)")
                    cls.score += 15
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("Debris falls on you, bruising your shoulder. (-20 health)")
                    cls.health -=20
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The ceiling caves in before you can move.")
                    cls.health = 0
            elif choice.upper() == "FLEE":
                print("You dash for safety before the tunnel collapses.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You sprint to safety as rocks thunder behind you. (+10 score)")
                    cls.score += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("A falling rock clips your leg. (-15 health)")
                    cls.health -= 15
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("You trip and never make it out.")
                    cls.health = 0
            else:
                print("You look for a side passage or hidden alcove.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You find a hidden alcove filled with old supplies! (+20 score)")
                    cls.score += 20
                    cls.health = min(cls.health + 10, 100)
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You waste time and dust chokes you. (-10 health)")
                    cls.health -= 10
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The tunnel seals forever.")
                    cls.health = 0
                

    def enter_forest():
        forest_encounters = ["Wild Animal Ambush", "Bandit Trap", "Cursed Clearing"]
        one_forest_encounter = random.choice(cls.forest_encounter)
        if one_forest_encounter == "Wild Animal Ambush":
            choice = input("You hear wild rustling --- a pair of glowing eyes peek through the bushes. Do you FIGHT, FLEE, or DISTRACT? ")
            if choice.upper() == "FIGHT":
                print("You grab a fallen branch and stand your ground.")
                print(fight(cls, one_forest_encounter))
            elif choice.upper() == "FLEE":
                print("You sprint through some trees and hope you can outpace the animal.")
                outcome = random.choice(random_outcomes):
                if outcome == "Good":
                    print("You outrun the beast and find a safe clearing. (+15 score)")
                    print(explore_random_again(cls))
                    cls.score += 15
                elif outcome == "Bad":
                    print("You trip over roots and scrape your arm. (-10 health)")
                    cls.health -= 10
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The creature pounces before you can react.")
                    cls.health = 0
            else:
                print("You throw some food or make a loud noise to lure it away.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You toss food aside and the beast wanders off. (+10 score)")
                    print(explore_random_again(cls))
                    cls.score += 10
                elif outcome == "Bad":
                    print("Your distraction fails --- the beast charges at you (-20 health")
                    cls.health -= 20
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("Your trick enrages the creature --- it tears through everything.")
                    cls.health = 0
                    
        elif one_forest_encounter == "Bandit Trap":
            choice = input("A snare snaps around your ankle --- laughter echoes from the shadows. Do you FIGHT, FLEE, or NEGOTIATE? ")
            if bandit_trap_choice.upper() == "FIGHT":
                print("You try to cut yourself free and face the bandits.")
                print(fight(cls, one_forest_encounter))
            elif bandit_trap_choice.upper() == "FLEE":
                print("You use smoke or forest terrain to escape.")
                print(fight(cls, one_forest_encounter))
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You break free and escape into the woods. (+20 score)")
                    cls.score += 20
                elif outcome == "Bad":
                    print("You cut yourself escaping the snare. (-10 health)")
                    print(explore_random_again(cls))
                    cls.health -= 10
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("You fail to escape before the bandits arrive.")
                    cls.health = 0
            else:
                print("You offer the bandits something shiny in exchange for mercy.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("Your words win the bandits over --- they even share supplies! (+25 score)")
                    cls.score += 25
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("The bandits take your coins and leave you bruised. (-20 health, -15 score)")
                    health -= 20
                    cls.score = max(cls.score - 15, 0)
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The bandits laugh and draw blades. Everything fades.")
                    cls.health = 0
        else:
            choice = input("The air hums with magic; strange shapes flicker in the mist. Do you FIGHT, FLEE, OR INVESTIGATE? ")
            if choice == "FIGHT":
                print("You try to dispel the spirits with your weapon or spell.")
            elif cursed_clearing_choice == "FLEE":
                print("You back away before the curse spreads.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You escape before the strange lights close in. (+10 score)")
                    cls.score += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You inhale the mist and cough violently (-15 health)")
                    cls.health -= 15
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The mist consumes you entirely.")
                    cls.health = 0
            else:
                print("You try to understand what's causing the phenomenon.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You uncover an ancient charm glowing with power! (+25 score, +10 health)")
                    cls.score += 25
                    cls.health += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You touch a cursed rune --- it burns your skin. (-20 health)")
                    cls.health -= 20
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("A ghostly figure reaches out and ends your story.")
                    cls.health = 0

    def fight(cls, encounter):
        enemy_name = cls.enemies[encounter["name"]]
        enemy_description = cls.enemies[encounter["description"]]
        print("BATTLE COMMENCE against " + enemy_name + "! " + enemy_description)
        
        combat_health = cls.health
        enemy_health = cls.enemies[encounter["health"]]
        round_number = 1

        while combat_health > 0 and enemy_health > 0:
            print("Round", round_number)

            #attack and damage
            your_attack = max(0, cls.attack - cls.enemies[encounter["defense"]])
            enemy_attack = max(0, cls.enemies[encounter["attack"]] - cls.defense)

            #prevents the fight if both player and enemy deal 0 damage
            if your_attack == 0 and enemy_attack == 0:
                print(enemy_name, "lets you leave without a fight.")

            #subtracts damage from health
            combat_health -= enemy_attack
            enemy_health -= your_attack

            #prints battle results
            print("You attack " + enemy_name + ", dealing " + your_attack + ". " + enemy_name + " has " + enemy_health + "."_)
            print(enemy_name + " attacks you, dealing " + enemy_attack + ". You have " + combat_health + "."

            #increases number of rounds
            round_number += 1

        #Decide winner
        if combat_health <= 0 and enemy_health <= 0:
            print("It's a draw! Both you and " + enemy_name + " died fighting.")
        elif combat_health <= 0:
            print("Yay! You won the fight against " + enemy_name ".")
            health += cls.enemies[encounter["health award"]]
            attack += cls.enemies[encounter["attack award"]]
            defense += cls.enemies[encounter["defense award"]]
            print(explore_random_again(cls))
        else:
            print("Uh-oh! " + enemy_name + " defeated you in combat.")
            health = 0
        
    def enter_town(cls):
        current_town = random.choice(cls.town_names)
        print("You arrive at the mysterious town of " + current_town + ". " + town_descriptions[current_town]
        town_outcome = random.choice(cls.random_outcomes)
        if outcome == "Good":
            print("You find a friendly healer who restores your strength! (+30 health, +20 score)")
            cls.health += 30
            cls.score += 20
            print(explore_random_again(cls))
        elif outcome == "Bad":
            print("A thief steals from your pouch while you rest! (-15 score)")
            cls.score = max(score - 10, 0)
            if cls.health > 0:
                print(explore_random_again(cls))
        else:
            print("The town was cursed --- spectral hands drag you beneath the cobblestones.")
            cls.health = 0

    def enter_dungeon(cls):
        print("You descend into the dungeon --- the air grows cold and torches flicker on their own.")
        dungeon_encounters = ["Treasure Vault", "Haunted Chamber", "Ancient Guardian"]
        one_dungeon_encounter = random.choice(dungeon_encounters)
        if one_dungeon_encounter == "Treasure Vault":
            treasure_vault_choice = input("The vault glitters with gold. Do you LOOT, INSPECT, or LEAVE?")
            if treasure_vault_choice.upper() == "LOOT":
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You fill your pack with treasure! (+50 score)")
                    cls.score +=50
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("A poison dart hits your arm! (-25 health)")
                    cls.health -= 25
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("The vault was cursed --- darkness consumes you...")
                    cls.health = 0
            elif treasure_vault_choice.upper() == "INSPECT":
                print("You carefully examine the runes and mechanisms.")
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("You safely disable a trap and find a rare gem! (+30 score)")
                    cls.score += 30
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("You trigger a gas trap! (-20 health)")
                    cls.health -= 20
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("A hidden mechanism locks the door forever...")
                    cls.health = 0
            else:
                print("You leave the vault untouched, your instincts telling you it's best not to risk it.")
        elif one_dungeon_encounter == "Haunted Chamber":
            haunted_chamber_choice = input("Ghostly whispers surround you. Do you FIGHT, FLEE, or PRAY? ")
            if haunted_chamber_choice.upper() == "FIGHT":
                print("You swing at the shadows --- the air freezes around your weapon!")
                print(fight(cls, one_dungeon_encounter))
            elif haunted_chamber_choice.upper() == "FLEE":
                outcome = random.choice(random_outcomes)
                if outcome == "Good":
                    print("You escape before the spirits can follow! (+10 score)")
                    cls.score += 10
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("A phantom grazes your soul as you flee! (-30 health)")
                    cls.health -= 30
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("You vanish into the mist, never to beseen again...")
                    cls.health = 0
            else:
                outcome = random.choice(cls.random_outcomes)
                if outcome == "Good":
                    print("Light surrounds you, banishing the spirits! (+20 score, +20 health")
                    cls.score += 20
                    cls.health += 20
                    print(explore_random_again(cls))
                elif outcome == "Bad":
                    print("Your prayer goes unanswered... the spirits mock your weakness. (-10 score)
                    cls.score = max(score - 10, 0)
                    if cls.health > 0:
                        print(explore_random_again(cls))
                else:
                    print("You join the spirits --- now one of them forever.")
                    cls.health = 0
        else:
            outcome = random.choice(cls.random_outcomes)
            if outcome == "Good":
                print("You present a relic --- the guardian bows and grants you passage! (+25 score)")
                cls.score += 25
                print(explore_random_again(cls))
            elif outcome == "Bad":
                print("The guardian sees through your bluff and strikes you down. (-35 health)")
                cls.health -= 35
                if cls.health > 0:
                    print(explore_random_again(cls))
            else:
                print("The guardian unleashes its ancient fury --- the dungeon shakes apart...")
                cls.health = 0
        
        
                
    def end_game(cls, encounter):
        print("Final score:", score)
        if choice == 5:
            return "Game Over: You manually exited the game."
        else:
            return "Game Over:", cls.endgame_prompts[encounter]
        

        
    def pause(cls):
        input("\nPress Enter to continue...")

    def clear(cls):
        if os.name == 'nt':
            os.system('cls')  # Windows
        else:
            os.system('clear')  # Unix/Linux/Mac
            
    def Game.start_game(cls):
        while cls.health > 0 or choice !==5:
            print(explore_random(cls, encounter))
        else:
            if choice == 5:
                print("Game Over: You manually exited the game.")
            elif choice == "FIGHT":
                print("Game Over: You died fighting against " + enemy_name)
            else:
                print("Game Over:", endgame_prompts[encounter])

print(Game.start_game(cls))
