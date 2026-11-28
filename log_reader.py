from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
import csv
import json

@dataclass(frozen=True)
class LogRecord:
    timestamp: datetime
    ip_address: str
    username: str
    result: str

class LogReader(ABC):  # Adapter: Target
    @abstractmethod
    def read_logs(self, file_path): ...

class CSVFileReader:  # Adaptee
    def read_csv(self, file_path):
        with open(file_path, encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f))

class JSONFileReader:  # Adaptee
    def read_json(self, file_path):
        with open(file_path, encoding='utf-8-sig') as f:
            rows = json.load(f)
        if not isinstance(rows, list):
            raise ValueError('JSON must contain a list of records')
        return rows

def normalize(rows):
    records = []
    for i, row in enumerate(rows, 1):
        try:
            row = {k.strip().lower(): v for k, v in row.items()}
            result = row['result'].strip().lower()
            if result not in ('failure', 'success'):
                raise ValueError('result must be failure or success')
            timestamp = datetime.fromisoformat(row['timestamp'])
            if timestamp.tzinfo is not None:
                raise ValueError('Use local timestamps without timezone')
            ip, user = row['ip_address'].strip(), row['username'].strip()
            if not ip or not user:
                raise ValueError('Empty IP or username')
            records.append(LogRecord(timestamp, ip, user, result))
        except (KeyError, ValueError, TypeError, AttributeError) as e:
            raise ValueError(f'Record {i}: invalid or missing field: {e}') from e
    return records

class CSVLogAdapter(LogReader):  # Concrete Adapter
    def __init__(self): self.reader = CSVFileReader()
    def read_logs(self, file_path): return normalize(self.reader.read_csv(file_path))

class JSONLogAdapter(LogReader):  # Concrete Adapter
    def __init__(self): self.reader = JSONFileReader()
    def read_logs(self, file_path): return normalize(self.reader.read_json(file_path))
