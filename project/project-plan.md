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
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars
* Data Type: CSV

A composite data file of Exoplanet Systems, which includes fields such as the exoplanet system name, number of stars and planets, discovery method and year, the orbital days, planet radius and mass (Earch and Jupiter), and stellar radius and mass.

### Datasource2: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/docs/API_ML.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=ML
* Data Type: CSV

A data file of exoplanets found through the Microlensing method, which includes fields such as planet name, planet mass (Jupiter and Earth mass), planet-star projected semi-major axis, lens mass, lens and source distance, Einstein crossing days, planet-star mass ratio, right ascention and declination, galactic longitude and latitude, lens-source relative and microlens parallax, planet-star separation rate of change, source trajectory angle rate of change, source angular radius and crossing time, and effective timescale.

### Datasource3: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/docs/API_directimaging.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=directimaging&constraint=immodeldef=1
* Data Type: CSV

A data file of exoplanets found through the Direct Imaging method, which includes fields such as planet name, projected and true separation of star-planet, position angle planet-star, distance, number of stars, right ascention and declination, distance, stellar spectral type, stellar mass and age, planet mass (Jupiter mass), planet spectral type and temperature, and planet radius (Jupiter radius).

### Datasource4: NASA Exoplanet Archive
* Metadata URL: https://exoplanetarchive.ipac.caltech.edu/docs/API_transit_detection.html
* Data URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TD
* Data Type: CSV

A data file of exoplanets found through the Transit method, which includes fields such as planet name, orbital days, planet radius (Earth and Jupiter radius), eccentricity (upper unc., lower unc., limit flag) and inclination (upper unc., lower unc., limit flag), transit depth and duration, ratio of semi-major axis to stellar radius and of planet to stellar radius, stellar effective temperature, stellar radius, stellar surface gravity, right ascention and declination, and galactic latitude and longitude.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore datasources [#1][i1]
2. Build a data pipeline [#2][i2]
3. Build the automated tests [#3][i3]
4. Analyse resulting data
5. Draw conclusion from the observations
6. Make repository ready for submission

[i1]: https://github.com/kejsi-dh/made-template/issues/1
[i2]: https://github.com/kejsi-dh/made-template/issues/2
[i3]: https://github.com/kejsi-dh/made-template/issues/3