import os
import urllib.error
import sqlite3
import time
import numpy as np
import pandas as pd

# Links to the datasources
url1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,sy_snum,sy_pnum,discoverymethod,disc_year,rv_flag,pul_flag,tran_flag,micro_flag,ima_flag,pl_orbper,pl_orbsmax,pl_rade,pl_radj,pl_bmasse,pl_bmassj,pl_dens,pl_orbeccen,pl_eqt,pl_orbincl,pl_trandep,pl_trandur,pl_ratdor,pl_ratror,pl_rvamp,st_spectype,st_teff,st_rad,st_mass,st_logg,st_age,st_dens,st_vsin,st_rotp,ra,dec,glat,glon,sy_dist+from+pscomppars&format=csv"
url2 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_massj,pl_masse,pl_orbsmax,st_mass,sy_dist,ml_dists,ml_xtimeein,ml_massratio,ra,dec,glon,glat,ml_plxrel,ml_dsdt,ml_radsang,ml_xtimesrc,ml_efftime+from+ML&format=csv"

# No link was provided by the NASA website for this particular table;
# The link to viewing the interactive table was provided under:
# Data Source 3's Data URL in the Project Plan
drive_file = "https://drive.google.com/file/d/1DEhnB5PcfGD_DfBgcTVEbOIdTJUzXp7R/view?usp=share_link"
file_id = drive_file.split('/')[-2]
url3 = 'https://drive.google.com/uc?id=' + file_id

url4 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_orbper,pl_rade,pl_radj,pl_orbeccen,pl_orbeccenerr1,pl_orbeccenerr2,pl_orbeccenlim,pl_orbincl,pl_orbinclerr1,pl_orbinclerr2,pl_orbincllim,pl_trandep,pl_trandur,pl_ratdor,pl_ratror,st_teff,st_rad,st_logg,ra,dec,glat,glon+from+TD&format=csv"

# Loads data from the csv file and returns it as a dataframe
def load_data(url: str, loads: int = 0) -> pd.DataFrame:
    file = None
    for _ in range(loads+1):
        try:
            file = pd.read_csv(url, header = 0, on_bad_lines = 'skip')
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
    file.columns = ["Planet Name", "Discovery Method", "Discovery Year", "Radial Velocity", \
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
    ds1 = dataset1()
    ds1_rv = d1_rv(ds1)
    ds1_pt = d1_pt(ds1)
    ds2 = dataset2()
    ds3 = dataset3()
    ds4 = dataset4()
    
    conn = sqlite3.connect('data.sqlite')
    
    ds1.to_sql("planet_systems", conn, if_exists = "replace", index = False)
    print("Planetary Systems Data has been successfully added to SQLite")
    
    ds1_rv.to_sql("radial_velocity", conn, if_exists = "replace", index = False)
    print("Radical Velocity Data has been successfully added to SQLite")
    
    ds1_pt.to_sql("pulsar_timing", conn, if_exists = "replace", index = False)
    print("Pulsar Timing Data has been successfully added to SQLite")
    
    ds2.to_sql("microlensing", conn, if_exists = "replace", index = False)
    print("Microlensing Data has been successfully added to SQLite")
    
    ds3.to_sql("direct_imaging", conn, if_exists = "replace", index = False)
    print("Direct Imaging Data has been successfully added to SQLite")
    
    ds4.to_sql("transit", conn, if_exists = "replace", index = False)
    print("Transit Data has been successfully added to SQLite")
    
    conn.commit()

if __name__ == "__main__":
    main()