# Let's Cook! &nbsp; --> Extract --> Transform --> Load
## Background
Often in time, data is not always "clean" to be analyzed, plotted or even for machine learning. In this project, two `.csv` files were downloaded from Kaggle that have several issues such as missing values, datetime format, datatype mismatch, etc. A team of two: ***Henry Le*** and ***Abimbola Agunloye*** utilized Python to perform Extract, Transform and Load operations to resolve mentioned issues. Cleaned version of data is then loaded into SQLite DataBase.


<p align="center">
  <img src="./Pictures/Gifs_and_Pics/maintheme_pic.gif" alt="error" max-height="50%" max-width="50%">
</p>  

&nbsp; &nbsp; &nbsp; <i><span style="font-family:metronova; font-size:12px"></span></i>

## Languages, Tools & Technologies
* **Languages:** 
  * Python | SQL
* **Python Libraries/ Modules:**
  * SQLAlchemy | SQLite3 | Pandas | TQDM | Numpy | Datetime | CSV | OS
* **SQL Database:**
  * SQLite
* **Software/ Applications:**
  * Visual Studio Code | Jupyter Notebook
* **Operating Systems:**
  * Windows 10 Pro

## Table of Content (master branch)

Folders/ Files | Descriptions
---- | ----- 
Pictures | pictures of finished loaded SQLite Database, Progress Bar, and Readme gif files
|

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
<ul>
  <li>
    <a class = "btn" href="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB.png"><span style = "color:blue;"><b>Click here</b></span>
    </a> to see all loaded table image<br>
  </li>

  <li>
    <a class = "btn" href="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_imdb_movies.png"><span style = "color:blue;"><b>Click here</b></span>
    </a> to see the loaded <b>imdb_movies</b> table image<br>
  </li>

  <li>
    <a class = "btn" href="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_movie.png"><span style = "color:blue;"><b>Click here</b></span>
    </a> to see the loaded <b>netflix_movie</b> table image<br>
  </li>

  <li>
    <a class = "btn" href="https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB_netflix_tv_show.png"><span style = "color:blue;"><b>Click here</b></span>
    </a> to see the loaded <b>netflix_tv_show</b> image<br>
  </li>
