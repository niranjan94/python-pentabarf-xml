from xml.etree.ElementTree import Element, SubElement, Comment, tostring


class Conference:

    title = None
    start = None
    end = None
    days = None
    day_change = None
    timeslot_duration = None
    venue = None
    city = None

    day_objects = []

    def __init__(self,
                 title=None,
                 start=None,
                 end=None,
                 days=None,
                 day_change=None,
                 city=None,
                 timeslot_duration=None,
                 venue=None):

        self.title = title
        self.start = start
        self.end = end
        self.days = days
        self.day_change = day_change
        self.timeslot_duration = timeslot_duration
        self.venue = venue
        self.city = city
        self.day_objects = []

    def add_day(self, day):
        self.day_objects.append(day)

    def generate(self, comment=None):
        schedule = Element('schedule')
        conference = SubElement(schedule, 'conference')
        title_element = SubElement(conference, 'title')
        title_element.text = self.title
        start_element = SubElement(conference, 'start')
        start_element.text = self.start.strftime('%Y-%m-%d')
        end_element = SubElement(conference, 'end')
        end_element.text = self.end.strftime('%Y-%m-%d')
        venue_element = SubElement(conference, 'venue')
        venue_element.text = self.venue
        days_element = SubElement(conference, 'days')
        days_element.text = str(self.days)
        day_change_element = SubElement(conference, 'day_change')
        day_change_element.text = self.day_change
        timeslot_duration_element = SubElement(conference, 'timeslot_duration')
        timeslot_duration_element.text = self.timeslot_duration
        city_element = SubElement(conference, 'city')
        city_element.text = self.city

        index = 1
        for day in self.day_objects:
            day_element = SubElement(schedule, 'day', {
                'date': day.date.strftime('%Y-%m-%d'),
                'index': str(index)
            })
            index += 1
            for room in day.room_objects:
                room_element = SubElement(day_element, 'room', {
                    'name': room.name
                })

                for event in room.event_objects:
                    event_element = SubElement(room_element, 'event', {
                        'id': str(event.id)
                    })
                    date_element = SubElement(event_element, 'date')
                    date_element.text = event.date.isoformat()
                    start_element = SubElement(event_element, 'start')
                    start_element.text = event.start
                    duration_element = SubElement(event_element, 'duration')
                    duration_element.text = event.duration
                    event_room_element = SubElement(event_element, 'duration')
                    event_room_element.text = room.name
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
                        person_element = SubElement(persons_element, 'person', {
                            'id': str(person.id)
                        })
                        person_element.text = person.name

        if comment:
            comment = Comment(comment)
            schedule.append(comment)
        return tostring(schedule)
