import pandas as pd
import mysql.connector

# --- UPDATE THIS ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Louie114",
    database="world_data"
)
cursor = conn.cursor()

# --- Load population CSV ---
pop_df = pd.read_csv(r"/Users/nathankostynick/EmissionsProject/population/population.csv")
pop_df.columns = ['country_name', 'country_code', 'year', 'population']
pop_df = pop_df.dropna(subset=['country_code', 'population'])
pop_df['population'] = pop_df['population'].astype(int)


# --- Load CO2 CSV ---
co2_df = pd.read_csv(r"/Users/nathankostynick/EmissionsProject/owid-co2-data.csv")
co2_df = co2_df[['country', 'iso_code', 'year', 'co2', 'co2_per_capita']]
co2_df.columns = ['country_name', 'country_code', 'year', 'co2', 'co2_per_capita']
co2_df = co2_df.dropna(subset=['country_code'])

# --- Insert countries (unique list from population file) ---
print("Inserting countries...")
countries = pop_df[['country_name', 'country_code']].drop_duplicates()
for _, row in countries.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO countries (country_code, country_name)
        VALUES (%s, %s)
    """, (row['country_code'], row['country_name']))
conn.commit()
print(f"  {len(countries)} countries inserted")

# --- Insert population rows ---
print("Inserting population data...")
count = 0
for _, row in pop_df.iterrows():
    cursor.execute("""
        INSERT INTO population (country_code, year, population)
        VALUES (%s, %s, %s)
    """, (row['country_code'], int(row['year']), int(row['population'])))
    count += 1
conn.commit()
print(f"  {count} rows inserted")

# --- Insert CO2 rows (only where country_code exists in countries table) ---
print("Inserting CO2 data...")
count = 0
for _, row in co2_df.iterrows():
    co2_val = None if pd.isna(row['co2']) else float(row['co2'])
    per_cap_val = None if pd.isna(row['co2_per_capita']) else float(row['co2_per_capita'])
    cursor.execute("""
        INSERT IGNORE INTO co2_emissions (country_code, year, co2, co2_per_capita)
        VALUES (%s, %s, %s, %s)
    """, (row['country_code'], int(row['year']), co2_val, per_cap_val))
    count += 1
conn.commit()
print(f"  {count} rows inserted")

cursor.close()
conn.close()
print("Done!")






