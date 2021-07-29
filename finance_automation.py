import numpy as np
import pandas as pd
from datetime import datetime

file = pd.read_csv("Docs/N26_Juni.csv")
balance = file["Amount (EUR)"].sum()

print(file)
print("______________________")
print("El balance del mes de ")

file['month'] = pd.DatetimeIndex(file['Date']).month
print(file['month'][0:1])
print(str(file['month'][0:1]))
month = datetime.strptime(file['month'][0:1], '%b').date()
print(month)