import abc
from abc import abstractmethod


class SimModule(metaclass=abc.ABCMeta):
    def __init__(self, name, module_type, simulator):
        self.name = name
        self.module_type = module_type
        self.simulator = simulator

    def get_name(self):
        return self.get_name()

    def get_type(self):
        return self.module_type

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def finish(self):
        pass


class TraceReader(metaclass=abc.ABCMeta):
    def __init__(self, filename):
        self.trace_filename = filename

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def finish(self):
        pass

    @abstractmethod
    def peek_event(self):
        pass

    @abstractmethod
    def get_event(self):
        pass

    @abstractmethod
    def get_events(self, count):
        pass

    @abstractmethod
    def end_of_trace(self):
        pass


class SimulatorBase(metaclass=abc.ABCMeta):
    @abstractmethod
    def build(self, config):
        pass

    @abstractmethod
    def register(self, sim_module, override=False):
        pass

    @abstractmethod
    def get_module_for_type(self, module_type):
        pass

    @abstractmethod
    def has_module_instance(self, name):
        pass

    @abstractmethod
    def get_module_instance(self, name):
        pass

    @abstractmethod
    def run(self, trace_file):
        pass

    @abstractmethod
    def subscribe(self, event_type, callback, event_filter=None):
        pass

    @abstractmethod
    def broadcast(self, event):
        pass

    @abstractmethod
    def register_alarm(self, alarm, callback):
        pass
