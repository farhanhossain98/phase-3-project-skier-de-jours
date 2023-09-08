from classes.__init__ import CONN, CURSOR

class Registration:

    # all = []

    def __init__(self, riding_team_id, skier_id, event_id, id=None):
        self.riding_team_id = riding_team_id
        self.skier_id = skier_id
        self.event_id = event_id
        self.id = id
        # Registration.all.append(self)

    @property
    def id(self):
        if self._id is None:
            return -1
        else:
            return self._id 
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def riding_team_id(self):
        return self._riding_team_id
    
    @riding_team_id.setter
    def riding_team_id(self, riding_team_id):
        if isinstance(riding_team_id, int):
            self._riding_team_id = riding_team_id
        else:
            raise Exception("Invalid ID")

    @property
    def skier_id(self):
        return self._skier_id
    
    @skier_id.setter
    def skier_id(self, skier_id):
        if isinstance(skier_id, int):
            self._skier_id = skier_id
        else:
            raise Exception("Invalid ID")

    @property
    def event_id(self):
        return self._event_id
    
    @event_id.setter
    def event_id(self, event_id):
        if isinstance(event_id, int):
            self._event_id = event_id
        else:
            raise Exception("Invalid ID")



    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS registrations (id INTEGER PRIMARY KEY, riding_team_id INTEGER, skier_id INTEGER, event_id INTEGER)"
        CURSOR.execute(sql)
        CONN.commit()
   
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS registrations"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def print_db_record ( cls, record ) :
        r = Registration(
            id = record[0],
            riding_team_id = record[1],
            skier_id = record[2],
            event_id = record[3],
        )
        print(f"Riding team ID: {r.riding_team_id} | Skier ID: {r.skier_id} | Event ID: {r.event_id} | Registration ID: {r.id}")

    @classmethod
    def print_db_records ( cls, records ) :
        return [Registration.print_db_record( record ) for record in records ]

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM registrations"
        registrations = CURSOR.execute(sql).fetchall()
        return Registration.print_db_records(registrations)
        
    def save(self):
        sql = "INSERT INTO registrations (riding_team_id, skier_id, event_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.riding_team_id, self.skier_id, self.event_id))
        CONN.commit()
        self.id = CURSOR.lastrowid    

    @classmethod
    def create(cls, riding_team_id, skier_id, event_id):
        r = Registration(riding_team_id, skier_id, event_id)
        r.save()
        return r

    @classmethod
    def new_from_db ( cls, record ) :
        return Registration(
            id = record[0],
            riding_team_id = record[1],
            skier_id = record[2],
            event_id = record[3],
            )
        

    @property
    def riding_team(self) :
        return self._riding_team
    
    @riding_team.setter
    def riding_team(self, new_team) :
        if type(new_team) is RidingTeam :
            self._riding_team = new_team
        else :
            raise TypeError('Riding team must be of the RidingTeam class.')
        
    @property
    def skier(self):
        return self._skier
    
    @skier.setter
    def skier(self, new_skier):
        if type(new_skier) is Skier:
            self._skier = new_skier
        else:
            raise TypeError('Skier must be of the Skier class')
        
    @property
    def event(self):
        return self._event
    
    @event.setter
    def event(self, new_event):
        if type(new_event) is Event:
            self._event = new_event
        else:
            raise TypeError('Event must be of the Event class')
        
    
    def add_category(self, category):
        category_options = []
        pass

    
    @property
    def raw_time(self):
        return self._raw_time
    
    @raw_time.setter
    def raw_time(self, raw_time):
        if not hasattr(self, 'raw_time'):
            self._raw_time = raw_time
        else:
            raise Exception('Raw time can not be changed. We will be adding penalty time to it for final time.')
    

    @property
    def penalty(self):
        return self._penalty
    
    @penalty.setter
    def penalty(self, penalty):
        if type(penalty) is int and penalty %10 == 0: 
            self._penalty = penalty
        else:
            raise Exception('Penalty must be an increment of 10.')
    

    @property
    def final_time(self):
        return self.final_time

    @final_time.setter
    def final_time(self, raw_time, penalty):
        if not hasattr(self, "final_time"):    
            self._final_time = raw_time + penalty
        else:
            raise Exception("Final time cannot be modified... better luck next year slow poke!")
        



from classes.event import Event
from classes.riding_team import RidingTeam
from classes.skier import Skier
