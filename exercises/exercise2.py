import urllib.error
import time
import pandas as pd
import sqlalchemy

csv_file = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# Function to read the data from the csv file
def load_data(url: str) -> pd.DataFrame:
    file = None
    for _ in range(6):
        try:
            file = pd.read_csv(url, sep=';', decimal=',')
            break
        except (urllib.error.HTTPError, urllib.error.URLError):
            time.sleep(5)
    return file

if __name__ == '__main__':
    file = load_data(csv_file)
    
    # Column "Status" gets completely dropped
    file = file.drop(columns=["Status"])
    # Empty cells get dropped
    file = file.dropna()
    
    # Modify columns: Verkehr, Laenge, Breite, IFOPT
    file = file.loc[file["Verkehr"].isin(["FV", "RV", "nur DPN"])]
    file = file.loc[(file["Laenge"] >= -90) & (file["Laenge"] <= 90)]
    file = file.loc[(file["Breite"] >= -90) & (file["Breite"] <= 90)]
    file = file.loc[file["IFOPT"].str.match(r"^[a-zA-Z]{2}:\d+:\d+(:\d+)?$")]
    
    # Load SQLite and add the modified data frame there
    file.to_sql("trainstops", "sqlite:///trainstops.sqlite", if_exists = "replace", index = False, dtype = {
        "EVA_NR": sqlalchemy.BIGINT,
        "DS100": sqlalchemy.TEXT,
        "IFOPT": sqlalchemy.TEXT,
        "NAME": sqlalchemy.TEXT,
        "Verkehr": sqlalchemy.TEXT,
        "Laenge": sqlalchemy.FLOAT,
        "Breite": sqlalchemy.FLOAT,
        "Betreiber_Name": sqlalchemy.TEXT,
        "Betreiber_Nr": sqlalchemy.BIGINT
    })