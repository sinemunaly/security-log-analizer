
from log_reader import (
    LogReader,
    LogRecord,
    CSVFileReader,
    JSONFileReader,
    CSVLogAdapter,
    JSONLogAdapter,
)


def test_csv_adapter():
    adapter = CSVLogAdapter(CSVFileReader())
    records = adapter.read_logs("data/sample.csv")

    assert isinstance(adapter, LogReader)
    assert len(records) == 3
    assert isinstance(records[0], LogRecord)
    assert records[0].username == "admin"
    assert records[0].result == "FAILED"


def test_json_adapter():
    adapter = JSONLogAdapter(JSONFileReader())
    records = adapter.read_logs("data/sample.json")

    assert isinstance(adapter, LogReader)
    assert len(records) == 2
    assert isinstance(records[0], LogRecord)
    assert records[1].result == "SUCCESS"
