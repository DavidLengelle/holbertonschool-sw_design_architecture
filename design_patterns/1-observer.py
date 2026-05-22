#!/usr/bin/env python3
"""Observer pattern: notify subscribers filtered by topic."""


class NewsSubject:
    """Publish events to observers without knowing their type."""

    def __init__(self):
        """Initialize the subject with an empty observer registry."""
        self._observers = {}

    def subscribe(self, observer, topics=None):
        """Register an observer for given topics (None means all)."""
        self._observers[observer] = topics

    def unsubscribe(self, observer):
        """Remove an observer from the registry."""
        self._observers.pop(observer, None)

    def notify(self, topic, data):
        """Send an event to every observer that wants this topic."""
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that writes events to a log."""

    def update(self, topic, data):
        """Print the received event as a log line."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends events by email."""

    def update(self, topic, data):
        """Print the received event as an email line."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends events by SMS."""

    def update(self, topic, data):
        """Print the received event as an SMS line."""
        print(f"sms:{topic}={data}")


def main():
    """Wire observers to the subject and emit a few events."""
    subject = NewsSubject()
    subject.subscribe(LogObserver(), topics={"sports", "breaking"})
    subject.subscribe(EmailObserver())
    subject.subscribe(SmsObserver(), topics={"breaking"})
    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
