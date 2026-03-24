import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

print("Dataset of Iris: ")
print(df.head())
print("Shape:", df.shape[0], "rows,", df.shape[1], "columns\n")

print("Statistics:")
print(df.describe())
print("\n")

print("Column Stats:")
for col in df.select_dtypes(include='number').columns:
    print(col + " : ")
    print("Mean : ", round(df[col].mean(), 2))
    print("Median : ", round(df[col].median(), 2))
    print("Min : ", round(df[col].min(), 2))
    print("Max : ", round(df[col].max(), 2))
    print("Std : ", round(df[col].std(), 2))
    print()

print("Missing Values:")
missing = df.isnull().sum()
if missing.sum() == 0:
    print("No missing values!")
else:
    print(missing[missing > 0])