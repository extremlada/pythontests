from database.Database import Database

db = Database()



def get_person(filter):
    return [name for name in db.get_people_names() if filter(name)]
