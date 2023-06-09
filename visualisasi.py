import pandas as pd
import sqlite3

data = "csv_data/data_sesuai.csv"
df = pd.read_csv(data, encoding="latin1")
df