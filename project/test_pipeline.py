import os
import pandas as pd
import pytest
import sqlite3
from sqlalchemy import create_engine, inspect
import datapipeline as pipe

# Test to check whether the datasets get loaded
@pytest.mark.dependency()
def test_datasources():
    data1 = pipe.dataset1()
    assert isinstance(data1, pd.DataFrame), "Test failed! - PS"
    
    data1_rv = pipe.d1_rv(data1)
    assert isinstance(data1_rv, pd.DataFrame), "Test failed! - RV"
    
    data1_pt = pipe.d1_pt(data1)
    assert isinstance(data1_pt, pd.DataFrame), "Test failed! - PT"
    
    data2 = pipe.dataset2()
    assert isinstance(data2, pd.DataFrame), "Test failed! - ML"
    
    data3 = pipe.dataset3()
    assert isinstance(data3, pd.DataFrame), "Test failed! - DI"
    
    data4 = pipe.dataset4()
    assert isinstance(data4, pd.DataFrame), "Test failed! - TR"
    
    print("All datasets get loaded!")
    
# Test to see whether data gets stored
@pytest.mark.dependency()
def test_storingdf():
    data = {
        "Name": ['Tom', 'Nicholas', 'Andrea'], 
        "Age": [26, 43, 15]
    }
    df = pd.DataFrame(data)
    
    test_datapath = './data/data_test.sqlite'
    conn = sqlite3.connect(test_datapath)
    df.to_sql("Test", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    
    assert os.path.exists(test_datapath), "Test database was not created!"
    
    conn = sqlite3.connect(test_datapath)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Test',) in table, "Test table not found!"
    
    if os.path.exists(test_datapath): os.remove(test_datapath)
    
    print("The process of storing the data was successful!")
    

# Testing the real pipeline
@pytest.mark.dependency(depends=["test_datasources", "test_storingdf"])
def test_pipeline():
    db_ps = './data/planet_systems.sqlite'
    db_rv = './data/radial_velocity.sqlite'
    db_pt = './data/pulsar_timing.sqlite'
    db_ml = './data/microlensing.sqlite'
    db_di = './data/direct_imaging.sqlite'
    db_tr = './data/transit.sqlite'
    
    if os.path.exists(db_ps): os.remove(db_ps)
    if os.path.exists(db_rv): os.remove(db_rv)
    if os.path.exists(db_pt): os.remove(db_pt)
    if os.path.exists(db_ml): os.remove(db_ml)
    if os.path.exists(db_di): os.remove(db_di)
    if os.path.exists(db_tr): os.remove(db_tr)
    
    pipe.main()
    
    assert os.path.exists(db_ps), "PS table does not exist!"
    assert os.path.exists(db_rv), "RV table does not exist!"
    assert os.path.exists(db_pt), "PT table does not exist!"
    assert os.path.exists(db_ml), "ML table does not exist!"
    assert os.path.exists(db_di), "DI table does not exist!"
    assert os.path.exists(db_tr), "TR table does not exist!"
    
    # Planetary Systems table, first dataset
    conn = sqlite3.connect(db_ps)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Planetary Systems',) in table, "PS table not found!"
    
    # Radial Velocity table, first dataset
    conn = sqlite3.connect(db_rv)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Radial Velocity',) in table, "RV table not found!"
    
    # Pulsar Timing table, first dataset
    conn = sqlite3.connect(db_pt)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Pulsar Timing',) in table, "PT table not found!"
    
    # Microlensing table, second dataset
    conn = sqlite3.connect(db_ml)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Microlensing',) in table, "ML table not found!"
    
    # Direct Imaging table, third dataset
    conn = sqlite3.connect(db_di)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Direct Imaging',) in table, "DI table not found!"
    
    # Transit table, fourth dataset
    conn = sqlite3.connect(db_tr)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchall()
    conn.close()
    
    assert len(table) == 1, "Expected tables: 1 \n Found: {} tables".format(len(table))
    assert ('Transit',) in table, "TR table not found!"
    
    print("The test was executed without any errors!")
 
if __name__ == '__main__':
    test_pipeline()