from classes.__init__ import CONN, CURSOR

class Skier:

    # all = []

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
        # Skier.all.append(self)
    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS skiers (id INTEGER PRIMARY KEY, name TEXT)"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS skiers
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def print_db_record ( cls, record ) :
        skier = Skier(
            id = record[0],
            name = record[1],
        )
        print(f"Skier name: {skier.name} | id: {skier.id}")

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
    def id(self):
        if self._id is None:
            return -1
        else:
            return self._id 
    
    @id.setter
    def id(self, id):
        self._id = id

    def __repr__ ( self ) :
        return f"{{ 'id': { self.id }, 'name': { self.name }}}"

    @classmethod
    def find_by_name(cls, search_name):
        sql = f"SELECT * FROM skiers WHERE name LIKE '{search_name}'"
        skiers = CURSOR.execute(sql).fetchall()
        if skiers:
            return Skier.print_db_records( skiers )
        else :
            raise Exception( 'No skier found with that name.' )
    
    @classmethod
    def new_from_db ( cls, record ) :
        return Skier(
            id = record[0],
            name = record[1],
            )
    
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f'SELECT * FROM skiers WHERE id = { id }'
            skier = CURSOR.execute( sql ).fetchone()
            if skier :
                return Skier.new_from_db( skier ).print_db_record(skier)
            else :
                return None
        else :
            raise Exception( 'Id must be a number greater than 0.' )


    # @property
    # def registration(self):
    #     return self._registration
    
    # @registration.setter
    # def registration(self, registration):
    #     if type(registration) is Registration:
    #         self._registration = registration
    #     else:
    #         raise Exception('Registration must be of Registration class.')


    def registrations(self):
        sql = f"""
                
            SELECT skiers.name, events.location, riding_teams.rider_name, riding_teams.horse_name  
            FROM registrations 
            INNER JOIN skiers on registrations.skier_id = skiers.id
            INNER JOIN events on registrations.event_id = events.id
            INNER JOIN riding_teams on registrations.riding_team_id = riding_teams.id
            WHERE skiers.id = {self.id}
            """
        results = CURSOR.execute(sql).fetchall()
        for row in results:
            print(f"Registration details for {row[0]}: ")
            print(f"Event location: {row[1]}, Rider: {row[2]}, Horse: {row[3]} ")

        # return [ registration for registration in Registration.all if 
        # registration.skier is self ]

    def events(self):
        sql = f"""
            SELECT skiers.name, events.location, events.capacity
            FROM registrations 
            INNER JOIN skiers on registrations.skier_id = skiers.id
            INNER JOIN events on registrations.event_id = events.id
            WHERE skiers.id = {self.id}
            """
        results = CURSOR.execute(sql).fetchall()
        print("Event details are as follows: ")
        for result in results:
            print(f"Get ready {result[0]}, your next event will be held in {result[1]} with a crowd capicty of {result[2]}")
        
        # return list (set ([registration.event for registration in self.registrations() ]))
    

    def create_registration(self, riding_team_id, event_id):
        r = Registration.create(riding_team_id, self.id, event_id)
        print(f"Great job, {self.name}! You just created a registration!")
        print(r)
        # return Registration(
        #     skier = self,
        #     event = event,
        #     riding_team = riding_team
        # )
    


from classes.registration import Registration

