#!/usr/bin/env python
# coding: utf-8

# # Python | Pandas for Data Clean-up
# ---

# ## Import Modules/ Libs

# In[1]:


import pandas as pd
import csv
import datetime as dt
from datetime import datetime
import numpy as np

# for the progress bar
from time import sleep
from tqdm.notebook import tqdm


# ## Import SQL-Alchemy for SQL-Lite Data Load

# In[2]:


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Session
from sqlalchemy import func
import pathlib
import sqlite3


# ## Define local functions to use

# In[3]:


# convert to interger
def to_int (df_name, col_name):
    
    """
    1. Converting string, etc. into integer
    2. Usage:
        to_int (data-frame-name, column-name):
    """
    
    print (f"\n>> Processing Column: '{col_name}'")
    
    # convert empty string to number, if no num available, put NaN 
#     df_name[col_name] = pd.to_numeric(df_name[col_name], errors='coerce')

    try:
        df_name[col_name] = df_name[col_name].astype(np.int64)
        type_col = df_name[col_name].dtype
        print("---->>> No issue observed")
        
    except ValueError as error:
        
        print("---->>> An Exception has occured ::", str(error))
        print("---->>> Proceed with alternative routes, please wait...")
        # replace all empty space with 0
        df_name[col_name] =  df_name[col_name].fillna(0)
        df_name[col_name] = df_name[col_name].replace('',0, regex=True)

        # convert df to numpy array
        np_of_df = df_name[col_name].values

        # comvert to type as float
        np_of_df_float = np_of_df.astype(float)  

        df_name[col_name] = np_of_df_float
        df_name[col_name] = df_name[col_name].astype(np.int64)
        type_col = df_name[col_name].dtype
        

    print(f">> DONE Coverting to {type_col}\n\n{50*('=')}\n{50*('=')}")
   
    
    return df_name


# In[4]:


def conv_currency (df_name, col_name):
    
    """
    1. Converting "$" to 'USD'
    2. Split column contains "currency" and "number" into 2 columns
        a. <original_column_name>_currency : tag of currency like 'USD', 'EUR', 'INR', etc.
    3. Usage: 
        conv_currency (data-frame-name, column-name)
    """
    df_name[col_name].replace(np.NaN, np.int64(0), inplace=True)
    
    print (f"\n>> Processing Column: '{col_name}'")
    
    # replace $ for USD and remove all "blanks"
    df_name.loc[:,col_name] = df_name.loc[:, col_name].str.replace("$", "USD ")
    df_name.loc[:,col_name] = df_name.loc[:, col_name].str.replace(",", "")
    print(df_name.loc[:,col_name].dtype)
    print(f">> DONE Replacing '$' with 'USD'!")
    
    # split currency and value into two cols
    
    try:
        new_col = f'{col_name}_currency'
        print(f'    >>> Creating new column named: "{new_col}"')
        df_name[new_col], df_name[col_name] = df_name[col_name].str.split(' ', 1).str
        print(df_name.loc[:,col_name].dtype)
        print(df_name.loc[:,new_col].dtype)
        print(f">> DONE Splitting Columns!")
              
    except ValueError:
        pass
    
    df_name[col_name].replace("", np.int64(0), inplace=True)
    print(f">> PROCESS COMPLETED !\n\n{50*('=')}\n{50*('=')}")
    
    return print(f">> PROCESS COMPLETED !\n\n{50*('=')}\n{50*('=')}")


# In[5]:


def replace_str (df_name, col_name, to_be_repl, repl_to):
    
    """
    1. Replace a character to another character
    2. Usage:
        replace_str (data-frame-name, column-name, string-to-replace, replace-to-string):
    """
    print (f"\n>> Processing Column: '{col_name}'")
    
    df_name[col_name] = df_name.loc[:, col_name].str.replace(to_be_repl, repl_to)
    

    print(f">> DONE Replacing Character!\n\n{50*('=')}\n{50*('=')}")
    return df_name.head(10)


# In[6]:


def to_str (df_name, col_name):
    
    """
    1. convert to string
    2. Usage:
        to_str (data-frame-name, column-name)
    """
    print (f"\n>> Processing Column: '{col_name}'")
    
   
    df_name[col_name] = df_name[col_name].astype('str') 
       

    print(f">> DONE Converting to String!\n\n{50*('=')}\n{50*('=')}")
    return df_name.head(10)


