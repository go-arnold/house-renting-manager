class House:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price
        self.is_rented = False

    def rent(self):
        if self.is_rented:
            raise Exception("House already rented")
        self.is_rented = True

    def release(self):
        self.is_rented = False

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "price": self.price,
            "is_rented": self.is_rented,
        }
