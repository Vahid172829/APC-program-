import pandas as pd

data = {
    "Name": ["Shreyash", "Siddhu", "Rahul", "Prathmesh"],
    "Marks": [85, None, 78, None],
    "Age": [20, 21, None, 20]
}

df = pd.DataFrame(data)

print("Before:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter replacing:")
print(df)
