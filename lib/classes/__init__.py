

def seed_database(db_file, seed_file):
    try:
        CONN = sqlite3.connect(f"{db_file}")
        CURSOR = CONN.cursor()  
    
        with open(f"{seed_file}", 'r') as seed_sql:
            sql_commands = seed_sql.read().split(';')

            for sql_command in sql_commands:
                CURSOR.execute(sql_command)
            
            CONN.commit()

        print("Database seeded successfully!")

    except sqlite3.Error as e:
        print(f"Error seeding the database: {e}")

    finally:
        if CONN:
            CONN.close()

