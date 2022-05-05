import datetime
import enum
from datetime import datetime


class LogEventTypes(enum.Enum):
    CRE = 0
    INF = 1
    ERR = 2


class Logger:

    def __init__(self, filename: str):
        self.filename = filename

    def write_event(self, event_type: LogEventTypes, date: datetime, comment: str):
        try:
            with open(self.filename, 'a') as f:
                f.write(f'{event_type.name} --- {date.strftime("%d/%m/%y, %H:%M:%S")} --- {comment}\n')
        except IOError:
            print("LOG FILE NOT FOUND")
