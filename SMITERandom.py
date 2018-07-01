import random
import sys
dir(random)
from random import randint

# Start to the Function
def Start():
    options = ["start","physical","magical","p","m","assassin","warrior","hunter","mage","guardian","achilles","agni","ah muzen cab","amc","ah puch","amaterasu","anhur","anubis","goobis","ao kuang","aphrodite","apollo","arachne","ares","artemis","artio","athena","awilix","bacchus","bakasura","baron samedi","bastet","bellona","cabrakan","camazotz","cerberus","cernunnos","chaac","chang'e","change","chernobog","chiron","chronos","cu chulainn","cu chu","cupid","da ji","discordia","erlang shen","fafnir","fenrir","freya","ganesha","ganesh","geb","guan yu","hachiman","hades","he bo","hel","hercules","hou yi","hun batz","isis","izanami","janus","jing wei","kali","khepri","kukulkan","kuku","kumbhakarna","kumbha","kuzenbo","loki","cancer","medusa","mercury","ne zha","trap","neith","nemesis","nike","nox","nu wa","odin","osiris","poseidon","ra","raijin","rama","ratatoskr","ravana","scylla","serqet","skadi","sobek","sol","sun wunkong","susano","sylvanus","terra","thanatos","the morrigan","thor","thoth","not a chicken","tyr","ullr","vamana","vulcan","xbalanque","xing tian","ymir","masterhat","zeus","zhong kui","ghostbusters"]
    choice = ""
    while choice not in options:
        print('''Welcome to the SMITE Random God and Build Generator v1.03 by elijahn't.
Enter a God of your choice, a Class of your choice, Physical or Magical, or type
Start for a random God.''')
        choice = str(input(">>>")).lower()
    if choice == options[0]:
        randomgod = randint(1,2)
    # Physical God Random
        if randomgod == 1:
            print("Randomizing, hold onto your memes!")
            print("You got a Physical God!")
            physical()
    # Magical God Random
        if randomgod == 2:
            print("Randomizing, hold onto your memes!")
            print("You got a Magical God!")
            magical()
    # Physical God Choice
    if choice == options[1]:
        print("You chose a Random Physical God!")
        physical()
    if choice == options[3]:
        print("You chose a Random Physical God!")
        physical()
    # Magical God Choice
    if choice == options[2]:
        print("You chose a Random Magical God!")
        magical()
    if choice == options[4]:
        print("You chose a Random Magical God!")
        magical()
    if choice == options[5]:
        print("You have chosen a Random Assassin!")
        assassin()
    if choice == options[6]:
        print("You have chosen a Random Warrior!")
        warrior()
    if choice == options[7]:
        print("You have chosen a Random Hunter!")
        hunter()
    if choice == options[8]:
        print("You have chosen a Random Mage!")
        mage()
    if choice == options[9]:
        print("You have chosen a Random Guardian!")
        guardian()
    if choice == options[10]:
        print("You have chosen Achilles!")
        chosenPhysical()
    if choice == options[11]:
        print("You have chosen Agni!")
        chosenMagical()
    if choice == options[12]:
        print("You have chosen Ah Muzen Cab!")
        chosenPhysical()
    if choice == options[13]:
        print("You have chosen Ah Muzen Cab!")
        chosenPhysical()
    if choice == options[14]:
        print("You have chosen Ah Puch!")
        chosenMagical()
    if choice == options[15]:
        print("You have chosen Amaterasu!")
        chosenPhysical()
    if choice == options[16]:
        print("You have chosen Anhur!")
        chosenPhysical()
    if choice == options[17]:
        print("You have chosen Anubis!")
        chosenMagical()
    if choice == options[18]:
        print("You have chosen Goobis!")
        chosenMagical()
    if choice == options[19]:
        print("You have chosen Ao Kuang!")
        chosenMagical()
    if choice == options[20]:
        print("You have chosen Aphrodite!")
        chosenMagical()
    if choice == options[21]:
        print("You have chosen Apollo!")
        chosenPhysical()
    if choice == options [22]:
        print("You have chosen Arachne!")
        chosenPhysical()
    if choice == options[23]:
        print("You have chosen Ares!")
        chosenMagical()
    if choice == options[24]:
        print("You have chosen Artemis!")
        chosenPhysical()
    if choice == options[25]:
        print("You have chosen Artio!")
        chosenMagical()
    if choice == options[26]:
        print("You have chosen Athena!")
        chosenMagical()
    if choice == options[27]:
        print("You have chosen Awilix!")
        chosenPhysical()
    if choice == options[28]:
        print("You have chosen Bacchus!")
        chosenMagical()
    if choice == options[29]:
        print("You have chosen Bakasura!")
        chosenPhysical()
    if choice == options[30]:
        print("You have chosen Baron Samedi!")
        chosenMagical()
    if choice == options[31]:
        print("You have chosen Bastet!")
        chosenPhysical()
    if choice == options[32]:
        print("You have chosen Bellona!")
        chosenPhysical()
    if choice == options[33]:
        print("You have chosen Cabroken!")
        chosenMagical()
    if choice == options[34]:
        print("You have chosen Camazotz!")
        chosenPhysical()
    if choice == options[35]:
        print("You have chosen Cerberus!")
        chosenMagical()
    if choice == options[36]:
        print("You have chosen Cernunnos!")
        chosenPhysical()
    if choice == options[37]:
        print("You have chosen Chaac!")
        chosenPhysical()
    if choice == options[38]:
        print("You have chosen Chang'e!")
        chosenMagical()
    if choice == options[39]:
        print("You have chosen Chang'e!")
        chosenMagical()
    if choice == options[40]:
        print("You have chosen Chernobog!")
        chosenPhysical()
    if choice == options[41]:
        print("You have chosen Chiron!")
        chosenPhysical()
    if choice == options[42]:
        print("You have chosen Chronos!")
        chosenMagical()
    if choice == options[43]:
        print("You have chosen Cu Chulainn")
        chosenPhysical()
    if choice == options[44]:
        print("You have chosen the Choo Choo Train!")
        chosenPhysical()
    if choice == options[45]:
        print("You have chosen Cupid!")
        chosenPhysical()
    if choice == options[46]:
        print("You have chosen Da Ji!")
        chosenPhysical()
    if choice == options[47]:
        print("You have chosen Discordia!")
        chosenMagical()
    if choice == options[48]:
        print("You have chosen Erlang Shen!")
        chosenPhysical()
    if choice == options [49]:
        print("You have chosen Fafnir!")
        chosenMagical()
    if choice == options[50]:
        print("You have chosen Fenrir!")
        chosenPhysical()
    if choice == options[51]:
        print("You have chosen Freya!")
        chosenMagical()
    if choice == options[52]:
        print("You have chosen Ganesha!")
        chosenMagical()
    if choice == options[53]:
        print("You have chosen Ganesha!")
        chosenMagical()
    if choice == options[54]:
        print("You have chosen Geb!")
        chosenMagical()
    if choice == options[55]:
        print("You have chosen Guan Yu!")
    if choice == options[56]:
        print("You have chosen Hachiman!")
        chosenPhysical()
    if choice == options[57]:
        print("You have chosen Hades!")
        chosenPhysical()
    if choice == options[58]:
        print("You have chosen He Bo!")
        chosenMagical()
    if choice == options[59]:
        print("You have chosen Hel!")
        chosenMagical()
    if choice == options[60]:
        print("You have chosen Hercules!")
        chosenPhysical()
    if choice == options[61]:
        print("You have chosen Hou Yi!")
        chosenPhysical()
    if choice == options[62]:
        print("You have chosen Hun Batz!")
        chosenPhysical()
    if choice == options[63]:
        print("You have chosen Isis!")
        chosenMagical()
    if choice == options[64]:
        print("You have chosen Izanami!")
        chosenPhysical()
    if choice == options[65]:
        print("You have chosen Janus!")
        chosenMagical()
    if choice == options[66]:
        print("You have chosen Jing Wei!")
        chosenPhysical()
    if choice == options[67]:
        print("You have chosen Kali!")
        chosenPhysical()
    if choice == options[68]:
        print("You have chosen Khepri!")
        chosenMagical()
    if choice == options[69]:
        print("You have chosen Kukulkan!")
        chosenMagical()
    if choice == options[70]:
        print("You have chosen Kukulkan!")
        chosenMagical()
    if choice == options[71]:
        print("You have chosen Kumbhakarna!")
        chosenMagical()
    if choice == options[72]:
        print("You have chosen Kumbhakarna!")
        chosenMagical()
    if choice == options[73]:
        print("You have chosen Kuzenbo, the King of the Kappa!")
        chosenMagical()
    if choice == options[74]:
        print("You have chosen Loki!")
        chosenPhysical()
    if choice == options[75]:
        print("You have chosen Loki!")
        chosenPhysical()
    if choice == options[76]:
        print("You have chosen Medusa!")
        chosenPhysical()
    if choice == options[77]:
        print("You have chosen Mercury!")
        chosenPhysical()
    if choice == options[78]:
        print("You have chosen Ne Zha!")
        chosenPhysical()
    if choice == options[79]:
        print("You have chosen the trap, Ne Zha!")
        chosenPhysical()
    if choice == options[80]:
        print("You have chosen Neith!")
        chosenPhysical()
    if choice == options[81]:
        print("You have chosen Nemesis!")
        chosenPhysical()
    if choice == options[82]:
        print("You have chosen Nike!")
        chosenPhysical()
    if choice == options[83]:
        print("You have chosen Nox!")
        chosenMagical()
    if choice == options[84]:
        print("You have chosen Nu Wa!")
        chosenMagical()
    if choice == options[85]:
        print("You have chosen Odin!")
        chosenPhysical()
    if choice == options[86]:
        print("You have chosen Osiris!")
        chosenPhysical()
    if choice == options[87]:
        print("You have chosen Poseidon!")
        chosenMagical()
    if choice == options[88]:
        print("You have chosen Ra!")
        chosenMagical()
    if choice == options[89]:
        print("You have chosen Raijin!")
        chosenMagical()
    if choice == options[90]:
        print("You have chosen Rama!")
        chosenPhysical()
    if choice == options[91]:
        print("You have chosen Ratatoskr!")
        Ratatoskr()
    if choice == options[92]:
        print("You have chosen Ravana!")
        chosenPhysical()
    if choice == options[93]:
        print("You have chosen Scylla!")
        chosenMagical()
    if choice == options[94]:
        print("You have chosen Serqet!")
        chosenPhysical()
    if choice == options[95]:
        print("You have chosen Skadi!")
        chosenPhysical()
    if choice == options[96]:
        print("You have chosen Sobek!")
        chosenMagical()
    if choice == options[97]:
        print("You have chosen Sol!")
        chosenMagical()
    if choice == options[98]:
        print("You have chosen Sun Wukong!")
        chosenPhysical()
    if choice == options[99]:
        print("You have chosen Susano!")
        chosenPhysical()
    if choice == options[100]:
        print("You have chosen Sylvanus!")
        chosenMagical()
    if choice == options[101]:
        print("You have chosen Terra!")
        chosenMagical()
    if choice == options[102]:
        print("You have chosen Thanatos!")
        chosenPhysical()
    if choice == options[103]:
        print("You have chosen The Morrigan!")
        chosenMagical()
    if choice == options[104]:
        print("You have chosen Thor!")
        chosenPhysical()
    if choice == options[105]:
        print("You have chosen Thoth!")
        chosenMagical()
    if choice == options[106]:
        print("You have chosen the Ibis, Thoth! He's not a chicken!")
        chosenMagical()
    if choice == options[107]:
        print("You have chosen Tyr!")
        chosenPhysical()
    if choice == options[108]:
        print("You have chosen Ullr!")
        chosenPhysical()
    if choice == options[109]:
        print("You have chosen Vamana!")
        chosenPhysical()
    if choice == options[110]:
        print("You have chosen Vulcan!")
        chosenMagical()
    if choice == options[111]:
        print("You have chosen Xbalanque!")
        chosenPhysical()
    if choice == options[112]:
        print("You have chosen Xing Tian!")
        chosenMagical()
    if choice == options[113]:
        print("You have chosen Ymir!")
        chosenMagical()
    if choice == options[114]:
        print("You have chose the Guardian King of Duel's Main, Ymir!")
        chosenMagical()
    if choice == options[115]:
        print("You have chosen Zeus!")
        chosenMagical()
    if choice == options[116]:
        print("You have chosen Zhong Kui!")
        chosenMagical()
    if choice == options[117]:
        print("You have chosen Ghostbusters!")
        chosenMagical()

