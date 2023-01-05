from pathlib import Path
import sqlite3
import pandas as pd


conn = sqlite3.connect('companies.db')
companies = pd.read_csv('companies.csv')
companies.to_sql('companies', conn , if_exists='append', index=False)

