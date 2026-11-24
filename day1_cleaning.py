import pandas as pd

# 1. Load
df = pd.read_csv('sales_dirty.csv')
print("BEFORE:")
print(df)

# 2. Drop duplicates
df = df.drop_duplicates()

# 3. Drop rows where sales is missing
df = df.dropna(subset=['sales'])

# 4. Fix dates - bad dates become NaT, then drop them
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])

# 5. Fill missing region
df['region'] = df['region'].fillna('Unknown')

# 6. Groupby - total sales per product
result = df.groupby('product')['sales'].sum()
print("\nAFTER CLEANING:")
print(df)
print("\nTOTAL SALES PER PRODUCT:")
print(result)