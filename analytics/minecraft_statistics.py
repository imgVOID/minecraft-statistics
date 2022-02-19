import pandas as pd

df = pd.read_csv("history_activity/02.2022/Day 19.csv", index_col='id')
df["login"] = df["login"].str.replace("\\", "")
df["ads_source"] = df["ads_source"].str.replace("\\", "")
df["launched_at"] = pd.to_datetime(df['launched_at'])
df = df[(df['launched_at'] > "2018-01-01")]
print(df)
