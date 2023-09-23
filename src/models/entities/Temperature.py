import datetime
topic = "temp"

class Temperature():
    def __init__(self, id, ubication=None, value=None, person=None) -> None:
        self.id = id,
        self.ubication = ubication
        self.value = value
        self.person = person

    def to_JSON_person(self):
        return {
            "id": self.id,
            "ubication": self.ubication,
            "value": self.value,
            "date": datetime.datetime.now(),
            "topic": topic,
            "person": self.person
        }