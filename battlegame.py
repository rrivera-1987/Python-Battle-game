wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose Your Character:")
    
    if character == "1":
        print("You have chosen:",wizard)
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("Health:", wizard_hp)
        print("Damage:", wizard_damage,'\n')
        break
    if character == "2":
        print("You have chosen:",elf)
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("Health:", elf_hp)
        print("Damage:", elf_damage,'\n')
        break
    if character == "3":
        print("You have chosen the character:",human)
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("Health:", human_hp)
        print("Damage:", human_damage,'\n')
        break
    else:
        print("Unknown character")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The",character, "damaged the dragon")
    print("The Dragon's hitpoints are now: ", dragon_hp,'\n')
    if dragon_hp == 0:
        print("The Dragon has lost the battle!")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon stirkes back at the", character)
    print("The",character,"'s hitpoints are now:", my_hp,'\n')
    if my_hp == 0:
        print("The",character, "has lost the battle!")
        break
