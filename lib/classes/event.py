class Event:

    all = []

    def __init__(self, capacity, location):
        self.capacity = capacity 
        self.location = location
        Event.all.append(self)

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, name)