import events
from sim_interface import TraceReader
import json
import gzip
from datetime import datetime


class JsonTraceReader(TraceReader):
    def __init__(self, filename):
        TraceReader.__init__(self, filename)
        self.trace_logs = None
        self.trace_pos = 0

    def build(self):
        if self.trace_filename.endswith('.json'):
            with open(self.trace_filename, 'r') as fp:
                self.trace_logs = json.load(fp)
        elif self.trace_filename.endswith('.json.gz'):
            with gzip.open(self.trace_filename, 'rt') as fp:
                self.trace_logs = json.load(fp)
        else:
            raise Exception('Invalid JSON file type. Expected .json or .json.gz')

    def finish(self):
        pass

    def get_event(self):
        if self.end_of_trace():
            return None

        event = JsonTraceReader.convert_json_to_event(self.trace_logs[self.trace_pos])
        self.trace_pos += 1
        return event

    def peek_event(self):
        if self.end_of_trace():
            return None

        event = JsonTraceReader.convert_json_to_event(self.trace_logs[self.trace_pos])
        return event

    def end_of_trace(self):
        return self.trace_pos >= len(self.trace_logs)

    def get_events(self, count):
        events_list = []
        for i in range(count):
            event = self.get_event()
            if event:
                events_list.append(event)
            else:
                break
        return events_list

    @staticmethod
    def convert_json_to_event(event_json):
        data = event_json['log_data']
        timestamp = datetime.fromtimestamp(data['timestampMillis'] / 1000)
        if event_json['log_type'] == 'event':
            return events.Event(event_type=events.EventType.PSEUDO,
                                timestamp=timestamp)
        elif event_json['log_type'] == 'foreground_app':
            return events.AppActivityUsageEvent(timestamp=timestamp,
                                           app_id=data['packageName'],
                                           source_class=data['sourceClassName'])
        elif event_json['log_type'] == 'system_snapshot':
            return events.SystemMemorySnapshot(timestamp=timestamp)


def get_trace_reader(filename, type='json'):
    if type == 'json':
        return JsonTraceReader(filename=filename)
    else:
        raise Exception("Invalid Trace File Type")
