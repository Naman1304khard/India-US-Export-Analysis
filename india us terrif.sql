-- CREATE DATABASE exports_db;
USE exports_db; 

-- Total exports by year
SELECT Year, SUM(Export_Value_USD) as total_usd
FROM india_us_exports_2015_2022
GROUP BY Year
ORDER BY Year;

-- Top 10 sector by export value (all year)
SELECT Sector, SUM(Export_Value_USD) as total_usd
FROM india_us_exports_2015_2022
GROUP BY Sector
ORDER BY total_usd DESC
LIMIT 10;

-- State-wise simulated loss (50% tariff)
SELECT State_of_Origin, SUM(Export_Value_USD)*0.5 as simulated_loss_usd
FROM india_us_exports_2015_2022
GROUP BY State_of_Origin
ORDER BY simulated_loss_usd DESC
Limit 10;

-- Monthly sesonability example (avg exports by month)
SELECT Month, AVG(Export_Value_USD) as avg_usd
FROM india_us_exports_2015_2022
GROUP BY Month
ORDER BY Month;










