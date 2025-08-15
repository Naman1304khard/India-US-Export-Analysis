import pandas as pd 
 
# Loding Dataset

df = pd.read_csv("C:\\Users\\hp\OneDrive\\Desktop\\india_us_exports_analysis\\india_us_exports_2015_2022.csv")

print("First 5 rows of data:")
print(df.head())

# Removing duplicates value
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(how='all', inplace=True) #remove fully empty rows 
df.fillna(0,inplace=True) #replace missing numeric values with 0

# Standardize column names (lowercase, no space)
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

#Saving cleaned dataset
df.to_csv("india_us_exports_2015_2022_cleaned.csv", index=False)

print("\n Dataset cleaned and saved as india_us_export_2015_2022_cleaned.csv")