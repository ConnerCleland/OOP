class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        self.amount = min(self.capacity, self.amount + amount)

    def pour_out(self, amount):
        self.amount = max(0, self.amount - amount)
