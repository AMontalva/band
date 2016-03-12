class Band(object):
    def __init__(self):
        self.members = {}
    def hire(self, Musician):
        self.members[Musician] = Musician
    def fire(self, Musician):
        del self.members[Musician]
    def print_members(self):
        print(self.members)
    def play_music(self):
        try:
            d = self.members[drummer] 
            d.count_to_four()
            for i in self.members:
                i.solo(4)
            d.spontaneously_combust()
        except KeyError:
            print("You need a drummer")
        
class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bam", "Boom", "Crash"])
    def count_to_four(self):
        for i in range(1, 5):
            print(i)
    def spontaneously_combust(self):
        print("FIRE!")

bassist = Bassist()
guitarist = Guitarist()
drummer = Drummer()

band = Band()
band.hire(bassist)
band.hire(guitarist)
band.hire(drummer)
band.print_members()
band.play_music()
band.fire(bassist)
band.play_music()