# Emissions & Population Analysis

A Python project that loads global population and CO2 emissions data into a MySQL database and generates visualizations comparing countries over time.

## Data Sources

- **Population data** — `population/population.csv` (World Bank)
- **CO2 emissions data** — `owid-co2-data.csv` ([Our World in Data](https://github.com/owid/co2-data))

## Database Schema

```mermaid
erDiagram
    countries {
        varchar country_code PK
        varchar country_name
    }
    population {
        int id PK
        varchar country_code FK
        int year
        bigint population
    }
    co2_emissions {
        int id PK
        varchar country_code FK
        int year
        float co2
        float co2_per_capita
    }
    countries ||--o{ population : has
    countries ||--o{ co2_emissions : has
```

## Visualizations

Running `analyze.py` produces five charts:

### Top 10 Most Populous Countries (2021)
![Population Chart](population_chart.png)

### Top 10 CO2 Emitters Per Capita (2021)
![CO2 Per Capita Chart](co2_chart.png)

### Population Growth: China, India, USA (1960–Present)
![Population Growth Chart](growth_chart.png)

### CO2 Emissions Over Time: China, India, USA (1960–Present)
![CO2 Growth Chart](co2_growth_chart.png)

### Population vs Total CO2 Emissions (2021)
![Scatter Chart](scatter_chart.png)

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
