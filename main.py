from log_reader import (
    LogReader,
    CSVFileReader,
    JSONFileReader,
    CSVLogAdapter,
    JSONLogAdapter,
)


def display_logs(reader: LogReader, file_path: str):
    """Kaynak türünden bağımsız log gösterimi."""
    records = reader.read_logs(file_path)

    print(f"\nToplam {len(records)} kayıt bulundu.")

    for record in records:
        print(
            f"{record.timestamp} | "
            f"{record.ip_address} | "
            f"{record.username} | "
            f"{record.result}"
        )


def main():
    print("=== Güvenlik Log Analizi Sistemi ===")

    csv_adapter = CSVLogAdapter(CSVFileReader())
    json_adapter = JSONLogAdapter(JSONFileReader())

    print("\n--- CSV Kayıtları ---")
    display_logs(csv_adapter, "data/sample.csv")

    print("\n--- JSON Kayıtları ---")
    display_logs(json_adapter, "data/sample.json")


if __name__ == "__main__":
    main()
    