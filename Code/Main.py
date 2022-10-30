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


