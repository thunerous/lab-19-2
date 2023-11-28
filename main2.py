import pandas as pd
import json

with open('digits.json', 'r') as file:
    data = json.load(file)

series1 = pd.Series(data[0])
series2 = pd.Series(data[1])

uniq_lists = [lst for lst in series1 if lst not in series2.tolist() or series1.tolist().count(lst) != series2.tolist().count(lst)]
uniq = pd.Series(uniq_lists)
uniq.to_json('uniq.json')
