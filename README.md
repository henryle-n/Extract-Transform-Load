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







    













The final tables or collections that will be used in the production database.


You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.

Project Report
At the end of the week, your team will submit a Final Report that describes the following:


Extract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).


Transform: what data cleaning or transformation was required.


Load: the final database, tables/collections, and why this was chosen.


Please upload the report to Github and submit a link to Bootcampspot.
