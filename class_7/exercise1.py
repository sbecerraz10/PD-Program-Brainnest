from dataclasses import dataclass

@dataclass
class Student:
    name: str
    id: int
    grades:list[float]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

alice = Student("Alice", 12345, [3.5, 4.0, 3.7])
print(f"{alice.name} average grade is: {alice.average_grade()}")
