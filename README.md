# Notify for Amazfit Weight Data Extractor

This is an as-is Python script that extracts weight data from a backup.nak file created by the Notify app for Amazfit smartbands.
It should also work with Notify for Mi Band, but has not been tested.

# Usage
Install Pandas by running:
    
    pip install pandas 
    or
    pip install -r requirements.txt
    
Make sure you have the backup.nak file from the Notify app in the same folder as the script. It can be easily created in the app side menu > export backup file
    
Run "Backup to XLSX.py" and a file named weight.xlsx should be created in the same folder.
    
This script will convert the timestamps from unix time to DD-MM-YYYY but can be changed in the code if another format is needed.