def Ratatoskr():
    print("~//~"'\n')
    print("Acorn of Yggdrasil")
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()



def chosenMagical():
    print("~//~"'\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Shoes of the Magi")
        if boots == 2:
            print("Shoes of Focus")
        if boots == 3:
            print("Reinforced Shoes")
        if boots == 4:
            print("Traveler's Shoes")
    boots()

    items = [None]*5

    def MagicalBuild():
            item = randint(1, 50)
            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emporer's Armor"
            if item == 5:
                return "Pythagorem's Piece"
            if item == 6:
                return "Bancroft's Talon"
            if item == 7:
                return "Typhon's Fang"
            if item == 8:
                return "Soul Gem"
            if item == 9:
                return "Brestplate of Valor"
            if item == 10:
                return "Spectral Armor"
            if item == 11:
                return "Magi's Cloak"
            if item == 12:
                return "Hide of the Urchin"
            if item == 13:
                return "Spirit Robe"
            if item == 14:
                return "Mantle of Discord"
            if item == 15:
                return "Bulwark of Hope"
            if item == 16:
                return "Pestilence"
            if item == 17:
                return "Heartward Amulet"
            if item == 18:
                return "Talisman of Energy"
            if item == 19:
                return "Demonic Grip"
            if item == 20:
                return "Telekhines Ring"
            if item == 21:
                return "Shaman's Ring"
            if item == 22:
                return "Hastened Ring"
            if item == 23:
                return "Obsidian Shard"
            if item == 24:
                return "Divine Ruin"
            if item == 25:
                return "Spear of the Magus"
            if item == 26:
                return "Spear of Desolation"
            if item == 27:
                return "Gem of Isolation"
            if item == 28:
                return "Warlock's Staff"
            if item == 29:
                return "Etheral Staff"
            if item == 30:
                return "Rod of Asclepius"
            if item == 31:
                return "Book of Thoth"
            if item == 32:
                return "Polynomicon"
            if item == 33:
                return "Soul Reaver"
            if item == 34:
                return "Book of the Dead"
            if item == 35:
                return "Rod of Tahuti"
            if item == 36:
                return "Chronos' Pendant"
            if item == 37:
                return "Celestial Legion Helm"
            if item == 38:
                return "Lotus Crown"
            if item == 39:
                return "Jade Emperor's Crown"
            if item == 40:
                return "Stone of Gaia"
            if item == 41:
                return "Shield of Regrowth"
            if item == 42:
                return "Mail of Renewal"
            if item == 43:
                return "Gauntlet of Thebes"
            if item == 44:
                return "Genji's Guard"
            if item == 45:
                return "Oni Hunter's Garb"
            if item == 46:
                return "Shogun's Kusari"
            if item == 47:
                return "Void Stone"
            if item == 48:
                return "Stone of Fal"
            if item == 49:
                return "Hide of the Nemean Lion"
            if item == 50:
                return "Doom Orb"


    items[0] = MagicalBuild()
    items[1] = MagicalBuild()
    items[2] = MagicalBuild()
    items[3] = MagicalBuild()
    items[4] = MagicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = MagicalBuild()

    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

def chosenPhysical():
    print("~//~"'\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Warrior Tabi")
        if boots == 2:
            print("Ninja Tabi")
        if boots == 3:
            print("Reinforced Greaves")
        if boots == 4:
            print("Talaria Boots")
    boots()
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()





#Guardian Choice
def guardian():
    god = randint(1,17)
    if god == 1:
        print("You got Ares")
    if god == 2:
        print("You got Artio")
    if god == 3:
        print("You got Athena")
    if god == 4:
        print("You got Bacchus")
    if god == 5:
        print("You got Cabrakan")
    if god == 6:
        print("You got Cerberus")
    if god == 7:
        print("You got Fafnir")
    if god == 8:
        print("You got Ganesha")
    if god == 9:
        print("You got Geb")
    if god == 10:
        print("You got Khepri")
    if god == 11:
        print("You got Kumbhakarna")
    if god == 12:
        print("You got Kuzenbo, cool as a cucumber!")
    if god == 13:
        print("You got Sobek")
    if god == 14:
        print("You got Sylvanus")
    if god == 15:
        print("You got Terra")
    if god == 16:
        print("You got Xing Tian")
    if god == 17:
        print("You got Ymir")
    print("~//~" '\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Shoes of the Magi")
        if boots == 2:
            print("Shoes of Focus")
        if boots == 3:
            print("Reinforced Shoes")
        if boots == 4:
            print("Traveler's Shoes")
    boots()
    items = [None]*5

    def MagicalBuild():
            item = randint(1, 50)
            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emporer's Armor"
            if item == 5:
                return "Pythagorem's Piece"
            if item == 6:
                return "Bancroft's Talon"
            if item == 7:
                return "Typhon's Fang"
            if item == 8:
                return "Soul Gem"
            if item == 9:
                return "Brestplate of Valor"
            if item == 10:
                return "Spectral Armor"
            if item == 11:
                return "Magi's Cloak"
            if item == 12:
                return "Hide of the Urchin"
            if item == 13:
                return "Spirit Robe"
            if item == 14:
                return "Mantle of Discord"
            if item == 15:
                return "Bulwark of Hope"
            if item == 16:
                return "Pestilence"
            if item == 17:
                return "Heartward Amulet"
            if item == 18:
                return "Talisman of Energy"
            if item == 19:
                return "Demonic Grip"
            if item == 20:
                return "Telekhines Ring"
            if item == 21:
                return "Shaman's Ring"
            if item == 22:
                return "Hastened Ring"
            if item == 23:
                return "Obsidian Shard"
            if item == 24:
                return "Divine Ruin"
            if item == 25:
                return "Spear of the Magus"
            if item == 26:
                return "Spear of Desolation"
            if item == 27:
                return "Gem of Isolation"
            if item == 28:
                return "Warlock's Staff"
            if item == 29:
                return "Etheral Staff"
            if item == 30:
                return "Rod of Asclepius"
            if item == 31:
                return "Book of Thoth"
            if item == 32:
                return "Polynomicon"
            if item == 33:
                return "Soul Reaver"
            if item == 34:
                return "Book of the Dead"
            if item == 35:
                return "Rod of Tahuti"
            if item == 36:
                return "Chronos' Pendant"
            if item == 37:
                return "Celestial Legion Helm"
            if item == 38:
                return "Lotus Crown"
            if item == 39:
                return "Jade Emperor's Crown"
            if item == 40:
                return "Stone of Gaia"
            if item == 41:
                return "Shield of Regrowth"
            if item == 42:
                return "Mail of Renewal"
            if item == 43:
                return "Gauntlet of Thebes"
            if item == 44:
                return "Genji's Guard"
            if item == 45:
                return "Oni Hunter's Garb"
            if item == 46:
                return "Shogun's Kusari"
            if item == 47:
                return "Void Stone"
            if item == 48:
                return "Stone of Fal"
            if item == 49:
                return "Hide of the Nemean Lion"
            if item == 50:
                return "Doom Orb"


    items[0] = MagicalBuild()
    items[1] = MagicalBuild()
    items[2] = MagicalBuild()
    items[3] = MagicalBuild()
    items[4] = MagicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = MagicalBuild()

    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()


def mage():
    god = randint(1,28)
    if god == 1:
        print("You got Agni")
    if god == 2:
        print("You got Ah Puch")
    if god == 3:
        print("You got Anubis")
    if god == 4:
        print("You got Ao Kuang")
    if god == 5:
        print("You got Aphrodite")
    if god == 6:
        print("You got Baron Samedi")
    if god == 7:
        print("You got Chang'e")
    if god == 8:
        print("You got Chronos")
    if god == 9:
        print("You got Discordia")
    if god == 10:
        print("You got Freya")
    if god == 11:
        print("You got Hades")
    if god == 12:
        print("You got He Bo")
    if god == 13:
        print("You got Hel")
    if god == 14:
        print("You got Isis")
    if god == 15:
        print("You got Janus")
    if god == 16:
        print("You got Kukulkan")
    if god == 17:
        print("You got Nox")
    if god == 18:
        print("You got Nu Wa")
    if god == 19:
        print("You got Poseidon")
    if god == 20:
        print("You got Ra")
    if god == 21:
        print("You got Raijin")
    if god == 22:
        print("You got Scylla")
    if god == 23:
        print("You got Sol")
    if god == 24:
        print("You got The Morrigan")
    if god == 25:
        print("You got Thoth")
    if god == 26:
        print("You got Vulcan")
    if god == 27:
        print("You got Zeus")
    if god == 28:
        print("You got Zhong Kui")
    print("~//~" '\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Shoes of the Magi")
        if boots == 2:
            print("Shoes of Focus")
        if boots == 3:
            print("Reinforced Shoes")
        if boots == 4:
            print("Traveler's Shoes")
    boots()

    items = [None]*5

    def MagicalBuild():
            item = randint(1, 50)
            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emporer's Armor"
            if item == 5:
                return "Pythagorem's Piece"
            if item == 6:
                return "Bancroft's Talon"
            if item == 7:
                return "Typhon's Fang"
            if item == 8:
                return "Soul Gem"
            if item == 9:
                return "Brestplate of Valor"
            if item == 10:
                return "Spectral Armor"
            if item == 11:
                return "Magi's Cloak"
            if item == 12:
                return "Hide of the Urchin"
            if item == 13:
                return "Spirit Robe"
            if item == 14:
                return "Mantle of Discord"
            if item == 15:
                return "Bulwark of Hope"
            if item == 16:
                return "Pestilence"
            if item == 17:
                return "Heartward Amulet"
            if item == 18:
                return "Talisman of Energy"
            if item == 19:
                return "Demonic Grip"
            if item == 20:
                return "Telekhines Ring"
            if item == 21:
                return "Shaman's Ring"
            if item == 22:
                return "Hastened Ring"
            if item == 23:
                return "Obsidian Shard"
            if item == 24:
                return "Divine Ruin"
            if item == 25:
                return "Spear of the Magus"
            if item == 26:
                return "Spear of Desolation"
            if item == 27:
                return "Gem of Isolation"
            if item == 28:
                return "Warlock's Staff"
            if item == 29:
                return "Etheral Staff"
            if item == 30:
                return "Rod of Asclepius"
            if item == 31:
                return "Book of Thoth"
            if item == 32:
                return "Polynomicon"
            if item == 33:
                return "Soul Reaver"
            if item == 34:
                return "Book of the Dead"
            if item == 35:
                return "Rod of Tahuti"
            if item == 36:
                return "Chronos' Pendant"
            if item == 37:
                return "Celestial Legion Helm"
            if item == 38:
                return "Lotus Crown"
            if item == 39:
                return "Jade Emperor's Crown"
            if item == 40:
                return "Stone of Gaia"
            if item == 41:
                return "Shield of Regrowth"
            if item == 42:
                return "Mail of Renewal"
            if item == 43:
                return "Gauntlet of Thebes"
            if item == 44:
                return "Genji's Guard"
            if item == 45:
                return "Oni Hunter's Garb"
            if item == 46:
                return "Shogun's Kusari"
            if item == 47:
                return "Void Stone"
            if item == 48:
                return "Stone of Fal"
            if item == 49:
                return "Hide of the Nemean Lion"
            if item == 50:
                return "Doom Orb"


    items[0] = MagicalBuild()
    items[1] = MagicalBuild()
    items[2] = MagicalBuild()
    items[3] = MagicalBuild()
    items[4] = MagicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = MagicalBuild()

    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

def hunter():
    god = randint(1,18)
    if god == 1:
        print("You got Ah Muzen Cab")
    if god == 2:
        print("You got Anhur")
    if god == 3:
        print("You got Apollo")
    if god == 4:
        print("You got Artemis")
    if god == 5:
        print("You got Cernunnos")
    if god == 6:
        print("You got Chernobog")
    if god == 7:
        print("You got Chiron")
    if god == 8:
        print("You got Cupid")
    if god == 9:
        print("You got Hachiman")
    if god == 10:
        print("You got Hou Yi")
    if god == 11:
        print("You got Izanami")
    if god == 12:
        print("You got Jing Wei")
    if god == 13:
        print("You got Medusa")
    if god == 14:
        print("You got Neith")
    if god == 15:
        print("You got Rama")
    if god == 16:
        print("You got Skadi")
    if god == 17:
        print("You got Ullr")
    if god == 18:
        print("You got Xbalanque")
    print("~//~"'\n')
    def boots():
        if god == 19:
            print("Acron of Yggdrasil")
        if god != 19:
            boots = randint(1,4)
            if boots == 1:
                print("Warrior Tabi")
            if boots == 2:
                print("Ninja Tabi")
            if boots == 3:
                print("Reinforced Greaves")
            if boots == 4:
                print("Talaria Boots")
    boots()
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

def warrior():
    god = randint(1,15)
    if god == 1:
        print("You got Achilles")
    if god == 2:
        print("You got Amaterasu")
    if god == 3:
        print("You got Bellona")
    if god == 4:
        print("You got Chaac")
    if god == 5:
        print("You got Cu Chulainn")
    if god == 6:
        print("You got Erlang Shen")
    if god == 7:
        print("You got Guan Yu")
    if god == 8:
        print("You got Hercules! BOOM BABY!")
    if god == 9:
        print("You got Nike")
    if god == 10:
        print("You got Odin")
    if god == 11:
        print("You got Osiris")
    if god == 12:
        print("You got Ravana")
    if god == 13:
        print("You got Sun Wukong")
    if god == 14:
        print("You got Tyr")
    if god == 15:
        print("Vamana")
    print("~//~"'\n')
    def boots():
        if god == 16:
            print("Acron of Yggdrasil")
        if god != 16:
            boots = randint(1,4)
            if boots == 1:
                print("Warrior Tabi")
            if boots == 2:
                print("Ninja Tabi")
            if boots == 3:
                print("Reinforced Greaves")
            if boots == 4:
                print("Talaria Boots")
    boots()
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

def assassin():
    god = randint(1,18)
    if god == 1:
        print("You got Arachne")
    if god == 2:
        print("You got Awilix")
    if god == 3:
        print("You got Bakasura")
    if god == 4:
        print("You got Bastet")
    if god == 5:
        print("You got Camazotz")
    if god == 6:
        print("You got Da Ji")
    if god == 7:
        print("You got Fenrir")
    if god == 8:
        print("You got Hun Batz")
    if god == 9:
        print("You got Kali")
    if god == 10:
        print("You got Loki")
    if god == 11:
        print("You got Mercury")
    if god == 12:
        print("You got Ne Zha")
    if god == 13:
        print("You got Nemesis")
    if god == 14:
        print("You got Ratatoskr")
    if god == 15:
        print("You got Serqet")
    if god == 16:
        print("You got Susano")
    if god == 17:
        print("You got Thanatos")
    if god == 18:
        print("You got Thor")
    print("~//~" '\n')
    def boots():
        if god == 14:
            print("Acron of Yggdrasil")
        if god != 14:
            boots = randint(1,4)
            if boots == 1:
                print("Warrior Tabi")
            if boots == 2:
                print("Ninja Tabi")
            if boots == 3:
                print("Reinforced Greaves")
            if boots == 4:
                print("Talaria Boots")
    boots()
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

# Physical Random God
def physical():
    god = randint(1,51)
    if god == 1:
        print("You got Achilles")
    if god == 2:
        print("You got Ah Muzen Cab")
    if god == 3:
        print("You got Amaterasu")
    if god == 4:
        print("You got Anhur")
    if god == 5:
        print("You got Apollo")
    if god == 6:
        print("You got Arachne")
    if god == 7:
        print("You got Artemis")
    if god == 8:
        print("You got Awilix")
    if god == 9:
        print("You got Bakasura")
    if god == 10:
        print("You got Bastet")
    if god == 11:
        print("You got Bellona")
    if god == 12:
        print("You got Camazotz")
    if god == 13:
        print("You got Cernunnos")
    if god == 14:
        print("You got Chaac")
    if god == 15:
        print("You got Chernobog")
    if god == 16:
        print("You got Chiron")
    if god == 17:
        print("You got Cu Chulainn")
    if god == 18:
        print("You got Cupid")
    if god == 19:
        print("You got Da Ji")
    if god == 20:
        print("You got Erlang Shen")
    if god == 21:
        print("You got Fenrir")
    if god == 22:
        print("You got Guan Yu")
    if god == 23:
        print("You got Hachiman")
    if god == 24:
        print("You got Hercules")
    if god == 25:
        print("You got Hou Yi")
    if god == 26:
        print("You got Hun Batz")
    if god == 27:
        print("You got Izanami")
    if god == 28:
        print("You got Jing Wei")
    if god == 29:
        print("You got Kali")
    if god == 30:
        print("You got Loki")
    if god == 31:
        print("You got Medusa")
    if god == 32:
        print("You got Mercury")
    if god == 33:
        print("You got Ne Zha")
    if god == 34:
        print("You got Neith")
    if god == 35:
        print("You got Nemesis")
    if god == 36:
        print("You got Nike")
    if god == 37:
        print("You got Odin")
    if god == 38:
        print("You got Osiris")
    if god == 39:
        print("You got Rama")
    if god == 40:
        print("You got Ratatoskr")
    if god == 41:
        print("You got Ravana")
    if god == 42:
        print("You got Serqet")
    if god == 43:
        print("You got Skadi")
    if god == 44:
        print("You got Sun Wukong")
    if god == 45:
        print("You got Susano")
    if god == 46:
        print("You got Thanatos")
    if god == 47:
        print("You got Thor")
    if god == 48:
        print("You got Tyr")
    if god == 49:
        print("You got Ullr")
    if god == 50:
        print("You got Vamana")
    if god == 51:
        print("You got Xbalanque")
    print("~//~" '\n')
    def boots():
        if god == 40:
            print("Acron of Yggdrasil")
        if god != 40:
            boots = randint(1,4)
            if boots == 1:
                print("Warrior Tabi")
            if boots == 2:
                print("Ninja Tabi")
            if boots == 3:
                print("Reinforced Greaves")
            if boots == 4:
                print("Talaria Boots")
    boots()
    items = [None]*5

    def PhysicalBuild():
            item = randint(1, 58)

            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emperor's Armor"
            if item == 5:
                return "The Executioner"
            if item == 6:
                return "Qin's Sais"
            if item == 7:
                return "Titan's Bane"
            if item == 8:
                return "Brawler's Beat Stick"
            if item == 9:
                return "Jotunn's Wrath"
            if item == 10:
                return "The Crusher"
            if item == 11:
                return "Transcendence"
            if item == 12:
                return "Hydra's Lament"
            if item == 13:
                return "Deathbringer"
            if item == 14:
                return "Rage"
            if item == 15:
                return "Malice"
            if item == 16:
                return "Soul Eater"
            if item == 17:
                return "Devourer's Gauntlet"
            if item == 18:
                return "Bloodforge"
            if item == 19:
                return "Winged Blade"
            if item == 20:
                return "Witchblade"
            if item == 21:
                return "Relic Dagger"
            if item == 22:
                return "Toxic Dagger"
            if item == 23:
                return "Frostbound Hammer"
            if item == 24:
                return "Runeforged Hammer"
            if item == 25:
                return "Blackthorn Hammer"
            if item == 26:
                return "Shifter's Shield"
            if item == 27:
                return "Void Shield"
            if item == 28:
                return "Hide of the Nemean Lion"
            if item == 29:
                return "Breastplate of Valor"
            if item == 30:
                return "Spectral Armor"
            if item == 31:
                return "Magi's Cloak"
            if item == 32:
                return "Hide of the Urchin"
            if item == 33:
                return "Spirit Robe"
            if item == 34:
                return "Mantle of Discord"
            if item == 35:
                return "Bulwark of Hope"
            if item == 36:
                return "Pestilence"
            if item == 37:
                return "Heartward Amulet"
            if item == 38:
                return "Talisman of Energy"
            if item == 39:
                return "Runic Shield"
            if item == 40:
                return "Ancile"
            if item == 41:
                return "Odysseus' Bow"
            if item == 42:
                return "Atlanta's Bow"
            if item == 43:
                return "Stone of Gaia"
            if item == 44:
                return "Shield of Regrowth"
            if item == 45:
                return "Gauntlet of Thebes"
            if item == 46:
                return "Wind Demon"
            if item == 47:
                return "Poisoned Star"
            if item == 48:
                return "Stone Cutting Sword"
            if item == 49:
                return "Masamune"
            if item == 50:
                return "Heartseeker"
            if item == 51:
                return "Hastened Katana"
            if item == 52:
                return "Genji's Guard"
            if item == 53:
                return "Oni Hunter's Garb"
            if item == 54:
                return "Shogun's Kusari"
            if item == 55:
                return "Asi"
            if item == 56:
                return "Silverbranch Bow"
            if item == 57:
                return "Gladiator's Shield"
            if item == 58:
                return "Ichaival"


    items[0] = PhysicalBuild()
    items[1] = PhysicalBuild()
    items[2] = PhysicalBuild()
    items[3] = PhysicalBuild()
    items[4] = PhysicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = PhysicalBuild()


    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()

# Magical Random
def magical():
    god = randint(1,45)
    if god == 1:
        print("You got Agni")
    if god == 2:
        print("You got Ah Puch")
    if god == 3:
        print("You got Anubis")
    if god == 4:
        print("You got Ao Kuang")
    if god == 5:
        print("You got Aphrodite")
    if god == 6:
        print("You got Ares")
    if god == 7:
        print("You got Artio")
    if god == 8:
        print("You got Athena")
    if god == 9:
        print("You got Bacchus")
    if god == 10:
        print("You got Baron Samedi")
    if god == 11:
        print("You got Cabrakan")
    if god == 12:
        print("You got Cerberus")
    if god == 13:
        print("You got Chang'e")
    if god == 14:
        print("You got Chronos")
    if god == 15:
        print("You got Discordia")
    if god == 16:
        print("You got Fafnir")
    if god == 17:
        print("You got Freya")
    if god == 18:
        print("You got Ganesha")
    if god == 19:
        print("You got Geb")
    if god == 20:
        print("You got Hades")
    if god == 21:
        print("You got He Bo")
    if god == 22:
        print("You got Hel")
    if god == 23:
        print("You got Isis")
    if god == 24:
        print("You got Janus")
    if god == 25:
        print("You got Khepri")
    if god == 26:
        print("You got Kukulkan")
    if god == 27:
        print("You got Kumbhakarna")
    if god == 28:
        print("You got Kuzenbo")
    if god == 29:
        print("You got Nox")
    if god == 30:
        print("You got Nu Wa")
    if god == 31:
        print("You got Poseidon")
    if god == 32:
        print("You got Ra")
    if god == 33:
        print("You got Raijin")
    if god == 34:
        print("You got Scylla")
    if god == 35:
        print("You got Sobek")
    if god == 36:
        print("You got Sol")
    if god == 37:
        print("You got Sylvanus")
    if god == 38:
        print("You got Terra")
    if god == 39:
        print("You got The Morrigan")
    if god == 40:
        print("You got Thoth")
    if god == 41:
        print("You got Vulcan")
    if god == 42:
        print("You got Xing Tian")
    if god == 43:
        print("You got Zeus")
    if god == 44:
        print("You got Zhong Kui")
    if god == 45:
        print("You got Ymir")
    print("~//~" '\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Shoes of the Magi")
        if boots == 2:
            print("Shoes of Focus")
        if boots == 3:
            print("Reinforced Shoes")
        if boots == 4:
            print("Traveler's Shoes")
    boots()

    items = [None]*5

    def MagicalBuild():
            item = randint(1, 50)
            if item == 1:
                return "Sovereignty"
            if item == 2:
                return "Mystical Mail"
            if item == 3:
                return "Midgardian Mail"
            if item == 4:
                return "Emporer's Armor"
            if item == 5:
                return "Pythagorem's Piece"
            if item == 6:
                return "Bancroft's Talon"
            if item == 7:
                return "Typhon's Fang"
            if item == 8:
                return "Soul Gem"
            if item == 9:
                return "Brestplate of Valor"
            if item == 10:
                return "Spectral Armor"
            if item == 11:
                return "Magi's Cloak"
            if item == 12:
                return "Hide of the Urchin"
            if item == 13:
                return "Spirit Robe"
            if item == 14:
                return "Mantle of Discord"
            if item == 15:
                return "Bulwark of Hope"
            if item == 16:
                return "Pestilence"
            if item == 17:
                return "Heartward Amulet"
            if item == 18:
                return "Talisman of Energy"
            if item == 19:
                return "Demonic Grip"
            if item == 20:
                return "Telekhines Ring"
            if item == 21:
                return "Shaman's Ring"
            if item == 22:
                return "Hastened Ring"
            if item == 23:
                return "Obsidian Shard"
            if item == 24:
                return "Divine Ruin"
            if item == 25:
                return "Spear of the Magus"
            if item == 26:
                return "Spear of Desolation"
            if item == 27:
                return "Gem of Isolation"
            if item == 28:
                return "Warlock's Staff"
            if item == 29:
                return "Etheral Staff"
            if item == 30:
                return "Rod of Asclepius"
            if item == 31:
                return "Book of Thoth"
            if item == 32:
                return "Polynomicon"
            if item == 33:
                return "Soul Reaver"
            if item == 34:
                return "Book of the Dead"
            if item == 35:
                return "Rod of Tahuti"
            if item == 36:
                return "Chronos' Pendant"
            if item == 37:
                return "Celestial Legion Helm"
            if item == 38:
                return "Lotus Crown"
            if item == 39:
                return "Jade Emperor's Crown"
            if item == 40:
                return "Stone of Gaia"
            if item == 41:
                return "Shield of Regrowth"
            if item == 42:
                return "Mail of Renewal"
            if item == 43:
                return "Gauntlet of Thebes"
            if item == 44:
                return "Genji's Guard"
            if item == 45:
                return "Oni Hunter's Garb"
            if item == 46:
                return "Shogun's Kusari"
            if item == 47:
                return "Void Stone"
            if item == 48:
                return "Stone of Fal"
            if item == 49:
                return "Hide of the Nemean Lion"
            if item == 50:
                return "Doom Orb"


    items[0] = MagicalBuild()
    items[1] = MagicalBuild()
    items[2] = MagicalBuild()
    items[3] = MagicalBuild()
    items[4] = MagicalBuild()

    def find_duplicate():
        for x in range(0, 4):
            for y in range(x + 1, 5):
                if items[x] == items[y]:
                    return y
        return -1

    duplicate = 0

    while duplicate != -1:
        duplicate = find_duplicate()

        if duplicate != -1:
            items[duplicate] = MagicalBuild()

    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print(items[4])
    print('\n'"~//~")
    retry()


def retry():
    tryag=["yes","no","y","n"]
    retry=""
    print("Would you like to get another build? Yes / No ? ")
    retry = str(input(">>>")).lower()

    if retry == tryag[0]:
        Start()
    if retry== tryag[2]:
        Start()
    if retry == tryag[1]:
        exit()
    if retry == tryag[3]:
        exit()

Start()
