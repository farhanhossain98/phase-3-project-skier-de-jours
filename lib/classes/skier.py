class Skier:

    all = []

    def __init__(self, name):
        self.name = name
        Skier.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) is str and 0 < len(new_name) >15 :
            self._name = new_name
        else:
            raise Exception("Name must be of type string class and between 0-15 characters.")
