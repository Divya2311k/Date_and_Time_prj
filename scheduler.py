import json
import os
from event import Event

EVENTS_FILE = "events.json"

class Scheduler:
    def __init__(self):
        self.events = []
        self.load_events()

    def add_event(self, name, date_time):
        event = Event(name, date_time)
        self.events.append(event)
        self.save_events()

    def save_events(self):
        with open(EVENTS_FILE, "w") as f:
            json.dump(
                [{"name": e.name, "date_time": e.date_time.strftime("%Y-%m-%d %H:%M")} for e in self.events],
                f, indent=4
            )

    def load_events(self):
        if not os.path.exists(EVENTS_FILE):
            return
        with open(EVENTS_FILE, "r") as f:
            for item in json.load(f):
                self.events.append(Event(item["name"], item["date_time"]))

    def get_upcoming_events(self):
        return sorted([e for e in self.events if e.is_upcoming()], key=lambda x: x.date_time)
