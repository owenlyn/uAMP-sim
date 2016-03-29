#! /usr/bin/python
import argparse
from collections import defaultdict, deque

from device import DeviceState
from sim_interface import SimulatorBase, SimModule
from utils import PriorityQueue


class Simulator(SimulatorBase):
    def __init__(self):
        self.modules = {}
        self.module_type_map = defaultdict(deque)

        self.device_state = DeviceState()
        self.event_queue = PriorityQueue()
        self.alarms = []
        self.modules = {}
        self.event_listeners = {}

    def register(self, sim_module, override=False):
        if not isinstance(sim_module, SimModule):
            raise TypeError("Expected SimModule object")

        if sim_module.get_name() in self.modules:
            raise Exception("Module %s already exists" % sim_module.get_name())

        self.modules[sim_module.get_name()] = sim_module

        if override:
            self.module_type_map[sim_module.get_type()].appendleft(sim_module)
        else:
            self.module_type_map[sim_module.get_type()].append(sim_module)

    def has_module_instance(self, name):
        return name in self.modules

    def get_module_instance(self, name):
        return self.modules[name]

    def get_module_for_type(self, module_type):
        if module_type in self.module_type_map:
            return self.module_type_map[module_type][0]
        else:
            return None

    def build(self, config):
        # Instantiate necessary modules based on config files

        # Build list of modules
        for module in self.modules.values():
            module.build()

    def run(self, trace_file):
        super().run()

    def subscribe(self, event_type, handler, event_filter=None):
        if event_type not in self.event_listeners:
            self.event_listeners[event_type] = []
        self.event_listeners[event_type].append(handler)

    def broadcast(self, event):
        # Get the set of listeners for the given event type
        listeners = self.event_listeners[event.get_type()]
        for listener in listeners:
            # TODO: Send event to each subscribed listener
            pass

    def register_alarm(self, alarm, handler):
        pass


def parse_args():
    parser = argparse.ArgumentParser(description='Run uamp_sim')
    parser.add_argument('--trace', type=str, required=True,
                        help='User log trace file')
    parser.add_argument('--sim_config', type=str, required=True,
                        help='Sim Configuration File')
    return parser.parse_args()


def build_sim(args):
    simulator = Simulator()
    simulator.build(args.sim_config)
    return simulator

if __name__ == "__main__":
    command_args = parse_args()
    sim = build_sim(command_args)
    sim.run(command_args.trace)
