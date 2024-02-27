import pandas as pd
import sqlite3

fileExtension = "csv"
# change file name accordingly
inputFile = f"../../data-input-sim/src/sensorData.csv"

dataFrame = pd.read_csv(inputFile)

# connect
database = "priaData.db"
conn = sqlite3.connect(database)

# write
table = "sensorData"
dataFrame.to_sql(table, conn, index=False, if_exists="replace")

conn.close()