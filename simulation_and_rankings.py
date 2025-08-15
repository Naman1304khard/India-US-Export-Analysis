import pandas as pd
import numpy as np
import matplotlib .pyplot as plt

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\india_us_exports_analysis\\india_us_exports_2015_2022_cleaned.csv")

# Ensure numeric
df['export_value_usd'] = pd.to_numeric(df['export_value_usd'], errors= 'coerce').fillna(0)
df['quantity_tons'] = pd.to_numeric(df['quantity_tons'], errors='coerce').fillna(0)


# Derived columns
df['unit_price_usd_per_Ton'] = np.where(df['quantity_tons']>0,df['export_value_usd']/df['quantity_tons'],0)

df['export_share_percent'] = df['export_value_usd'] / df['export_value_usd'].sum() * 100

# Simulation: apply 50% tariff -> immediate revenue loss= export_value * 0.5
tariff_rate = 50.0
df['simulated_tariff_rate'] = tariff_rate
df['simulated_loss_usd'] = df['export_value_usd'] * (df['historical_average_tariff_rate_percent'] / 100.0)

# Aggregated sector and state level
sector_loss = df.groupby('sector')['simulated_loss_usd'].sum().reset_index().sort_values('simulated_loss_usd', ascending=False)
state_loss = df.groupby('state_of_origin')['simulated_loss_usd'].sum().reset_index().sort_values('simulated_loss_usd', ascending=False)


# Saving results
sector_loss.to_csv("top_sector_loss_50pct.csv", index=False)
state_loss.to_csv("top_state_loss_50pct.csv", index=False)
