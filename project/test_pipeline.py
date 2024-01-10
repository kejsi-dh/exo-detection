import os
import sqlite3
import datapipeline as pipe

db_path = "sqlite:////data/data.sqlite"
if os.path.exists(db_path): os.remove(db_path)

pipe.main()

assert os.path.exists(db_path), "Database does not exist!"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
conn.close()

assert ('planet_systems',) in table, "PS table not found!"
assert ('radial_velocity',) in table, "RV table not found!"
assert ('pulsar_timing',) in table, "PT table not found!"
assert ('microlensing',) in table, "ML table not found!"
assert ('direct_imaging',) in table, "DI table not found!"
assert ('transit',) in table, "TR table not found!"
    
print("The test was executed successfully!")