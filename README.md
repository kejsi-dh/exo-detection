# Methods of Exoplanet Detection

This project aims to inquire on whether a certain detection method can only detect planets that possess certain properties. Therefore, it uses open source datasources from NASA's Exoplanet Archive, in order to analyse the properties of the planets for each of the most known 5 methods.

In the `project` folder, the entire process can be found:
* The [data pipeline](https://github.com/kejsi-dh/made-template/blob/main/project/datapipeline.py) file loads the datasources from the Internet and processes the information, which will lastly be saved into a SQLite database.
* The [pipeline test](https://github.com/kejsi-dh/made-template/blob/main/project/test_pipeline.py) file is a test file that verifies that the database and the appropriate tables are found.
* The [data exploration](https://github.com/kejsi-dh/made-template/blob/main/project/data-exploration.ipynb) file analyses different aspects of the planets for each detection method, by building plots.

The final report on the findings from this project can be found as a [pdf file](https://github.com/kejsi-dh/made-template/blob/main/project/report.pdf).
