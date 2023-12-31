"""
Class of "Project"
Name	Start Date	Priority	Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100

"""


class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def is_complete(self):
        return self.completion == 100

    def __repr__(self):
        return (f"{self.name:<25} start: {self.date:<20} Priority {self.priority:<10}"
                f" Estimate: ${self.cost:<20.2f} Completion: {self.completion:>10}%")


