from device import DeviceState
from queue import PriorityQueue


class Controller(object):
    def __init__(self):
        self.device_state = DeviceState()
        self.event_queue = PriorityQueue()
        self.alarms = []
        self.modules = {}
        self.event_listeners = {}

    def subscribe(self, event_type, handler, event_filter=None):
        if event_type not in self.event_listeners:
            self.event_listeners[event_type] = []
        self.event_listeners[event_type].apppend(handler)

    def broadcast(self, event):
        # Get the set of listeners for the given event type
        listeners = self.event_listeners[event.get_type()]
        for listener in listeners:
            # TODO: Send event to each subscribed listener
            pass

    def register_alarm(self, alarm, handler):
        pass

    """ Add a Simulator Module to the Controller """
    def add_module(self, module):
        pass

    def run(self):
        while True:
            if self.event_queue.empty():
                # TODO: Read in events from the trace file
                pass
            else:
                event = self.event_queue.get(block=False)
                self.broadcast(event=event)
