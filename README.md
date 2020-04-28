# Extract-Transform-Load | SQLAlchemy and SQL Lite
## Overview   
In this project, team of two: ***Henry Le*** and ***Abimbola Agunloye*** processed two downloaded CSV files from Kaggle.com.  
<hr>
The main objectives are to clean up, process, load final version into SQL Lite DataBase.   

## Tools/ Techniques/ Modules  
* Python | SQLAlchemy | SQL Lite  
* Pandas | TQDM | Numpy | Datetime | CSV | OS (path, join) | UTF-8 Encoding

## Table of Content
There are three branches in this repository:  
* **master** :: main branch  
* **hle** :: contains IMDb data and ETL of this database, pictures of final database, tables, progress bar, etc.  
* **agun** ::  contains Netflix data and ETL of this database  

## Finding Data (Extract)  
Link to both CSVs:  

* Netflix: https://www.kaggle.com/shivamb/netflix-shows  
* IMDB : https://www.kaggle.com/PromptCloudHQ/imdb-data  

## Data Cleanup & Analysis (Transform)  
After two datasets were downloaded, performed ETL on the data as the following:  

### IMDb File  
* Convert data: empty string to number, float to integer, string to date  
* Replacing data: replace letters in 'id' column with empty string, '$' for 'USD' currency, fill_na for missing data  
* Split data: currency and value into two columns  
* Break up one columns to multiple ones
* Re-name and re-arrange columns  

### Netflix File  
* Drop un-necessary columns  
* Extract data, month, year from one columns and split into 3 columns  
* Convert string (object) dtype to integer with numpy module  
* Split entire database into 'tv_show' and 'movie' based on column 'type'  
* Exported to CSV and get ready for loading into SQL Lite  
* Re-name and re-arrange columns  

## Loading Data in to SQL Lite  
### DataBase Selection  
Since the data is relational database with columns and rows, SQL Lite is chosen for the project instead of un-relational DB like MongoDB  

The following tables are loaded into SQL Lite:  
* **imdb_movies.csv**  
* **netflix_movie.csv**  
* **netflix_tv_show.csv**  

### Method of Loading
* **imdb_movies.csv**  :: SQLAlchemy with Class and Tables creation to load Pandas DataFrame into SQL Lite through engine/connection  
* **netflix_movie.csv** :: manual loaded by SQL Lite -> File -> Import  
* **netflix_tv_show.csv**  :: manual loaded by SQL Lite -> File -> Import  

## Final Images of Loaded SQL Lite DB  
* **All Tables**  

<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB.png" alt="error" max-height="30%" max-width="30%">  

* **imdb_movies.csv**  
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_imdb_movies.png" alt="error" max-height="30%" max-width="30%">  


* **netflix_movie.csv**  
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_movie.png" alt="error" max-height="30%" max-width="30%">   


* **netflix_tv_show.csv** 
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_tv_show.png" alt="error" max-height="30%" max-width="30%">  

## Other Considerations with SQL Alchemy
* Since the database is too large to upload to GitHub, recommend to download to local storage and use the codes in this repository to replicate the project if desired  
* Loading data takes sometimes especially a large one, so progress bar was built in for Jupyter Notebook and records/ progress percentage messages are added to both Jupter Notebook and Python to help user track the progress, as below  

<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/Progress_Bar_Finshed.png" alt="error" max-height="50%" max-width="50%">  

<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/LoadDataInTerminal.png" alt="error" max-height="100%" max-width="100%">  


* Upon running the program, there will be two more folders created to store the cleaned csv and final SQL Lite DB. Final folder structure as below:  

<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/Final_Folders.png" alt="error" max-height="100%" max-width="100%">  

* Program was built with an option to ask user to select how much data need to be loaded to prevent program from crashing on slower computing devices

* To automate the process, the Jupyter Notebook contains codes to convert all codes into a Python file than can be run from terminal. Please remember that after conversion, comment out the conversion part to prevent accidental deletion of the python file


