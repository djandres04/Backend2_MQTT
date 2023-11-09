# Determining the time when the class is used
import datetime

# A topic that describes what this class is, when it is inserted into the collection
topic = "buzzer"


class alarm:
    def __init__(self, id, ubication, waiting, person) -> None:
        self.id = id
        self.ubication = ubication
        self.waiting = waiting
        self.person = person

    def to_JSON(self):
        return {
            "id": self.id,
            "ubication": self.ubication,
            "waiting": self.waiting,
            "date": datetime.datetime.now(),
            "topic": topic,
            "person": self.person
        }
