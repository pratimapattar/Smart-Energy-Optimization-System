class DataLogger :
    def __init__(self) :
        self.records = []

    def store(self, record) : 
        self.records.append(record)

    # count the cycles
    def count(self) :
        return len(self.records)
