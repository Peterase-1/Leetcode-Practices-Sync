class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, startTime, endTime):
        for start, end in self.events:
            if startTime < end and endTime > start:
                return False
        
        self.events.append((startTime, endTime))
        return True