import abc
from abc import abstractmethod


class SimModule(metaclass=abc.ABCMeta):
    @abstractmethod
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


class SimulatorBase(metaclass=abc.ABCMeta):
    @abstractmethod
    def build(self, config):
        pass

    @abstractmethod
    def register(self, module_type, sim_module, override=False):
        pass

    @abstractmethod
    def get_module_for_type(self, module_type):
        pass

    @abstractmethod
    def get_module_instance(self, name):
        pass

    @abstractmethod
    def run(self):
        pass
