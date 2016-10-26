from xml.etree.ElementTree import Element, SubElement, Comment, tostring


class Conference:

    title = None
    start = None
    end = None
    days = None
    day_change = None
    timeslot_duration = None

    day_objects = []

    def __init__(self, title=None, start=None, end=None, days=None, day_change=None, timeslot_duration=None):
        self.title = title
        self.start = start
        self.end = end
        self.days = days
        self.day_change = day_change
        self.timeslot_duration = timeslot_duration

    def add_day(self, day):
        self.day_objects.append(day)

    def generate(self, comment=None):
        schedule = Element('schedule')
        SubElement(schedule, 'conference')
        index = 1
        for day in self.day_objects:
            day_element = SubElement(schedule, 'day')
            day_element.set('date', day_element.date.strftime('%Y-%m-%d'))
            day_element.set('index', index)
            index += 1
            for room in day.room_objects:
                room_element = SubElement(day_element, 'room')
                room_element.set('name', room.name)

                for event in room_element.event_objects:
                    event_element = SubElement(room_element, 'event')
                    event_element.set('id', event.id)
                    date_element = SubElement(event_element, 'date')
                    date_element.text = event.date.isoformat()
                    start_element = SubElement(event_element, 'start')
                    start_element.text = event.start
                    duration_element = SubElement(event_element, 'duration')
                    duration_element.text = event.duration
                    room_element = SubElement(event_element, 'duration')
                    room_element.text = room.name
                    track_element = SubElement(event_element, 'track')
                    track_element.text = event.track
                    abstract_element = SubElement(event_element, 'abstract')
                    abstract_element.text = event.abstract
                    title_element = SubElement(event_element, 'title')
                    title_element.text = event.title
                    description_element = SubElement(event_element, 'description')
                    description_element.text = event.description
                    type_element = SubElement(event_element, 'type')
                    type_element.text = event.type
                    conf_url_element = SubElement(event_element, 'conf_url')
                    conf_url_element.text = event.conf_url
                    full_conf_url_element = SubElement(event_element, 'full_conf_url')
                    full_conf_url_element.text = event.full_conf_url
                    released_element = SubElement(event_element, 'released')
                    released_element.text = event.released
                    persons_element = SubElement(event_element, 'persons')

                    for person in event.person_objects:
                        person_element = SubElement(persons_element, 'person')
                        room_element.set('id', person.id)
                        person_element.text = person.name

        if comment:
            comment = Comment(comment)
            schedule.append(comment)
        return tostring(schedule)
