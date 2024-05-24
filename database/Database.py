from database.Person import Person

class Database():
    def __init__(self):
        self.data = []

    def add_person(self, person: Person.update_person):
        self.data.append(person)

    def get_people_names(self):
        return [person.get_name() for person in self.data if person.get_name() is not None]


    def update_people_names(self, new_contents):
        self.data.clear()  # Clear existing data
        for name in new_contents:
            self.add_person(name)
