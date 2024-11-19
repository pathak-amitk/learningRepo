import pandas as pd
print("Hello")

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

#Create a DataFrame from List
df = pd.DataFrame(data, columns=['student_id', 'age'])
#print(df)

#Get the Size of a DataFrame
#print(df.shape)

#Display the First Three Rows
#print(df.head(3))

#Select Data
#print(df[df['student_id'] == 4][[ 'age']])
#print(df.loc[df['student_id']== 4, ['age']])

#Create a New Column
# print(df.assign(double_age=df['age']*2))

#Drop Duplicate Rows
#print(df.drop_duplicates(subset="age", keep='first'))

#Drop Missing Data
#print(df.dropna(subset="age"))

#Modify Columns
df.age = df.age*2
print(df)