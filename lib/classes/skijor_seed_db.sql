DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS skiers;
DROP TABLE IF EXISTS registrations;
DROP TABLE IF EXISTS riding_teams;

CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, capacity INTEGER, location TEXT);
CREATE TABLE IF NOT EXISTS skiers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS registrations (id INTEGER PRIMARY KEY, riding_team_id INTEGER, skier_id INTEGER, event_id INTEGER);
CREATE TABLE IF NOT EXISTS riding_teams (id INTEGER PRIMARY KEY, horse_name TEXT, rider_name TEXT);

--Seed events table
INSERT INTO events (capacity, location) VALUES (1500, "Leadville");
INSERT INTO events (capacity, location) VALUES (2500, "Colorado Springs");
INSERT INTO events (capacity, location) VALUES (500, "Denver Dash");


--Seed events skiers
INSERT INTO skiers (name) VALUES ("Farhan");
INSERT INTO skiers (name) VALUES ("Tess");
INSERT INTO skiers (name) VALUES ("Curtis");
INSERT INTO skiers (name) VALUES ("BreElle");
INSERT INTO skiers (name) VALUES ("John");
INSERT INTO skiers (name) VALUES ("Teddy");


--Seed registrations



--Seed riding_teams

