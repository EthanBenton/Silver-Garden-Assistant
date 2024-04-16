import pandas as pd
import sqlite3

# change file name accordingly
inputFile = f"../../data_input_sim/src/sensor_data.json"

dataFrame = pd.read_json(inputFile)

# connect
database = "priaData.db"
conn = sqlite3.connect(database)

# write
table = "sensorData"
dataFrame.to_sql(table, conn, index=False, if_exists="replace")

conn.close()