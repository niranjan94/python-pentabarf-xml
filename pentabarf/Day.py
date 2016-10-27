
class Day:
    date = None
    index = None

    room_objects = []

    def __init__(self, date=None, index=None):
        self.date = date
        self.index = index
        self.room_objects = []

    def add_room(self, room):
        self.room_objects.append(room)
