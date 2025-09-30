class Plant:
    def __init__(self, size=3):
        self.size = size

    def grow(self):
        self.size += 1


class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def eat(self, plant):
        if plant.size > 0:
            plant.size -= 1
            self.energy += 2

    def move(self):
        self.energy -= 1

    def is_alive(self):
        return self.energy > 0


class Ecosystem:
    def __init__(self):
        self.plants = []
        self.animals = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def add_animal(self, animal):
        self.animals.append(animal)

    def step(self):
        for plant in self.plants:
            plant.grow()

        for animal in self.animals:
            animal.move()
            if self.plants:
                animal.eat(self.plants[0])

        self.animals = [a for a in self.animals if a.is_alive()]

    def display(self):
        print("Ecosystem state:")
        print(f"  Number of plants: {len(self.plants)}")
        print(f"  Number of animals: {len(self.animals)}")
        for a in self.animals:
            print(f"    {a.name} (energy={a.energy})")
        for i, p in enumerate(self.plants, start=1):
            print(f"    Plant {i} (size={p.size})")
        print("")


ecosystem = Ecosystem()

for _ in range(5):
    ecosystem.add_plant(Plant(size=3))

ecosystem.add_animal(Animal("Rabbit", 5))
ecosystem.add_animal(Animal("Deer", 8))

for step in range(5):
    print(f"--- Step {step+1} ---")
    ecosystem.step()
    ecosystem.display()
