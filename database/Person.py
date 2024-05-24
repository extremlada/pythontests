from database.observer import Subject, Observer

subject = Subject()
observer = Observer(subject)
class Person:
    def __init__(self):
        self.person_attributes = {}

    def update_person(self, **kwargs):
        subject.notify("the person has been updated")
        for key, value in kwargs.items():
            self.person_attributes[key] = value

    def get_name(self):
        return self.person_attributes.get('Név', None)
