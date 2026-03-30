import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection — set DB_PASSWORD environment variable before running
db_password = os.environ["DB_PASSWORD"]
db_user = os.environ.get("DB_USER", "root")
db_host = os.environ.get("DB_HOST", "localhost")
db_name = os.environ.get("DB_NAME", "world_data")
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

# --- Chart 1: Top 10 most populous countries in 2021 ---
pop_query = """
    SELECT c.country_name, p.population
    FROM population p
    JOIN countries c ON p.country_code = c.country_code
    WHERE p.year = 2021
    AND LENGTH(c.country_code) = 3
    ORDER BY p.population DESC
    LIMIT 10;
"""
pop_df = pd.read_sql_query(pop_query, engine)
pop_df['population'] = pop_df['population'] / 1_000_000

plt.figure(figsize=(12, 6))
plt.barh(pop_df['country_name'][::-1], pop_df['population'][::-1], color='steelblue')
plt.xlabel("Population (millions)")
plt.title("Top 10 most populous countries (2021)")
plt.tight_layout()
plt.savefig(BASE_PATH + "population_chart.png")
plt.show()
print("Chart 1 saved!")

# --- Chart 2: Top 10 CO2 emitters per capita in 2021 ---
co2_query = """
    SELECT c.country_name, e.co2_per_capita
    FROM co2_emissions e
    JOIN countries c ON e.country_code = c.country_code
    WHERE e.year = 2021
    AND e.co2_per_capita IS NOT NULL
    AND LENGTH(c.country_code) = 3
    ORDER BY e.co2_per_capita DESC
    LIMIT 10;
"""
co2_df = pd.read_sql_query(co2_query, engine)

plt.figure(figsize=(12, 6))
plt.barh(co2_df['country_name'][::-1], co2_df['co2_per_capita'][::-1], color='coral')
plt.xlabel("CO2 per capita (tonnes)")
plt.title("Top 10 CO2 emitters per capita (2021)")
plt.tight_layout()
plt.savefig(BASE_PATH + "co2_chart.png")
plt.show()
print("Chart 2 saved!")

# --- Chart 3: Population growth over time ---
growth_query = """
    SELECT c.country_name, p.year, p.population
    FROM population p
    JOIN countries c ON p.country_code = c.country_code
    WHERE c.country_code IN ('USA', 'CHN', 'IND')
    AND p.year >= 1960
    ORDER BY p.year;
"""
growth_df = pd.read_sql_query(growth_query, engine)
growth_df['population'] = growth_df['population'] / 1_000_000

plt.figure(figsize=(12, 6))
for country in growth_df['country_name'].unique():
    data = growth_df[growth_df['country_name'] == country]
    plt.plot(data['year'], data['population'], label=country, linewidth=2)

plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.title("Population growth: China, India, USA (1960-present)")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_PATH + "growth_chart.png")
plt.show()
print("Chart 3 saved!")
