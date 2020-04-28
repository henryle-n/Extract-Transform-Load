# Let's Cook!;&nbsp; |-> Extract -> Transform -> Load
## Overview   
In this project, team of two: ***Henry Le*** and ***Abimbola Agunloye*** processed two downloaded CSV files from Kaggle.com.   
<br>
The main objectives are to clean up, process, load final version into SQLite DataBase.  
<br>
<hr>


<p align="center">
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/maintheme_pic.gif" alt="error" max-height="50%" max-width="50%">
</p>  

*Created by: Henry Le | Apr. 27, 2020*

<hr>

## Tools/ Techniques/ Modules  
* Python | SQLAlchemy | SQLite3  
* Pandas | TQDM | Numpy | Datetime | CSV | OS (path, join) | UTF-8 Encoding

## Table of Content
There are three branches in this repository:  
* **master** :: main branch contains these files:
    - **ipynb_checkpoints** : jupyter notebooks checkpoints    
    - **In_Dev** : other file versions with new development
    - **Pictures** : contains pictures of exported db, progress bar, folder hierachy, etc.
    - **SQLite_HLE.py** : python app converted from ***hle_IMDb.ipynb***
    - **agun_netflix.ipynb**   : jupyter notebook developed by **Abimbola Agunloye** 
    - **hle_IMDb.ipynb** : jupyter notebook developed by **Henry Le**  
    
* **hle** :: contains IMDb data and ETL of this database, pictures of final database, tables, progress bar, etc.  
* **agun** ::  contains Netflix data and ETL of this database  





## Finding Data (Extract)  
Link to both CSVs:  

* Netflix: https://www.kaggle.com/shivamb/netflix-shows  
* IMDB : https://www.kaggle.com/PromptCloudHQ/imdb-data  

## Data Cleanup & Analysis (Transform)  
After two datasets were downloaded, performed data transformation as the following:  

### IMDb File  (by: **Henry Le**)
* Convert data: empty string to number, float to integer, string to date  
* Replacing data: replace letters in 'id' column with empty string, '$' for 'USD' currency, fill_na for missing data  
* Split data: currency and value into two columns  
* Break up one columns to multiple ones
* Re-name and re-arrange columns  

### Netflix File  (by: **Abimbola Agunloye**)
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
* **imdb_movies.csv**  :: SQLAlchemy with Class and Table creation to load Pandas DataFrame into SQL Lite via engine/connection  
* **netflix_movie.csv** :: manually loaded by SQL Lite -> File -> Import  
* **netflix_tv_show.csv**  :: manually loaded by SQL Lite -> File -> Import   

## Summary
* Both downloaded datasets are not cleaned, lots of issues such as numbers mixed with strings, missing data, special characters, inconsistent data in the same columns, date time are all in one columns, etc. These create many issues with DataType mismatch upon pushing to SQLite by SQL Alchemy

* SQL Lite Limitations: can processed interger upto 8-bit by default, thus was causing errors upon using SQLAlchemy to load data. Upon intensive research online and from documentations, found the solutions to assign integer-64-bit to SQL Lite



## Other Considerations with SQL Alchemy  
* Program was built with an option to let user to select amount of data to load. This helps prevent program from crashing on slower computing devices  

<p align="center">  
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/user_input_jpnb.gif" alt="error" max-height="50%" max-width="50%">
</p>

<p align="center">  
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/user_input_terminal.gif" alt="error" max-height="50%" max-width="50%">
 </p>
       

* To automate the process, the Jupyter Notebook contains codes (in ***Part 3*** towards the end of the notebook) to convert all codes into a Python file than can be run from terminal. Please remember that after conversion, comment out the conversion part to prevent accidental deletion of the python file  

* Since the database is too large to upload to GitHub, recommend to download to local storage and use the codes in this repository to replicate the project if desired  

* Loading data takes good amount of time especially a large one, so progress bar was built in for Jupyter Notebook and records/ progress percentage messages are added to both Jupter Notebook and Python to help user track the progress, as below. Note that, the progress bar only works in Jupyter Notebook. So far, I'm unable to find any stable modules to work with both Python and Jupyter Notebook.

<p align="center">
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/PrgBar_in_jpnb.gif" alt="error">
</p>
<p align="center">  
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/PrgBar_in_Terminal.gif" alt="error" max-height="50%" max-width="50%">
</p>


* Upon running the program, there will be two more folders created to store the cleaned csv and final SQL Lite DB. Final folder structure as below:  
<p align="center">
  <img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/Final_Folders.png" alt="error" max-height="50%" max-width="50%">
</p>  


## Final Loaded SQLite DB Images 
* **All tables**  

<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB.png" alt="error" max-height="30%" max-width="30%">  

* **imdb_movies** table 
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_imdb_movies.png" alt="error" max-height="30%" max-width="30%">  


* **netflix_movie**  table
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_movie.png" alt="error" max-height="30%" max-width="30%">   


* **netflix_tv_show** table 
<img src="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_tv_show.png" alt="error" max-height="30%" max-width="30%">  

