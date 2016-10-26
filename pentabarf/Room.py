
class Room:

    name = None

    event_objects = []

    def __init__(self, name=None):
        self.name = name

    def add_event(self, event):
        self.event_objects.append(event)
