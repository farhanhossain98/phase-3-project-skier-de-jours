class RidingTeam:

    all = []

    def __init__(self,horse_name, rider_name, equipment):
        self.horse_name = horse_name
        self.rider_name = rider_name
        RidingTeam.all.append(self)
    

    @property
    def horse_name(self):
        return self._horse_name

    @horse_name.setter
    def horse_name(self, name):
        pass

    @property
    def rider_name(self, name):
        pass



    from classes.event import Event
    from classes.registration import Registration
    from classes.skier import Skier
    


