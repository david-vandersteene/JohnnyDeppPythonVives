from typing import Tuple

from PIL import Image

from imgrender import render

from random import randint


class Vessel:
    def __init__(self, name: str, masts: int, acceleration: int, img_path: str):
        self.passengers = []
        self.name = name
        self.masts = masts
        self.acceleration = acceleration
        self.img_path = img_path
        self.speed = 0

    def ShowImage(self):
        render(self.img_path, scale=(40,60))

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
            self.speed = 0
            print(f"{self.name} is just floating with {len(self.passengers)} passengers")
        elif windstream[1]:
            self.speed = self.acceleration * self.masts
            print(f"{self.name} has set sail! Full speed ahead! ({self.speed} km/h)")
        else:
            self.speed = (self.acceleration * self.masts) / 2
            print(f"{self.name} has set sail! But the wind is not in our favor. ({self.speed / 2} km/h) ")


class Boat(Vessel):
    def __init__(self, name: str, acceleration: int, img_path: str):
        if 1 <= acceleration <= 25:
            super(Boat, self).__init__(name, 1, acceleration, img_path)
            self.passengers = []
            self.speed = 0
        else:
            raise Exception("Acceleration is too high for a boat!")

    def embark(self, passenger):
        if not self.passengers.__contains__(passenger):
            self.passengers.append(passenger)
        else:
            raise Exception("Passenger is already on the ship")

    def disembark(self, passenger=None):
        if self.passengers.__contains__(passenger):
            self.passengers.remove(passenger)
        else:
            print("Passenger is not onboard")

    def sail(self, windstream: Tuple[bool, bool]):
        if len(self.passengers) > 0:
            super(Boat, self).sail(windstream)
        else:
            self.speed = 0
            print(f"{self.name} is just floating with 0 passengers.")

    def __str__(self):
        res = f"{self.name} has {len(self.passengers)} passenger(s)"
        if self.speed:
            return res + f" and is sailing at {self.speed} km/h"
        else:
            return res + f" and is not sailing."


class Ship(Vessel):
    def __init__(self, name: str, masts: int, acceleration: int, img_path: str):
        if masts < 2:
            masts = 2
        if 0 < acceleration:
            super(Ship, self).__init__(name, masts, acceleration, img_path)
            self.captain = None
        else:
            raise Exception("Speed is too low")

    def embark(self, passenger):
        if type(passenger) == Captain:
            if not self.captain:  # if no captain
                self.captain = passenger
                self.passengers.append(passenger)

            elif len(self.captain.crew) < len(passenger.crew):  # if new captain has bigger crew
                self.crew_transfer(self.captain, passenger)
                self.captain = passenger
                self.passengers.append(passenger)

            elif len(self.captain.crew) == len(passenger.crew):  # both crews same size
                if randint(0, 1):
                    self.captain = passenger
                    self.passengers.append(passenger)

        elif type(passenger) == Pirate:
            if self.captain:
                self.captain.add_crewmember(passenger)
                self.passengers.append(passenger)
            else:
                print("A crew without a captain is no crew!")

        else:
            print("Passenger is no pirate nor captain!!")

    def crew_transfer(self, old_captain, new_captain):
        for mate in old_captain.crew:
            new_captain.add_crewmember(mate)
            old_captain.remove_crew_member(mate)

    def disembark(self, passenger=None):
        if type(passenger) == Pirate:
            if self.captain.crew.__contains__(passenger):
                self.captain.remove_crew_member(passenger)
        if self.passengers.__contains__(passenger):
            self.passengers.remove(passenger)

    def sail(self, windstream: Tuple[bool, bool]):
        super(Ship, self).sail(windstream)

    def __str__(self):
        if self.speed:
            res = f"{self.name} is just floating with"
        else:
            res = f"{self.name} is sailing with"
        if self.captain:
            return res + f" captain {self.captain.name} as it's captain! (crew: {len(self.captain.crew)} members). Speed = {self.speed} km/h"
        else:
            return res + f" no captian. Speed = {self.speed} km/h"


class SilentMary(Ship):
    def __init__(self, img_path="../img/no_image.jpg"):
        super(SilentMary, self).__init__("Silent Mary", 2, 40, img_path)
        


class BlackPearl(Ship):
    def __init__(self, img_path="../img/no_image.jpg"):
        super(BlackPearl, self).__init__("Black Pearl", 2, 45, img_path)


class FishingBoat(Boat):
    def __init__(self, img_path="../img/no_image.jpg"):
        super(FishingBoat, self).__init__("Fishing boat", 20, img_path)


class RescueBoat(Boat):
    def __init__(self, img_path="../img/no_image.jpg"):
        super(RescueBoat, self).__init__("Rescue boat", 20, img_path)


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
        else:
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
        return self.name + " is a " + type(self).__name__


# main function:
if __name__ == '__main__':
    jackSparrow = Captain(name="Jack Sparrow",
                          quote="This is the day you will always remember as the day you almost caught Captain Jack Sparrow!")
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

    silentMary = SilentMary(img_path="../img/silentmary.jpg")
    blackPearl = BlackPearl(img_path="../img/blackpearl.jpg")
    fishingBoat = FishingBoat(img_path="../img/fishingboat.jpg")
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
    # blackPearl.ShowImage()
    # fishingBoat.ShowImage()
    # rescueBoat.ShowImage()