# ## Data Clean-up Process

# ### DATABASE RAW_DF

# In[7]:


# define path to csv file
path="Resources_hle\IMDb_movies.csv"

# convert csv to pandas df
raw_df = pd.read_csv(path, encoding="UTF-8", low_memory=False) #, dtype={'usa_gross_income': "string", "worldwide_gross_income" : "string", "budget": "string"})


# 1. choose all cols to keep (netflix id, imdb id, title, ddmmyy, dd, mo,yr,duration, avg_vote, votes, reviews_from_users	reviews_from_critics, budget,usa_gross_icome, ww income, coutry, type, genre, actor, description)
# [[""]]
# 2. break the date published col into ye, mo, dd
# 3. table name messed up worlwide -->> worldwide
# 3. combine reviews
# 4. rename columns
# 5. load into SQL-pgadmin4
# 6. report
#        a. where data found, how
#        b. transforming process
#        c. load SQL, pic of SQL

# In[8]:


# review what imported
raw_df.head(20)


# In[ ]:





# In[9]:


# print out current columns with template to create a dictionary for columns rename
# un-comment to print out the template
# for col in raw_df.columns:
#     print(f'"{col}" : "__",')


# In[10]:


# define what will be renamed
cols = {
"imdb_title_id" : "imdb_id",
"production_company" : "prod_co",
"avg_vote" : "user_rating",
"votes" : "vote_num",
"worlwide_gross_income" : "worldwide_gross_income",
"metascore" : "web_rating"
    }

# process new col names
raw_df.rename(columns=cols, inplace=True)
# raw_df.head(10)


# In[11]:


# # fill empty space
# raw_df.fillna("0")
# raw_df.head(10)


# In[12]:


# print out all current column names
# for col in raw_df.columns:
#     print(f'"{col}",')


# 1. choose all cols to keep (netflix id, imdb id, title, ddmmyy, dd, mo,yr,duration, avg_vote, votes, reviews_from_users	reviews_from_critics, budget,usa_gross_icome, ww income, coutry, type, genre, actor, description)
# [[""]]
# 2. break the date published col into ye, mo, dd
# 3. combine reviews
# 4. rename columns
# 5. load into SQL-pgadmin4
# 6. report
#        a. where data found, how
#        b. transforming process
#        c. load SQL, pic of SQL

# ### DATABASE PROCESSED_DF

# In[13]:


# del processed_df


# In[14]:


# if table exist, delete the table
try:
    del processed_df

except Exception:
    pass

processed_df = raw_df
processed_df


# In[15]:


# replacing "tt" character in id columns and convert id to integer
replace_str(processed_df, "imdb_id", "tt", "")


# In[16]:


# extract day, month, year from the date_published columns
processed_df["date_published"] = pd.to_datetime(processed_df['date_published'])
processed_df['day'], processed_df['month'], processed_df['year']  = processed_df['date_published'].dt.day, processed_df['date_published'].dt.month, processed_df['date_published'].dt.year


# In[17]:


# convert 'id' to numbers
to_int(processed_df, 'imdb_id')


# In[18]:


# for trouble shoot and debugging purposes
# break_point_here


# In[19]:


col_to_covert = ['worldwide_gross_income', 'usa_gross_income', 'budget']


# In[20]:


for ea_col in col_to_covert:
    conv_currency(processed_df, ea_col)
processed_df[['worldwide_gross_income', 'usa_gross_income', 'budget']]


# In[21]:


# create an folder to hole temporarily exported data of converted data
get_ipython().system('mkdir archieve')

# export to csv for visual inspection or further process if needed
processed_df[["worldwide_gross_income_currency", 'worldwide_gross_income', "usa_gross_income_currency", 'usa_gross_income', "budget_currency", 'budget']].to_csv("archieve\exported_draft.csv")


# In[22]:



# print out the column names inside df
# useful as being able to copy and paste directly into cell without retyping all col names
# uncheck to use
# for col in processed_df.columns:
#     print (f'"{col}",')


# In[23]:


print(processed_df.dtypes)


# In[24]:


# specify columns to be converted to string
col_to_str = [
    "imdb_id",
    "title",
    "usa_gross_income_currency",
    "worldwide_gross_income_currency",
    "budget_currency",
    "country",
    "language",
    "genre",
    "director",
    "writer",
    "prod_co",
    "actors",
    "description"    
]

