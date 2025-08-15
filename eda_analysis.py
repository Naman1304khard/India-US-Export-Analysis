import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loding cleaned dataset 
df= pd.read_csv("C:\\Users\\hp\OneDrive\\Desktop\\india_us_exports_analysis\\india_us_exports_2015_2022.csv")


# Basic info
print("Shape", df.shape)
print("\nColumn:", df.columns)
print("\nData types:")
print(df.dtypes)


#Converting month name into integer
if df['Month'].dtype == object:
    df['Month'] = pd.to_datetime(df['Month'], format='%B').dt.month


# Combining Year + Month into a date column
df['date'] = pd.to_datetime(df[['Year','Month']].assign(DAY=1))
# Yearly export trend 
yearly_export = df.groupby('Year')['Export_Value_USD'].sum()

plt.figure(figsize=(8,5))
yearly_export.plot(kind='bar', color='purple')
plt.title("India -> Us Yearly Export Value (USD)")
plt.ylabel("Export Value (USD)")
plt.xlabel("Year")
plt.show()


# Monthly export trend
monthly = df.groupby('date')['Export_Value_USD'].sum().reset_index()
plt.figure(figsize=(12,5))
sns.lineplot(data=monthly, x='date', y='Export_Value_USD', marker='o')
plt.title("Monthly Export India -> Usa (USD)")
plt.ylabel("Export Value (USD)")
plt.show()

# Top 10 export sectors
top_sectors = df.groupby('Sector')['Export_Value_USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_sectors.values, y=top_sectors.index, palette='viridis')
plt.title("Top 10 Export Sector (2015-2022)")
plt.xlabel("Export Value (USD)")
plt.show()