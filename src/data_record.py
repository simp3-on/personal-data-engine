class DataRecord:
    def __init__(self, source, data):
        self.source = source
        self.data = data


if __name__ == "__main__":
    record = DataRecord(
        source="browser_history",
        data={"url": "https://example.com"}
    )

    print(record.source)
    print(record.data)