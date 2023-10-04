# Determining the time when the class is used
import datetime

# A topic that describes what this class is, when it is inserted into the collection
topic = "temp"


class Temperature:
    def __init__(self, value=None, id = None, ubication=None, ) -> None:
        self.value = value
        self.id = id,
        self.ubication = ubication

    def to_JSON(self):
        return {
            "id": self.id,
            "ubication": self.ubication,
            "value": self.value,
            "date": datetime.datetime.now(),
            "topic": topic,
        }
