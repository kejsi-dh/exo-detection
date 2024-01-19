import os
import pandas as pd
import urllib.request
import zipfile
from pathlib import Path
from sqlalchemy import BIGINT, TEXT, FLOAT
import sqlite3

file_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
data_name = Path(file_url).stem
zipfile_name = data_name + '.zip'

# Download and extract zip file
urllib.request.urlretrieve(file_url, zipfile_name)
with zipfile.ZipFile(zipfile_name, 'r') as z:
    with z.open("data.csv") as f:
        df = pd.read_csv(f, delimiter=';', usecols=range(11), decimal=',')
os.remove(zipfile_name)

df = df.reset_index()
df = df.iloc[:, [0,1,2,3,4,9,10]]
df.columns = ['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)', \
    'Batterietemperatur in °C', 'Geraet aktiv']

# Rename columns
df = df.rename(columns = {
    'Temperatur in °C (DWD)': 'Temperatur',
    'Batterietemperatur in °C': 'Batterietemperatur'
})

# Transform temperature data
df['Temperatur'] = (df['Temperatur'] * 9/5) + 32
df['Batterietemperatur'] = (df['Batterietemperatur'] * 9/5) + 32

# Validate data
df = df.loc[df['Geraet'] > 0]
df = df.loc[(df['Monat'] > 0) & (df['Monat'] < 13)]
df = df.loc[df['Geraet aktiv'].isin(['Ja', 'Nein'])]

# Add data into an SQLite database
df.to_sql("temperatures", "sqlite:///temperatures.sqlite", if_exists = 'replace', index = False, \
    dtype = {
    'Geraet': BIGINT,
    'Hersteller': TEXT,
    'Model': TEXT,
    'Monat': BIGINT,
    'Temperatur': FLOAT,
    'Batterietemperatur': FLOAT,
    'Geraet aktiv': TEXT
})