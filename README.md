# Extract-Transform-Load-DB  
## Overview   
In this project, team of two: Henry Le and Abimbola Agunloye processed two downloaded CSV files from Kaggle.com.   
The main objectives are to clean up, process, load final version into SQL Lite DataBase.   


## Finding Data (Extract)  
Link to both CSVs:  

* Netflix: https://www.kaggle.com/shivamb/netflix-shows  
* IMDB : https://www.kaggle.com/PromptCloudHQ/imdb-data  

## Data Cleanup & Analysis (Tranform)  
After  datasets were downloaded, performed ETL on the data as the following:  

### IMDb File  
* Convert data: empty string to number, float to integer, string to date  
* Replacing data: replace letters in 'id' column with empty string, '$' for 'USD' currency, fill_na for missing data  
* Split data: currency and value into two columns  

### Netflix File  
* Drop un-necessary columns  
* Extract data, month, year from one columns and split into 3 columns  
* Convert string (object) dtype to integer with numpy module  
* Split entire database into 'tv_show' and 'movie' based on column 'type'  
* Exported to CSV and get ready for loading into SQL Lite  

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

<img src="/blob/hle/Pictures/ETL_DB.png" alt="Mars out of range ... Waiting for satellite signal ..." max-height="60%" max-width="60%"><p>
  
[all table](https://github.com/henryle-n/Extract-Transform-Load-DB/blob/hle/Pictures/ETL_DB.png)

* **imdb_movies.csv**  


* **netflix_movie.csv**  

* **netflix_tv_show.csv** 


