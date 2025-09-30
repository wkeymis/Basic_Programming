# Question

### Ecosystem Simulation

You are asked to simulate a simple ecosystem containing **plants** and **animals**.  

The ecosystem works as follows:
- **Plants** have a `size` and grow by 1 unit every time step.  
- **Animals** have a `name` and `energy`. They can:
  - `eat` a plant, increasing their energy by 2 and reducing the plant’s size by 1.  
  - `move`, which decreases their energy by 1.  
  - `is_alive`, which checks if the animal still has energy (`> 0`).  
- The **Ecosystem** contains a collection of plants and animals. At each simulation step:
  - All plants grow.  
  - All animals move and attempt to eat the first available plant.  
  - Animals with no energy are removed from the ecosystem.  

---

## Your Task

Design three Python classes:

### 1. `Plant`
- Attributes:
  - `size` (default 3).  
- Methods:
  - `grow()`: Increases the plant’s size by 1.  

### 2. `Animal`
- Attributes:
  - `name`  
  - `energy`  
- Methods:
  - `eat(plant)`: Animal eats the plant if its size > 0, increasing energy by 2 and decreasing plant size by 1.  
  - `move()`: Decreases energy by 1.  
  - `is_alive()`: Returns `True` if energy > 0.  

### 3. `Ecosystem`
- Attributes:
  - `plants` (list of `Plant` objects)  
  - `animals` (list of `Animal` objects)  
- Methods:
  - `add_plant(plant)` and `add_animal(animal)`: Add objects to the ecosystem.  
  - `step()`: Executes a simulation step as described above.  
  - `display()`: Prints the current state of the ecosystem (number of plants and animals, energy of animals, size of plants).  

---

## Tasks

1. Implement the three classes described above.  
2. Initialize an ecosystem with:
   - 5 plants of size 3  
   - 2 animals: `"Rabbit"` with energy 5, `"Deer"` with energy 8  
3. Simulate 5 steps of the ecosystem and display the state after each step.  


---
