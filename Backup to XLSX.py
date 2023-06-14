# Import required libraries 
import pandas as pd
import sqlite3 as sql
import zipfile
import shutil

# Path to backup.nak file
bk = './backup.nak'  
# Path to output Excel file
weight = './weight.xlsx'  
# Temporary directory 
tmp = './tmp'  

# Extract backup.db from backup.nak 
with zipfile.ZipFile(bk,'r') as zip: 
  zip.extract('backup.db', path= tmp)
# Path to extracted database file 
db = './tmp/backup.db'  

# Query database and store in DataFrame 
with sql.connect(db) as conn:
  sql_query = pd.read_sql_query("SELECT timestamp, value FROM rush_com_mc_miband1_model2_Weight", conn)
df = pd.DataFrame(sql_query)
conn.close()  

# Convert timestamp to DD/MM/YYYY 
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms').dt.strftime('%d/%m/%Y')
df.sort_values(by='timestamp', inplace = True)   

# Export to Excel 
df.to_excel(weight, index=False)  

# Delete temporary directory
shutil.rmtree(tmp)