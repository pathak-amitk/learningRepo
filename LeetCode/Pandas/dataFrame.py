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

#Fill Missing Data
#products['quantity']=products['quantity'].fillna(0)

#Reshape Data: Concatenate
#print(pd.concat([df1, df2]))

#Reshape Data: Pivot
#return weather.pivot(index="month", columns="city", values="temperature")

#Reshare Data: Melt
#return report.melt(id_vars=["product"], value_vars=["quarter_1","quarter_2","quarter_3","quarter_4"], var_name="quarter", value_name="sales")

#Method Chaining
# print(animals[animals["weight"]>100].sort_values(by=["weight"], ascending=False)[["name"]])