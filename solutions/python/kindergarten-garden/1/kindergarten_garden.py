plant_map = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}


class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.data = {}

        students = sorted(students)

        for student in students:
            self.data[student] = []

        for part in diagram.split("\n"):
            for i in range(0, len(part)):
                self.data[students[i // 2]].append(plant_map[part[i]])

        print(self.data)

    def plants(self, student):
        return self.data[student]
