# Emissions & Population Analysis

A Python project that loads global population and CO2 emissions data into a MySQL database and generates visualizations comparing countries over time.

## Data Sources

- **Population data** — `population/population.csv` (World Bank)
- **CO2 emissions data** — `owid-co2-data.csv` ([Our World in Data](https://github.com/owid/co2-data))

## Prerequisites

- Python 3.8+
- MySQL server running locally (or remotely)

## Setup

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Create the database and tables:**

   ```bash
   mysql -u root -p < worldProject.sql
   ```

   (You'll need to create the `world_data` database first: `CREATE DATABASE world_data;`)

3. **Set your database password as an environment variable:**

   ```bash
   export DB_PASSWORD=yourpassword
   ```

   You can also optionally set `DB_HOST`, `DB_USER`, and `DB_NAME` (they default to `localhost`, `root`, and `world_data`).

4. **Load the data into MySQL:**

   ```bash
   python load_data.py
   ```

5. **Generate the charts:**

   ```bash
   python analyze.py
   ```

   This produces three PNG charts in the project directory:
   - `population_chart.png` — Top 10 most populous countries (2021)
   - `co2_chart.png` — Top 10 CO2 emitters per capita (2021)
   - `growth_chart.png` — Population growth for China, India, and the USA since 1960

## Project Structure

```
EmissionsProject/
├── worldProject.sql      # SQL schema (countries, population, co2_emissions tables)
├── load_data.py           # Loads CSV data into MySQL
├── analyze.py             # Queries the database and generates charts
├── requirements.txt       # Python dependencies
├── owid-co2-data.csv      # CO2 emissions dataset
└── population/
    └── population.csv     # World Bank population dataset
```
