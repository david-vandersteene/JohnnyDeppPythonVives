from typing import Tuple

from PIL import Image


class Vessel:
    def __init__(self, name: str, masts: int, acceleration: int, img_path: str):
        self.passengers = []
        self.name = name
        self.masts = masts
        self.acceleration = acceleration
        self.img_path = img_path
        self.speed = acceleration * masts

    def ShowImage(self):
        img = Image.open(self.img_path)
        img.show()

    def embark(self, passenger):
        self.passengers.append(passenger)

    def disembark(self, passenger=None):
        if self.passengers.__contains__(passenger):
            self.passengers.remove(passenger)
        else:
            raise Exception("No such passenger on board")

    # windstream [there's wind, headwind or not]
    def sail(self, windstream: Tuple[bool, bool]):
        if not windstream[0]:
            # todo: how to check if passenger on board?
            print(f"${type(self)} is just floating with ${len(self.passengers)} passengers")
        elif windstream[1]:
            print(f"${type(self)} has set sail! Full speed ahead! (${self.speed} km/h)")
        else:
            print(f"${type(self)} has set sail! But the wind is not in our favor. (${self.speed} km/h) ")


class Boat(Vessel):
    def __init__(self, name: str, acceleration: int, img_path: str):
        if 1 <= acceleration <= 25:
            super(Boat, self).__init__(name, 1, acceleration, img_path)
        else:
            raise Exception("Acceleration is too high for a boat!")


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

    def add_crewmember(self, crewmember):
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
