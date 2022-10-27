import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Jon",
          "Kanye West",
          "Samuel L. Jackson"]

time = ["lunch",
        "dinner",
        "supper",
        "breakfast"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)
random_time = random.choice(time)

print(f"How about you go to {random_bar} with {random_person} and/or {random_person2} for {random_time}")
