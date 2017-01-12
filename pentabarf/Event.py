
class Event:

    id = None
    date = None
    start = None
    duration = None
    track = None
    abstract = None
    level = None
    title = None
    type = None
    description = None
    conf_url = None
    full_conf_url = None
    released = None
    video_url = None
    slides_url = None
    audio_url = None

    person_objects = []

    def __init__(self, id=None, date=None, start=None, duration=None, track=None, abstract=None, video_url=None,
                 slides_url=None, audio_url=None, level=None,
                 title=None, type=None, description=None, conf_url=None, full_conf_url=None, released=None):
        self.id = id
        self.date = date
        self.start = start
        self.duration = duration
        self.track = track
        self.abstract = abstract
        self.level = level
        self.title = title
        self.type = type
        self.description = description
        self.conf_url = conf_url
        self.full_conf_url = full_conf_url
        self.released = released
        self.video_url = video_url
        self.slides_url = slides_url
        self.audio_url = audio_url
        self.person_objects = []

    def add_person(self, person):
        self.person_objects.append(person)
