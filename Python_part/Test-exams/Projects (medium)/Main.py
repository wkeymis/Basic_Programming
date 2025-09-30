class ProjectManager:
    def __init__(self, filename):
        self.projects = {}
        current_projects = None
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current_projects = line[1:-1]
                    self.projects[current_projects] = {
                        "leader": None,
                        "budget": 0,
                        "team": []
                    }

                elif line.startswith("Leader:") and current_projects:
                    leader = line.split(":",1)[1].strip()
                    self.projects[current_projects]["leader"] = leader
                elif line.startswith("Budget") and current_projects:
                    budget = int(line.split(":", 1)[1].strip())
                    self.projects[current_projects]["budget"] = budget
                elif line.startswith("-") and current_projects:
                    member = line[1:].strip()
                    self.projects[current_projects]["team"].append(member)

    def total_budget(self):
        total = 0
        for project in self.projects.values():
            total += project["budget"]
        return total

    def largest_team(self):
        largest_project = None
        largest_size = -1
        for name, project in self.projects.items():
            size = len(project["team"])
            if size > largest_size:
                largest_size = size
                largest_project = name
        return largest_project, largest_size

    def leader_of(self, project_name):
        if project_name in self.projects:
            return self.projects[project_name]["leader"]
        return None

class ProjectReporter:
    def __init__(self, manager):
        self.manager = manager

    def generate_report(self):
        largest_name, largest_size = self.manager.largest_team()
        print(f"\nProject with the largest team: {largest_name}({largest_size} members)")
        for name, data in self.manager.projects.items():
            print(f"{name}: {data["leader"]}")


if __name__ == "__main__":
    manager = ProjectManager("projects.txt")
    reporter = ProjectReporter(manager)
    reporter.generate_report()

