from classes.__init__ import CONN, CURSOR

class Skier:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS skiers (id INTEGER PRIMARY KEY, name TEXT)"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF NOT EXISTS skiers
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def print_db_record ( cls, record ) :
        skier = Skier(
            id = record[0],
            name = record[1],
        )
        print(f"Skier name: {skier.name}, id: {skier.id}")

    @classmethod
    def print_db_records ( cls, records ) :
        return [Skier.print_db_record( record ) for record in records ]


    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM skiers"
        skiers = CURSOR.execute(sql).fetchall()
        return Skier.print_db_records(skiers)
        
    
    def save(self):
        sql = "INSERT INTO skiers (name) VALUES (?)"
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls,name):
        skier = cls(name)
        skier.save()
        return skier
    

    @classmethod
    def say_hello ( cls ) :
        print( "Hello!!!" )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) is str and 0 < len(new_name) < 15 :
            self._name = new_name
        else:
            raise Exception("Name must be of type string class and between 0-15 characters.")

    
    @property
    def registration(self):
        return self._registration
    
    @registration.setter
    def registration(self, registration):
        if type(registration) is Registration:
            self._registration = registration
        else:
            raise Exception('Registration must be of Registration class.')


    def registrations(self):
        return [ registration for registration in Registration.all if 
        registration.skier is self ]

    def events(self):
        return list (set ([registration.event for registration in self.registrations() ]))
    

    def create_registration(self,riding_team, event):
        return Registration(
            skier = self,
            event = event,
            riding_team = riding_team
        )
    


from classes.registration import Registration
from classes.event import Event
from classes.riding_team import RidingTeam
