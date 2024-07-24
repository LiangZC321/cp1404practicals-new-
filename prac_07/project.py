from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name} - Start Date: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, Cost: ${self.cost_estimate}, Completion: {self.completion_percentage}%"

    def update_completion(self, new_completion):
        if new_completion:
            self.completion_percentage = int(new_completion)

    def update_priority(self, new_priority):
        if new_priority:
            self.priority = int(new_priority)
