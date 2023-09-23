import datetime
topic = "light"

class Light():
    def __init__(self, id, ubication=None, status=None, person=None) -> None:
        self.id = id,
        self.ubication = ubication
        self.status = status
        self.person = person

    def to_JSON_person(self):
        return {
            "id": self.id,
            "ubication": self.ubication,
            "status": self.status,
            "date": datetime.datetime.now(),
            "topic": topic,
            "person": self.person
        }
