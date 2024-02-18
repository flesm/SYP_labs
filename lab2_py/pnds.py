import pandas as pd

sales_df1 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
sales_df1["MoreThan500"] = ["Yes" if x > 500 else "No" for x in sales_df1["Sales"]]
# print(sales_df1)

sales_df2 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
states_df = pd.read_excel('pythonexcel.xlsx', sheet_name='states')
sales = sales_df2.merge(states_df, on="City", how="left")
# print(sales)


sales_df3 = pd.read_excel('pythonexcel.xlsx', sheet_name='sales')
pivot = sales_df3.pivot_table(values="Sales", index="City", aggfunc="sum")
print(pivot)