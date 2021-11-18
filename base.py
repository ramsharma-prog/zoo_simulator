from random import uniform


class Animals:
    """ Parents class for all animals """

    def __init__(self):
        self.health = 100
        self.is_dead = False
        self.name = type(self).__name__

    def time(self):
        """ time fun is called every iteration, reduces health, checks health & if animals is dead, returns None """
        if self.is_dead:
            return
        # Get random value to reduce the health of each animal
        self.health -= uniform(0, 20)
        # Calling check_health fun each iteration to check health of each animal.
        self.check_health()

    def feed_animals(self, value):
        """ feed_animal fun is called to feed alive animals when feed animals button triggered """

        if self.is_dead:
            return
        self.health += value
        # -------Cap health to max 100:00%---------#
        if self.health > 100.0:
            self.health = 100.0

    def check_health(self):
        """ check_health fun is to check health conditions of all animals, place & update inside species tab """
        pass

    def get_health(self):
        """ get_health fun returns health in floating value upto 2 decimals. """
        return f'{self.health:.2f}'

    def __str__(self):
        """ fun prints the name of each animal"""
        return self.name
