import defusedxml.ElementTree as ET
from pentabarf.Conference import Conference
from datetime import datetime

from pentabarf.Day import Day
from pentabarf.Event import Event
from pentabarf.Person import Person
from pentabarf.Room import Room


def get_text(sub_element, name):
    sub_element = sub_element.find(name)
    if sub_element is not None:
        return sub_element.text
    else:
        return None


class PentabarfParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(string):
        root = ET.fromstring(string)

        conference_element = root.find('conference')

        conference = Conference(
            title=conference_element.find('title').text,
            start=datetime.strptime(conference_element.find('start').text, '%Y-%m-%d'),
            end=datetime.strptime(conference_element.find('end').text, '%Y-%m-%d'),
            days=int(conference_element.find('days').text),
            day_change=conference_element.find('day_change').text,
            city=conference_element.find('city').text,
            timeslot_duration=conference_element.find('timeslot_duration').text,
            venue=conference_element.find('venue').text,
        )

        for day_element in root.findall('day'):
            day = Day(
                date=datetime.strptime(day_element.get('date'), '%Y-%m-%d'),
                index=int(day_element.get('index'))
            )

            for room_element in day_element.findall('room'):
                room = Room(name=room_element.get('name'))

                for event_element in room_element.findall('event'):
                    event = Event(
                        id=int(event_element.get('id')),
                        date=day.date,
                        start=get_text(event_element, 'start'),
                        duration=get_text(event_element, 'duration'),
                        track=get_text(event_element, 'track'),
                        abstract=get_text(event_element, 'abstract'),
                        title=get_text(event_element, 'title'),
                        type=get_text(event_element, 'type'),
                        description=get_text(event_element, 'description'),
                        conf_url=get_text(event_element, 'conf_url'),
                        full_conf_url=get_text(event_element, 'conf_url'),
                        level=get_text(event_element, 'level')
                    )

                    persons_element = event_element.find('persons')
                    for person_element in persons_element.findall('person'):
                        person = Person(
                            id=int(person_element.get('id')),
                            name=person_element.text,
                        )
                        event.add_person(person)

                    links_element = event_element.find('links')
                    if links_element:
                        for link_element in links_element.findall('link'):
                            link_url = link_element.get('href')
                            if not event.video_url and ('mp4' in link_url
                                                        or 'webm' in link_url
                                                        or 'youtube' in link_url
                                                        or 'avi' in link_url):
                                event.video_url = link_url
                            if not event.audio_url and ('mp3' in link_url or 'wav' in link_url or 'soundcloud' in link_url):
                                event.audio_url = link_url
                            if not event.slides_url and ('ppt' in link_url or 'pptx' in link_url or 'slide' in link_url):
                                event.slides_url = link_url

                    room.add_event(event)
                day.add_room(room)
            conference.add_day(day)
        return conference
