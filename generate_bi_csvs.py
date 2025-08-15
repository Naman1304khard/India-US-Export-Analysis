import pandas as pd

#Loding the clean datasets
df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\india_us_exports_analysis\\india_us_exports_2015_2022_cleaned.csv")

# Ensureing numeric columns
df['export_value_usd'] = pd.to_numeric(df['export_value_usd'],errors='coerce').fillna(0)
df['quantity_tons'] = pd.to_numeric(df['quantity_tons'],errors='coerce').fillna(0)

# bi_sector_year.csv
sector_year = df.groupby(['sector', 'year'])['export_value_usd'].sum().reset_index()
sector_year.to_csv("bi_sector_year.csv",index=False)

# bi_state_sector.csv
state_sector = df.groupby(['state_of_origin', 'sector'])['export_value_usd'].sum().reset_index()
state_sector.to_csv("bi_state_sector.csv", index=False)

# bi_monthly.csv
monthly = df.groupby(['year', 'month'])['export_value_usd'].sum().reset_index()
monthly.to_csv("bi_monthly.csv", index=False)

#bi_sector_loss_50.csv
# Simulated loss with 50% tariff
tariff_rate = 50.0
sector_loss = df.groupby('sector')['export_value_usd'].sum().reset_index()
sector_loss['simulated_loss_usd'] = sector_loss['export_value_usd'] *(tariff_rate / 100)
sector_loss.to_csv("bi_sector_loss_50.csv", index=False)

# bi_state_loss_50.csv
state_loss = df.groupby('state_of_origin')['export_value_usd'].sum().reset_index()
state_loss['simulated_loss_usd'] = state_loss['export_value_usd'] * (tariff_rate / 100)
state_loss.to_csv("bi_state_loss_50.csv", index=False)

print("All 5 CSV files have been created successfully.")
