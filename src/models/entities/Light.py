# Determining the time when the class is used
import datetime

# A topic that describes what this class is, when it is inserted into the collection
topic = "light"


class light:
    def __init__(self, id, ubication=None, status=None, person=None) -> None:
        self.id = id,
        self.ubication = ubication
        self.status = status
        self.person = person

    def to_JSON(self):
        return {
            "id": self.id,
            "ubication": self.ubication,
            "status": self.status,
            "date": datetime.datetime.now(),
            "topic": topic,
            "person": self.person
        }
