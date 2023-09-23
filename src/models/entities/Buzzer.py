import datetime
topic = "buzzer"
class Buzzer():
    def __init__(self,id,ubication,waiting,person) -> None:
        self.id = id
        self.ubication = ubication
        self.waiting = waiting
        self.person = person

    def to_JSON_person(self):
        return{
            "id":self.id,
            "ubication":self.ubication,
            "waiting":self.waiting,
            "date":datetime.datetime.now(),
            "topic": topic,
            "person":self.person
        }