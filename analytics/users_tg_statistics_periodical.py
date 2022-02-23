import pandas as pd

days = [day for day in range(12, 20)]

dataframe = pd.read_csv(f"history_activity/02.2022/Day 11.csv", index_col="user_id")
names = dataframe[["name"]]
for day in days:
    new_data = pd.read_csv(f'history_activity/02.2022/Day {day}.csv', index_col="user_id")
    names = pd.concat(
        (names, new_data[["name"]]), axis=0
    )
    dataframe = pd.concat([dataframe, new_data], axis=0).groupby(['user_id'], axis=0).agg('sum')

dataframe = pd.merge(dataframe, names, on="user_id", how="left")[
    ["name", "m", "r", "total"]
].drop_duplicates().sort_values('total', ascending=False).rename(columns={"total": "t"})

dataframe, new_players = dataframe[(dataframe.t > 0)], dataframe[(dataframe.t == 0)][["name"]]

dataframe.to_csv("statistics_activity.csv", index_label="user_id")
dataframe.to_markdown("statistics_activity.md", index=False)
new_players.to_markdown("statistics_new_players.md")
