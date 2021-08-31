import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])
print(df1)
print()
print(df1.mean())
print(df1.mean().mean())
print(f'Price: {df1.Price.mean()}')
print(f'Max Price: {df1.Price.max()}')
print()

df2 = pandas.DataFrame([{"Name": "John"}, {"Name": "Jack"}])
print(df2)
