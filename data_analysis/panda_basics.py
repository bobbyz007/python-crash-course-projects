import pandas as pd
import numpy as np

# Series
obj = pd.Series([4, 7, -5, 3])
print(obj)

obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
print(obj2)
print(obj2[obj2 > 0])

sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj3 = pd.Series(sdata)
print(obj3)
states = ["California", "Ohio", "Oregon", "Texas"]
obj4 = pd.Series(sdata, index=states)
print(obj4.isna())
print(obj3 + obj4) # like join operation in database
print()

# DataFrame
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head()) # first 5 rows
print(frame["state"]) # retrieve series
print(frame.year) # retrieve series

frame["debt"] = 16.5
print(frame)
frame["debt"] = np.arange(6.)
print(frame)
print()
val = pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
frame["debt"] = val
print(frame)

populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},"Nevada": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(populations) # from nested dictionary
print(frame3) # outer keys as columns, inner keys as row indices
print(frame3.T) # transposing
