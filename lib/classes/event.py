from classes.__init__ import CONN, CURSOR

class Event:

    

    def __init__(self, capacity, location, id=None):
        self.capacity = capacity 
        self.location = location
        self.id = id
        

    def __repr__ ( self ) :
        return f"{{ 'id': { self.id }, 'location': { self.name }, 'capacity': { self.capacity }}}"

    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, capacity INTEGER, location TEXT)"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS events"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def print_db_record ( cls, record ) :
        event = Event(
            id = record[0],
            capacity = record[1],
            location = record[2],
        )
        print(f"Event location: {event.location} | Capacity: {event.capacity} |id: {event.id}")

    @classmethod
    def print_db_records ( cls, records ) :
        return [Event.print_db_record( record ) for record in records ]

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM events"
        events = CURSOR.execute(sql).fetchall()
        return Event.print_db_records(events)
        
    
    def save(self):
        sql = "INSERT INTO events (capacity, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.capacity, self.location,))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, capacity, location):
        event = cls(capacity, location)
        event.save()
        return event

    @classmethod
    def find_by_location(cls, search_location):
        sql = f"SELECT * FROM events WHERE location LIKE '{search_location}'"
        events = CURSOR.execute(sql).fetchall()
        if events:
            return Event.print_db_records( events )
        else :
            raise Exception( 'No event found at that location.' )
    
    @classmethod
    def new_from_db ( cls, record ) :
        return Event(
            id = record[0],
            capacity = record[1],
            location = record[2],
            )
    
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f'SELECT * FROM events WHERE id = { id }'
            event = CURSOR.execute( sql ).fetchone()
            if event :
                return Event.new_from_db( event ).print_db_record(event)
            else :
                return None
        else :
            raise Exception( 'Id must be a number greater than 0.' )
    
    
    
    
    
    
    
    
    
    
    
    
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) is int and not hasattr(self, "capacity"):
        # if type(capacity) is int:
            self._capacity = capacity
        else: 
            raise Exception("Capacity has to be an integer.")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location)>0 and not hasattr(self, "location"):
        # if isinstance(location, str) and len(location)>0:
            self._location = location
        else:
            # raise Exception("Location must be a string, greater than 0 characters long, and cannot be re-assigned.")
            raise Exception("Location must be a string and greater than 0 characters long.")

    
    def registrations(self):
        return [registration for registration in Registration.all if registration.event == self]

    
    def skiers(self):
        return list(set([registration.skier for registration in Registration.all if registration.event == self]))
    
    def num_skiers(self):
        return len(self.skiers())
    
    def riding_teams(self):
        return [registration.riding_team for registration in Registration.all if registration.event == self]

   
    def add_results(self, result):
        pass


    def get_results(self):
        pass



from classes.registration import Registration
