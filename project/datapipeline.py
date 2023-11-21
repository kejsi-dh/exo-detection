import urllib.error
import sqlite3
import time
import numpy as np
import pandas as pd

# Links to the datasources
url1 = "/Users/Kejsi/Downloads/PSCompPars.csv"
url2 = "/Users/Kejsi/Downloads/ML_table.csv"
url3 = "/Users/Kejsi/Downloads/directimaging_table.csv"
url4 = "/Users/Kejsi/Downloads/TD_table.csv"

# Loads data from the csv file and returns it as a dataframe
def load_data(url: str, loads: int = 0) -> pd.DataFrame:
    for _ in range(loads+1):
        try:
            file = pd.read_csv(url)
            break
        except (urllib.error.HTTPError, urllib.error.URLError):
            time.sleep(5)
    return file

# Loads the first dataset and returns the clean dataframe
def dataset1() -> pd.DataFrame:
    file = load_data(url = url1, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 1: Planetary Systems")
    
    file = file.iloc[:, [0,4,5,6,7,8,9,10]]
    file.columns = ["Planet Name", "Discovery Method", "Discovery Year", "Radical Velocity", \
        "Timing", "Transit", "Microlensing", "Imaging"]
    
    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Prepares the first dataset for planets discovered through Radial Velocity
def d1_rv(file: pd.DataFrame) -> pd.DataFrame:
    file = load_data(url = url1, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 1: Planetary Systems - RV")
    
    file = file.query('discoverymethod == "Radial Velocity"')
    file = file.iloc[:, [0,13,14,15,16,17,18,20,21,22,24,28,29,30,31,32,35,36,37,38,39]]
    file.columns = ["Planet Name", "Planet Radius (Earth)", "Planet Radius (Jupiter)", \
        "Planet Mass (Earth)", "Planet Mass (Jupiter)", "Planet Density", "Eccentricity", \
            "Inclination", "Transit Depth", "Transit Duration", "Ratio of Planet to Stellar Ratio", \
            "Stellar Radius", "Stellar Mass", "Stellar Surface Gravity", "Stellar Age", \
                "Stellar Density", "Right Ascention", "Declination", "Galactic Latitude", \
                    "Galactic Longitude", "Distance"]

    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Prepares the first dataset for planets discovered through Pulsar Timing
def d1_pt(file: pd.DataFrame) -> pd.DataFrame:
    file = load_data(url = url1, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 1: Planetary Systems - PT")
    
    file = file.query('discoverymethod == "Pulsar Timing"')
    file = file.iloc[:, [0,13,14,15,16,17,18,29,35,36,37,38,39]]
    file.columns = ["Planet Name", "Planet Radius (Earth)", "Planet Radius (Jupiter)", \
        "Planet Mass (Earth)", "Planet Mass (Jupiter)", "Planet Density", "Eccentricity", \
            "Stellar Mass", "Right Ascention", "Declination", "Galactic Latitude", \
            "Galactic Longitude", "Distance"]

    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Loads the second dataset and returns the clean dataframe (Microlensing)
def dataset2() -> pd.DataFrame:
    file = load_data(url = url2, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 2: Microlensing")
    
    file = file.iloc[:, [0,1,2,4,5,6,8,9,10,11,12]]
    file.columns = ["Planet Name", "Planet Mass (Jupiter)", "Planet Mass (Earth)", "Lens Mass", \
        "Lens Distance", "Source Distance", "Planet-Star Mass Ratio", "Right Ascention", \
            "Declination", "Galactic Longitude", "Galactic Latitude"]

    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Loads the third dataset and returns the clean dataframe (Direct Imaging)
def dataset3() -> pd.DataFrame:
    file = load_data(url = url3, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 3: Direct Imaging")
    
    file = file.iloc[:, [0,4,6,7,8,9,11,12,13,15,16]]
    file.columns = ["Planet Name", "Distance", "Right Ascention", "Declination", \
        "Galactic Longitude", "Galactic Latitude", "Stellar Mass", "Stellar Age", \
            "Planet Mass (Jupiter)", "Planet Temperature", "Planet Radius (Jupiter)"]

    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Loads the fourth dataset and returns the clean dataframe for (Transits)
def dataset4() -> pd.DataFrame:
    file = load_data(url = url4, loads = 5)
    
    if file is None:
        raise FileNotFoundError("Could not load Data Source 4: Transit")
    
    file = file.iloc[:, [0,2,3,4,8,12,13,15,17,18,19,20,21,22]]
    file.columns = ["Planet Name", "Planet Radius (Earth)", "Planet Radius (Jupiter)", \
        "Eccentricity", "Inclination", "Transit Depth", "Transit Duration", \
            "Ratio of Planet to Stellar Radius", "Stellar Radius", "Stellar Surface Gravity", \
                "Right Ascention", "Declination", "Galactic Latitude", "Galactic Longitude"]
    
    file.replace("", np.NaN, inplace=True)
    file.dropna(how="all", inplace=True)
    
    return file

# Main
def main():
    print("Loading data...")
    ds1 = dataset1() # all planetary systems
    ds1_rv = d1_rv(ds1) # radical velocity
    ds1_pt = d1_pt(ds1) # pulsar timing
    ds2 = dataset2() # microlensing
    ds3 = dataset3() # direct imaging
    ds4 = dataset4() # transit
    
    # Add the first data frame to sqlite
    conn = sqlite3.connect('./data/planet_systems.sqlite')
    ds1.to_sql("Planetary Systems", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Planetary Systems Data has been successfully added to SQLite")
    
    # Add the second data frame to sqlite
    conn = sqlite3.connect('./data/radial_velocity.sqlite')
    ds1_rv.to_sql("Radial Velocity", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Radical Velocity Data has been successfully added to SQLite")
    
    # Add the third data frame to sqlite
    conn = sqlite3.connect('./data/pulsar_timing.sqlite')
    ds1_pt.to_sql("Pulsar Timing", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Pulsar Timing Data has been successfully added to SQLite")
    
    # Add the fourth data frame to sqlite
    conn = sqlite3.connect('./data/microlensing.sqlite')
    ds2.to_sql("Microlensing", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Microlensing Data has been successfully added to SQLite")
    
    # Add the fifth data frame to sqlite
    conn = sqlite3.connect('./data/direct_imaging.sqlite')
    ds3.to_sql("Direct Imaging", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Direct Imaging Data has been successfully added to SQLite")
    
    # Add the sixth data frame to sqlite
    conn = sqlite3.connect('./data/transit.sqlite')
    ds4.to_sql("Transit", conn, if_exists = "replace", index = False)
    conn.commit()
    conn.close()
    print("Transit Data has been successfully added to SQLite")

if __name__ == "__main__":
    main()