# Question

### Project Management System

You are asked to manage project data stored in a text file.  
Each project section starts with a header `[Project Name]` 


---

## Your Task

Design two Python classes:

### 1. `ProjectManager`
This class should:
- Read the file and store project information.  
- Provide the following methods:
  - `total_budget()`: Returns the sum of all project budgets.  
  - `largest_team()`: Returns the project with the largest team and the number of team members.  
  - `leader_of(project_name)`: Returns the leader of the specified project.  

### 2. `ProjectReporter`
This class should:
- Be initialized with a `ProjectManager` object.  
- Provide a method `generate_report()` that:
  - Prints the project with the largest team and its size.  
  - Prints the leader of each project.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the provided `projects.txt` file.  
3. Print:
   - The total budget of all projects  
   - The project with the largest team  
   - Leaders of all projects  

---
