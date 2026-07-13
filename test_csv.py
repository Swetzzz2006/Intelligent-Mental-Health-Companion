import pandas as pd

df = pd.read_csv("data/mood_dataset.csv")

print("Columns:")
print(df.columns)

print("\nData:")
print(df)

print("\nLast Row:")
print(df.iloc[-1])