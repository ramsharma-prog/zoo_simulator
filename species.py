from base import Animals

# ------- Assign IDs to each animal-----------#
species = {'Elephant': 0, 'Giraffe': 1, 'Monkey': 2}


class Elephant(Animals, object):
    """ Inherited from Animal class & modify check_health fun"""
    def __init__(self):
        self.species = species['Elephant']
        self.can_walk = True
        super(Elephant, self).__init__()

    def check_health(self):
        if self.health < 70.0 and self.can_walk == False:
            self.is_dead = True
        elif self.health < 70.0:
            self.can_walk = False
        elif self.health >= 70.0:
            self.can_walk = True


class Giraffe(Animals, object):
    """ Inherited from Animal class & modify check_health fun"""
    def __init__(self):
        self.species = species['Giraffe']
        super(Giraffe, self).__init__()

    def check_health(self):
        if self.health < 50.0:
            self.is_dead = True


class Monkey(Animals, object):
    """ Inherited from Animal class & modify check_health fun"""
    def __init__(self):
        self.species = species['Monkey']
        super(Monkey, self).__init__()

    def check_health(self):
        if self.health < 30.0:
            self.is_dead = True
