# Project Plan

## Title
<!-- Give your project a short title. -->
Methods of Exoplanet Detection

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Are certain methods of detection able to capture only certain exoplanets?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
These past years, there has been an increased interest in the planetary system, as it is evident, not only from the successful launch of the Indian spacecraft near what is known as "the dark side of the moon", but also on potential high hopes in discovering exoplanets, which could be inhabitable in the near future. Although the inhabitability aspect of these planets remains relatively unknown or uncertain, instead, in this project, I view the different methods used to discover exoplanets through the years and check if certain methods are only able to capture certain planets based on their properties (i.e. mass, radius, etc.).

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/index.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars
* Data Type: CSV

A composite data file of Exoplanet Systems, which include fields such as the exoplanet system name, number of stars and planets, discovery method and year, the orbital days, planet radius and mass, and stellar radius and mass.

### Datasource2: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/index.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=ML
* Data Type: CSV

A data file of exoplanets found through the Microlensing method, which include fields such as right ascention and declination, planet and lens mass, and Einstein crossing days.

### Datasource3: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/index.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=directimaging&constraint=immodeldef=1
* Data Type: CSV

A data file of exoplanets found through the Direct Imaging method, which include fields such as right ascention and declination, distance, planet mass and radius (Jupiter mass), and stellar mass and age.

### Datasource4: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/index.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TD
* Data Type: CSV

A data file of exoplanets found through the Transit method, which include fields such as right ascention and declination, distance, planet mass and radius, and stellar radius.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore datasources [#1] (https://github.com/kejsi-dh/made-template/issues/1)
2. Build a data pipeline [#2] (https://github.com/kejsi-dh/made-template/issues/2)
3. Build the automated tests
4. Analyse resulting data
5. Draw conclusion from the observations
6. Make repository ready for submission