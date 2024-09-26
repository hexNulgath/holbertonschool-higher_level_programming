class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)
    def extend(self, item):
        print(f"Extended the list with [{len(item)}] items.")
        super().extend(item)
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    def pop(self, index=None):
        if index is None:
            index = -1
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)