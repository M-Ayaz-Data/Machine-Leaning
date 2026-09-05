import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Hours": [5, 7, 3, 6, 8],
    "Attendance": [80, 90, 70, 85, 95],
    "Marks": [65, 82, 48, 75, 88]
})

print(df)

print(df[df["Marks"] > 70])

print(df.iloc[2])

print(df.iloc[1,2]) 