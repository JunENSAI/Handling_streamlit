import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("portfolio.db")
c = conn.cursor()

# 1. Create Tables
c.execute('CREATE TABLE IF NOT EXISTS bitcoin (date DATE, price REAL, volume INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS dogecoin (source TEXT, allocated INTEGER, spent INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS ethereum (source TEXT, allocated INTEGER, spent INTEGER)')

# 2. Insert Mock Data for Bitcoin (Time Series)
dates = pd.date_range(start="2025-01-01", periods=20, freq="D")
prices = np.random.uniform(40000, 45000, size=20)
for d, p in zip(dates, prices):
    c.execute('INSERT INTO bitcoin VALUES (?, ?, ?)', (d.strftime("%Y-%m-%d"), p, np.random.randint(1000, 5000)))

# 3. Insert Mock Data for Dogecoin & Ethereum (Categorical)
doge_data = [('Investors', 30000, 25000), ('Exchanges', 15000, 10000), ('Merchants', 5000, 2000)]
eth_data = [('Investors', 1200, 250), ('Exchanges', 1500, 1000), ('Merchants', 5000, 2200)]

c.executemany('INSERT INTO dogecoin VALUES (?,?,?)', doge_data)
c.executemany('INSERT INTO ethereum VALUES (?,?,?)', eth_data)

conn.commit()
conn.close()
print("Database 'portfolio.db' created successfully!")