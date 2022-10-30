class Vessel :
    pass


class Boat(Vessel):
    pass


class Ship(Vessel):
    pass


class SilentMary(Ship):
    pass


class BlackPearl(Ship):
    pass


class FishingBoat(Boat):
    pass


class RescueBoat(Boat):
    pass


class Pirate:
    def __init__(self, name: str, quote: str = "Ahoy!"):
        self.name = name
        self.quote = quote

    def __repr__(self):
        return self.name + ": " + self.quote


class Captain(Pirate):
    def __init__(self, name: str, quote: str):
        super().__init__(name, quote)
        self.crew = []

    def add_crew_member(self, crewmember):
        if self.crew.__contains__(crewmember):
            raise Exception("Crew does not contain given member in add_crew_member")
        else :
            self.crew.append(crewmember)

    def remove_crew_member(self, crewmember):
        if self.crew.__contains__(crewmember):
            self.crew.remove(crewmember)
        else:
            raise Exception("Crew does not contain given member in remove_crew_member")


class Civilian:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name + "is a" + str(type(self))


# main function:
if __name__ == '__main__':
    jackSparrow = Captain(name="Jack Sparrow", quote="This is the day you will always remember as the day you almost caught Captain Jack Sparrow!")
    barbossa = Captain(name="Barbossa", quote="You Best Start Believin' In Ghost Stories... You're in one!")
    salazar = Captain(name="Salazar", quote="My very dead men, the sea is ours! It's time to hunt a pirate!")

    print(jackSparrow)
    print(barbossa)
    print(salazar)
    print()

    gibbs = Pirate("Joshamee Gibs")
    will = Pirate("Will Turner")
    elizabeth = Pirate("Elizabeth Swann")

    print(gibbs)
    print(will)
    print(elizabeth)
    print()

    bootstrap = Pirate("Bootstrap Bill Turner")
    pintel = Pirate("Pintel")
    ragetti = Pirate("Ragetti")

    print(bootstrap)
    print(pintel)
    print(ragetti)
    print()

    silentMary = SilentMary(img_path="img/silentmary.jpg")
    blackPearl = BlackPearl(img_path="img/blackpearl.jpg")
    fishingBoat = FishingBoat(img_path="img/fishingboat.jpg")
    rescueBoat = RescueBoat()

    print(silentMary)
    print(blackPearl)
    print(fishingBoat)
    print(rescueBoat)
    print()

    silentMary.embark(salazar)
    print(silentMary)
    silentMary.sail((True, True))

    blackPearl.embark(jackSparrow)
    jackSparrow.add_crewmember(gibbs)
    barbossa.add_crewmember(bootstrap)
    barbossa.add_crewmember(pintel)
    blackPearl.embark(barbossa)

    print(blackPearl)
    print(rescueBoat)
    print(fishingBoat)
    print()

    blackPearl.sail((True, True))
    blackPearl.disembark()
    blackPearl.sail((True, True))
    print()

    rescueBoat.embark(will)
    rescueBoat.embark(elizabeth)
    print(rescueBoat)
    rescueBoat.sail((True, True))
    print(rescueBoat)
    rescueBoat.disembark(elizabeth)
    print(rescueBoat)
    rescueBoat.disembark(ragetti)
    rescueBoat.disembark(will)
    print(rescueBoat)
    print()

    amberHeard = Civilian("Amber Heard")
    print(amberHeard)
    blackPearl.embark(amberHeard)
    fishingBoat.embark(amberHeard)
    print(fishingBoat)

    silentMary.ShowImage()
    #blackPearl.ShowImage()
    #fishingBoat.ShowImage()
    #rescueBoat.ShowImage()
