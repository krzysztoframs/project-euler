class Fibonacci:
    __slots__ = ['earlier', 'previous', 'current', 'item_index']

    def __init__(self):
        self.item_index = -1
        self.earlier = 0
        self.previous = 1
        self.current = 0

    def next(self) -> int:
        self.item_index += 1
        if self.item_index == 0:
            self.earlier = 0
            self.previous = 0
            self.current = 0
        elif self.item_index in [1, 2]:
            self.earlier = 1
            self.previous = 1
            self.current = 1
        else:
            self.current = self.earlier + self.previous
            self.earlier = self.previous
            self.previous = self.current

        return self.current

    def get_current(self) -> int:
        return self.current

    def get_previous(self) -> int:
        return self.earlier

    def reset(self):
        self.earlier = 0
        self.previous = 1
        self.current = 0
        self.item_index = -1

    def get_current_item(self) -> int:
        return self.item_index

    def get_item(self, item_index: int) -> int:
        for n in range(0, item_index + 1):
            self.next()

        return self.get_current()
