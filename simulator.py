import tkinter as tk
from math import floor
from random import uniform
from species import Monkey, Giraffe, Elephant, species

window = tk.Tk()
window.config(background="gray")

# --------------iteration time in milliseconds-----------------#


ITERATION_TIME = 3000


# ---------------------formatted time-----------------------------#
def formatted_time(hours):
    days = floor(hours // 24)
    hours = hours % 24
    return f'Day {days} ({hours}:00)'


class Simulator:
    """ This class responsible for combining all the files &
    have feed, time/iteration, layout functions"""

    def __init__(self, container):
        self.box = container
        self.zoo = []
        # ------ Create 5 animals of all the species------------£
        for num in range(5):
            self.zoo.append(Monkey())
            self.zoo.append(Giraffe())
            self.zoo.append((Elephant()))

        # NOTE:-->  StringVar---I got some help with StringVar()--------#

        self.time = 0  # To be used in time_rolling function
        self.timer_text = tk.StringVar()
        self.display_layout()

        # -------------- Time RECURSION-------------------------------#
        self.started = True
        self.time_rolling()

    def feed_animals(self):
        """ feed animals generates 3 random values for 3 different species"""
        # Generate 3 random values
        food = [uniform(10, 25) for _ in range(3)]
        # -------------Feed different % of food quantity to animals----------#
        for animal in self.zoo:
            animal.feed_animals(food[animal.species])
            self.health_colors(animal)

    def time_rolling(self, triggered=False):
        """ TIME ROLLS BY 1 AFTER EACH ITERATION OF GIVEN ITERATION TIME """
        self.time += 1
        self.timer_text.set(formatted_time(self.time))

        for animal in self.zoo:
            animal.time()
            self.health_colors(animal)

        # ----Checking if the skip time button was manually triggered----#
        if not triggered:
            self.box.after(ITERATION_TIME, self.time_rolling)

    def health_colors(self, animal):
        """ health_colors fun() info, red: animal is dead, pink: elephant can't walk,
        yellow: unhealthy, green: healthy """

        if animal.is_dead:
            animal.label.config(bg='tomato')
            status_string = "I'm dead"

        elif animal.health < 70:
            animal.label.config(bg='yellow')
            status_string = 'Feed me'

        elif animal.species == species['Elephant'] and animal.can_walk == False:
            animal.label.config(bg='lightpink')
            status_string = "Can't walk"

        else:
            animal.label.config(bg='light green')
            status_string = "I'm good"

        animal.stringvar.set(f'{animal}\n{animal.get_health()}%\n\n{status_string}')

    def display_layout(self):
        # create all animals list
        animals_list = species.items()

        # Animal name headers
        for name, id in animals_list:
            tk.Label(self.box, font='Courier 24 bold', text=name, fg="black").grid(row=0, column=id, padx=100)

        # Create labels for each animal.
        row_number = 0
        for animal in self.zoo:
            animal.stringvar = tk.StringVar()

            # Create labels for each section
            animal.label = tk.Label(self.box, textvariable=animal.stringvar, fg="tomato")
            animal.label.grid(row=(row_number // 3) + 1, column=animal.species, padx=100, pady=20)
            self.health_colors(animal)
            row_number += 1

        # Button to feed animals
        tk.Button(self.box, text="Feed animals \n click me",
                  command=self.feed_animals, pady=20, padx=15, fg="green").grid(row=7, column=0)

        # # Button to skip time
        tk.Button(self.box, text='Skip time +1 hour\nclick me',
                  command=lambda: self.time_rolling(True), pady=20, padx=11, fg="red").grid(row=7, column=2)

        # Timer & Date/time in hours label

        tk.Label(text=f"Timer\ndefault time is {ITERATION_TIME / 1000} seconds", font=("Courier", 10)).grid(row=7,
                                                                                                            column=1)
        tk.Label(self.box, textvariable=self.timer_text,
                 font=("Courier", 25)).grid(row=9, column=1, padx=200, pady=10)


# ----------RUN SIMULATOR------------#

if __name__ == '__main__':
    window.resizable(False, False)
    window.title('Zoo Simulator')
    Simulator(window)
    window.mainloop()
