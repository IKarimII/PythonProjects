class Car:

def __init__(self, **kw):
    self.make = kw.get("make")

    self.model= kw.get("model")

    self.colour = kw.get("colour")

    self.seats = kw.get("seats")

