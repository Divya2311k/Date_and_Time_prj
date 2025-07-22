from datetime import datetime

class Event:
    def __init__(self, name: str, date_time: str):
        self.name = name
        self.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

    def time_remaining(self):
        now = datetime.now()
        return self.date_time - now

    def is_upcoming(self):
        return self.time_remaining().total_seconds() > 0

    def __str__(self):
        return f"{self.name} at {self.date_time.strftime('%Y-%m-%d %H:%M')}"