# loop and replace one by one
for col in col_to_str:
    to_str(processed_df, col)


# In[25]:


# specify columns to be converted to integer
col_to_int = [
    "imdb_id",
    "day",
    "month",
    "year",
    "user_rating",
    "web_rating",
    "vote_num",
    "reviews_from_users",
    "reviews_from_critics",
    "usa_gross_income",
    "worldwide_gross_income",
    "budget",
    "duration",
]

# loop and replace one by one
for col in col_to_int:
    to_int(processed_df, col)


# In[26]:


processed_df.dtypes


# 
# web_rating                                 object  - float
# reviews_from_users                         object  -int
# reviews_from_critics                       object    - int
# total_reviews                              object     - int
# usa_gross_income                           object     - int
# worldwide_gross_income                     object     - int
# budget                                     object      - int

# In[27]:


# re-arrange columns in the df
# build a list of what need to be included and their positions
cols=[
"imdb_id",
"title",

"date_published",
"day",
"month",
"year",

"user_rating",
"web_rating",

"vote_num",
"reviews_from_users",
"reviews_from_critics",
    
"usa_gross_income_currency",
"usa_gross_income",

"worldwide_gross_income_currency",
"worldwide_gross_income",

"budget_currency",
"budget",


"duration",
"country",
"language",
"genre",
"director",
"writer",
"prod_co",
"actors",
"description"
]


# re-arrange:
processed_df = processed_df[cols]


# In[28]:


processed_df.to_csv("archieve\processed_df.csv")


# In[29]:


# template to print out all columns and get ready for CLASS creation
# for col in  cols:
#     print (f'{col} = Column(    )')


# In[30]:


# Table export description:
t_shp = processed_df.shape
print(f"TABLE DESCRIPTIONS:\n{('-')*30}\n>>> Number of Rows: {'{:,.0f}'.format(t_shp[0])}\n>>> Number of Columns: {t_shp[1]}")


# In[31]:


# brk_here


# # SQL-Alchemy to load cleaned data SQL Lite DataBase
# ---
# ---

# ### Create Engine & Connection to SQL Lite DB

# In[32]:


# create declarative base
Base = declarative_base()

# check current table available in the Base - should be nothing at this point
Base.metadata.tables


# In[33]:


# folder name that will store the sql-lite database
fol_name = "Exp_SqlLiteDb_test"

# if exist print a message for user
if pathlib.Path(fol_name).exists():
    print(f' >> Folder "{fol_name}" already exists!\n >> No new folder was created ...')
    pass

# if not make a new one and let user know
else:
    get_ipython().system(' mkdir Exp_SqlLiteDb')
    print(f'Successfully created folder "{fol_name}"')


# In[34]:


sqlLite_db_path = "Exp_SqlLiteDb\movie.db"
engine = create_engine(f"sqlite:///{sqlLite_db_path}")
conn = engine.connect()


# In[35]:


engine.execute("DROP TABLE IF EXISTS movie")


# In[36]:


# per docs found online, SQL Lite works up to int8
# while creating this file, I found lots of DataType Mismatch errors
# found this solutions as 2 lines belows to extend SQL to work with int64
# -------------------------------------------------------------
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# In[37]:


# print out list of cols for class creation
# i=0
# for col in processed_df.columns:
#     print(f'{col} = Column()')
#     i+=1
# print(f'\n{("-")*50}\n>> There are total {i} columns in the current data frame.')


# ### Create Template and Load Data from Python to SQL Lite DB

# In[38]:


# class name == 'Movie' with table name 'movie'
# ------------------------------------------------------------------------------------

class Movie(Base):
    
    __tablename__ = 'movie'
    __table_args__ = {'extend_existing': True} 
    
    id = Column(Integer, primary_key=True)
    imdb_id = Column(Integer)
    title = Column(String)
    date_published = Column(Date)
                   
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
                   
    user_rating = Column(Integer)
    web_rating = Column(Integer)
    vote_num = Column(Integer)
    reviews_from_users = Column(Integer)
    reviews_from_critics = Column(Integer)
    
    usa_gross_income_currency = Column(String)
    usa_gross_income = Column(Integer)
    
    worldwide_gross_income_currency = Column(String)
    worldwide_gross_income = Column(Integer)
   
    budget_currency = Column(String)
    budget = Column(Integer)
       
    duration = Column(Integer)
                   
    country = Column(String)
    language = Column(String)
    genre = Column(String)
    director = Column(String)
    writer = Column(String)
    prod_co = Column(String)
    actors = Column(String)
    description = Column(String)


