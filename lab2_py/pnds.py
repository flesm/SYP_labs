import pandas as pd

# реалізаваць функцыю IF Excel праз pandas
sales_df1 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
sales_df1["MoreThan500"] = ["Yes" if x > 500 else "No" for x in sales_df1["Sales"]]
print(sales_df1.head(5), "\n")

# рэалізаваць функцыю VLOOKUP Excel праз pandas
sales_df2 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
states_df = pd.read_excel('pythonexcel.xlsx', sheet_name='states')
sales = sales_df2.merge(states_df, on="City", how="left")
print(sales.head(5), "\n")

# рэалізаваць функцыяна зводных табліцаў Excel праз pandas
sales_df3 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
pivot = sales_df3.pivot_table(values="Sales", index="City", aggfunc="sum")
print(pivot, "\n")

# задача на дыапазон датаў у pandas
# можна замест periods указаца end = "2024-01-01"
dates = pd.date_range(start="2023-12-12", periods=21, freq="D")
print(dates, "\n")

# задача на знвходжанне месяца даты ў pandas
# dates = pd.Series(['2020-05-18', '2020-08-20', '2020-12-21'])
# dates = pd.to_datetime(dates)
# months = dates.dt.month
# print(months, "\n")

# спосаб вышэй -- рашэнне дадзенай задачы праз серыю, гэты праз датафрэйм
df = pd.DataFrame({'sales_date': ['2020-05-18', '2020-08-20', '2020-12-21'], 'total_sales': [675, 500, 575]})
df['month'] = pd.DatetimeIndex(df['sales_date']).month
print(df, "\n")


# пераўтварэнне адметкі часу ў дату і час
timestamps = pd.Series([1577836800, 1581609600, 1583625600, 1585699200, 1588876800])
datetimes = pd.to_datetime(timestamps, unit="s")
print(datetimes)
