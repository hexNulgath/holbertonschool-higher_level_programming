class CountedIterator():
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def __next__(self):
        self.count += 1
        next(self.iterator)
        return self.count

    def get_count(self):
        return self.count