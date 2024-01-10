import os
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
    
print("The test was executed successfully!")