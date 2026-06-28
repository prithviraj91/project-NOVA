class EventBus:

    def __init__(self):
        self.listeners = {}

    def on(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def emit(self, event, data=None):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(data)


events = EventBus()