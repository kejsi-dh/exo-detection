import os
import pandas as pd
import sqlite3
import datapipeline as pipe

db_path = "data.sqlite"
if os.path.exists(db_path): os.remove(db_path)

pipe.main()

assert os.path.exists(db_path), "Database does not exist!"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()

assert ('Planetary Systems',) in table, "PS table not found!"
assert ('Radial Velocity',) in table, "RV table not found!"
assert ('Pulsar Timing',) in table, "PT table not found!"
assert ('Microlensing',) in table, "ML table not found!"
assert ('Direct Imaging',) in table, "DI table not found!"
assert ('Transit',) in table, "TR table not found!"

"""
# Database paths for all tables
db_ps = './planet_systems.sqlite'
db_rv = './radial_velocity.sqlite'
db_pt = './pulsar_timing.sqlite'
db_ml = './microlensing.sqlite'
db_di = './direct_imaging.sqlite'
db_tr = './transit.sqlite'
    
# Removing the SQLite tables
if os.path.exists(db_ps): os.remove(db_ps)
if os.path.exists(db_rv): os.remove(db_rv)
if os.path.exists(db_pt): os.remove(db_pt)
if os.path.exists(db_ml): os.remove(db_ml)
if os.path.exists(db_di): os.remove(db_di)
if os.path.exists(db_tr): os.remove(db_tr)
    
pipe.main() # Adding the tables in SQLite from scratch
    
# Verify that paths exist
assert os.path.exists(db_ps), "PS table does not exist!"
assert os.path.exists(db_rv), "RV table does not exist!"
assert os.path.exists(db_pt), "PT table does not exist!"
assert os.path.exists(db_ml), "ML table does not exist!"
assert os.path.exists(db_di), "DI table does not exist!"
assert os.path.exists(db_tr), "TR table does not exist!"
    
# Checks for the Planetary Systems table from the first dataset
conn = sqlite3.connect(db_ps)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Planetary Systems',) in table, "PS table not found!"
    
# Checks for the Radial Velocity table from the first dataset
conn = sqlite3.connect(db_rv)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Radial Velocity',) in table, "RV table not found!"
    
# Checks for the Pulsar Timing table from first dataset
conn = sqlite3.connect(db_pt)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Pulsar Timing',) in table, "PT table not found!"
    
# Checks for the Microlensing table from the second dataset
conn = sqlite3.connect(db_ml)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Microlensing',) in table, "ML table not found!"

# Checks for the Direct Imaging table from the third dataset
conn = sqlite3.connect(db_di)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Direct Imaging',) in table, "DI table not found!"
    
# Checks for the Transit table from the fourth dataset
conn = sqlite3.connect(db_tr)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()
    
assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
assert ('Transit',) in table, "TR table not found!"
"""
    
print("The test was executed successfully!")