# In[39]:


# Create a "Metadata" Layer That Abstracts our SQL Database
# ----------------------------------
Base.metadata.create_all(engine)


# In[40]:


# current in memory tables
Base.metadata.tables


# In[41]:


# redo again to make sure SQL lite register int64-variables
# -------------------------------------------------------------

sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# In[42]:


# orm requires session so rollbacks can occur etc.
session = Session(bind=engine)


# In[43]:


### Begin looping thru dataframe and load data into template


# In[44]:


# looping over every row of the database and export data into SQL Lite

# ==========================================================

# specify how much data want to load, in fraction
# ---------------------------

print(f">>> There are total: \033[1;31m{'{:,.0f}'.format(t_shp[0])}\033[0;30m Records")
data_load_perc = int(input (f">>> How much data would you like to load?\n>>> HINT: if 20%, input whole number 20\n--->>>User input: "))# in percentage 

total_to_load = data_load_perc * t_shp[0] // 100 # use '//' to get the integer as the next function only accepts integer
print(f">>> Preparing to load \033[1;31m{'{:,.0f}'.format(total_to_load)}\033[0;30m ({data_load_perc}%) Records")

# ==========================================================

values = range(total_to_load)


# In[45]:


# use progress bar to help user keep track of the process
# build the iter-row within this progress bar
# bar update code is inside the iter-row
# =========================================

i = 0
with tqdm(total=len(values)) as pbar:
    for index, row in processed_df.head(n=total_to_load).iterrows():
        
        # calculate the # of loaded data and percentage
       
        i +=1
        perc = round(i / total_to_load * 100, 2)
       
        
        # Print out message for percentage 
        print (f">>> Loading: \033[1;31m{'{:,.0f}'.format(i)}\033[0;30m Records | \033[1;34m{perc}%\033[0;00m Complete", end = "\r", flush=True)
        
        # this is to update the progress bar
        pbar.update(1) 
        
               
        # get the data from cleaned df
        movie = Movie( 
        imdb_id = row['imdb_id'],
        title = row['title'],
        date_published = row['date_published'],
        day = row['day'],
        month = row['month'],
        year = row['year'],
        user_rating = row['user_rating'],
        web_rating = row['web_rating'],
        vote_num = row['vote_num'],
        reviews_from_users = row['reviews_from_users'],
        reviews_from_critics = row['reviews_from_critics'],
        usa_gross_income_currency = row['usa_gross_income_currency'],
        usa_gross_income = row['usa_gross_income'],
        worldwide_gross_income_currency = row['worldwide_gross_income_currency'],
        worldwide_gross_income = row['worldwide_gross_income'],
        budget_currency = row['budget_currency'],
        budget = row['budget'],
        duration = row['duration'],
        country = row['country'],
        language = row['language'],
        genre = row['genre'],
        director = row['director'],
        writer = row['writer'],
        prod_co = row['prod_co'],
        actors = row['actors'],
        description = row['description']
        )
        
        
        # add data to SQL lite session, DB
        session.add(movie)
print(">>> Finished loading all records into memory")


# In[46]:


# commit to hard write onto DB
print(">>> Prepare to write records into SQL Lite DB")
try:
    session.commit()
    print(">>> Successfully wrote all records into SQL Lite DB")
except Exception as errmess:
    print(">>> An Exception has occured ::", str(error))


# In[47]:


# check if records are there, uncomment out to run if desire
# engine.execute("select * from Movie").fetchall()


# In[50]:


# close out session after done loading data into db
session.close()
print(">>> All session(s) closed")


# ## Conver Jupyter Notebook to Python File

# In[49]:


import os
import os.path
from os import path

# define file name
python_file_name = 'hle_SqlLite_load.py'

# if there is already old file, then delete and reprocess a new one
if path.exists('hle_SqlLite_load.py'):
    os.remove('hle_SqlLite_load.py')

# if exception raises, just skip the export process
try:
    get_ipython().system('jupyter nbconvert --to python hle_IMDb.ipynb')
    os.rename("hle_IMDb.py", "SQL_Lite_HLE.py")
except Exception:
    prit(Exception)
    pass

