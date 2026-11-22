
import csv
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass


# Ortak güvenlik kaydı modeli
@dataclass(frozen=True)
class LogRecord:
    timestamp: str
    ip_address: str
    username: str
    result: str


# ADAPTER PATTERN - Target
# Bütün log okuyucularının ortak arayüzü
class LogReader(ABC):

    @abstractmethod
    def read_logs(self, file_path: str) -> list[LogRecord]:
        pass


# ADAPTER PATTERN - Adaptee
# CSV dosyalarını okuyan sınıf
class CSVFileReader:

    def read_csv(self, file_path: str) -> list[dict]:
        with open(file_path, encoding="utf-8-sig", newline="") as file:
            return list(csv.DictReader(file))


# ADAPTER PATTERN - Adaptee
# JSON dosyalarını okuyan sınıf
class JSONFileReader:

    def read_json(self, file_path: str) -> list[dict]:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON verisi bir liste olmalıdır.")

        return data


def normalize_record(row: dict) -> LogRecord:
    print("GELEN VERI:", repr(row))
    """Ham veriyi ortak güvenlik kaydı modeline dönüştürür."""
    return LogRecord(
        timestamp=row["timestamp"],
        ip_address=row["ip"],
        username=row["user"],
        result=row["result"],
    )


# ADAPTER PATTERN - Adapter
# CSV verilerini ortak arayüze dönüştürür
class CSVLogAdapter(LogReader):

    def __init__(self, reader: CSVFileReader):
        self.reader = reader

    def read_logs(self, file_path: str) -> list[LogRecord]:
        rows = self.reader.read_csv(file_path)
        print("CSV sütunları:", rows[0].keys())
        return [normalize_record(row) for row in rows]


# ADAPTER PATTERN - Adapter
# JSON verilerini ortak arayüze dönüştürür
class JSONLogAdapter(LogReader):

    def __init__(self, reader: JSONFileReader):
        self.reader = reader

    def read_logs(self, file_path: str) -> list[LogRecord]:
        rows = self.reader.read_json(file_path)
        return [normalize_record(row) for row in rows]
