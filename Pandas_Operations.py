import pandas as pd 

data = {
    "name":["A","B","C","D","E"],
    "Hours":[5,7,3,6,8],
    "Attendance":[80,90,70,85,95],
    "Marks":[65,82,48,75,88]

}

df = pd.DataFrame(data)
print(df)

print(df.head(2))

print(df.shape)

print(df.info())


print(df["Marks"]) # series

print(df[["Marks"]]) # DataFrame

