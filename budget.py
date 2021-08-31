import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "departament": ["dev", "hr", "adm", "fin", "sup", "log", "mgm", "acc", "rep", "hlp"],
    "budget": [50, 60, 100, 150, 70, 100, 30, 80, 40, 50],
    "expenses": [46.5, 59.0, 105.3, 163.9, 69.96, 97.7, 30.05, 72.2, 45.1, 23.4]

}

df = pd.DataFrame(data)

df = df.set_index('id')
df.loc['Total'] = df.sum(numeric_only=True, axis=0)
df.loc[:, 'Balance'] = df['budget'] - df['expenses']
print(df)


# data = {
#     "departament": ["dev", "hr", "adm", "fin", "sup", "log", "mgm", "acc", "rep", "hlp"],
#     "budget": [50, 60, 100, 150, 70, 100, 30, 80, 40, 50],
#     "expenses": [46.5, 59.0, 105.3, 163.9, 69.96, 97.7, 30.05, 72.2, 45.1, 23.4]
#
# }
#
# df = pd.DataFrame.from_dict(data)
#
# df = df.set_index('departament')
# df.loc[:, 'balance'] = df['budget'] - df['expenses']
# print(df)
