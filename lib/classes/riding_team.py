from classes.__init__ import CONN, CURSOR

class RidingTeam:

    

    def __init__( self, horse_name, rider_name, id = None ):
        self.horse_name = horse_name
        self.rider_name = rider_name
        self.id = id
        
    
    @classmethod
    def create_table(cls):
        sql = " CREATE TABLE IF NOT EXISTS riding_teams (id INTEGER PRIMARY KEY, horse_name TEXT, rider_name TEXT) "
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = " DROP TABLE IF EXISTS riding_teams "
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def print_db_record ( cls, record ):
        riding_team = RidingTeam(
            id = record [0],
            horse_name = record[1],
            rider_name = record[2],
        )
        print(f"Horse Name: {riding_team.horse_name}, Rider Name: {riding_team.rider_name}, ID: {riding_team.id}")

    @classmethod
    def print_db_record ( cls, record ):
        riding_team = RidingTeam(
            id = record [0],
            horse_name = record[1],
            rider_name = record[2],
        )
        print(f"Horse Name: {riding_team.horse_name}, Rider Name: {riding_team.rider_name}, ID: {riding_team.id}")
        
    @classmethod
    def print_db_records ( cls, records ) :
        return [RidingTeam.print_db_record( record ) for record in records ]

    @classmethod
    def get_all ( cls ):
        sql  = " SELECT * FROM riding_teams "
        riding_teams = CURSOR.execute(sql).fetchall()
        return RidingTeam.print_db_records(riding_teams)

    def save(self):
        sql = "INSERT INTO riding_teams (horse_name, rider_name) VALUES (?, ?)"
        CURSOR.execute(sql, (self.horse_name, self.rider_name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, horse_name, rider_name ):
        riding_team = cls(horse_name, rider_name)
        riding_team.save()
        return riding_team
        
    @property
    def id(self):
        if self._id is None:
            return -1
        else:
            return self._id 
    
    @id.setter
    def id(self, id):
        self._id = id

    def __repr__ ( self ) :
        return f"{{ 'id': { self.id }, 'horse name': { self.horse_name }, rider name {self.rider_name}}}"

    @classmethod
    def find_by_rider_name(cls, rider_name):
        sql = f"SELECT * FROM riding_teams WHERE riding_teams.rider_name LIKE '{rider_name}'"
        riders = CURSOR.execute(sql).fetchall()
        if riders:
            return RidingTeam.print_db_records( riders )
        else:
            raise Exception( 'No rider found with that name.' )
    
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f'SELECT * FROM riding_team WHERE id = { id }'
            riding_team = CURSOR.execute( sql ).fetchall()
            if riding_team :
                return RidingTeam.print_db_records( riding_team )
            else :
                return None
        else :
            raise Exception( 'Id must be a number greater than 0.' )








    @property
    def horse_name(self):
        return self._horse_name

    @horse_name.setter
    def horse_name(self, horse_name):
        if type(horse_name) == str:
            if 1 <= len(horse_name) <= 15:
                self._horse_name = horse_name
            else:
                raise Exception('Name must be more than 0 characters long.')
        else:
            raise Exception('Name must be a string.')
        

    @property
    def rider_name(self):
        return self._rider_name
    
    @rider_name.setter
    def rider_name(self, rider_name):
        if type(rider_name) is str:
            if 1 <= len(rider_name) <= 15 :
                self._rider_name = rider_name
            else:
                raise ValueError('Name must be more than 0 characters long.')
        else:
            raise TypeError('Name must be a string.')
        

    def registrations(self):
        return [registration for registration in Registration.all if registration.riding_team is self]
    
    def create_registration(self, skier, event):
        return Registration(
            riding_team = self,
            skier = skier,
            event = event
        )
   
   
    def events(self):
        return [registration.event for registration in self.registrations()]

    
    def average_speed(self):
        pass
    
    
    
        


from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier



