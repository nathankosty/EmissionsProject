USE world_data;

CREATE TABLE countries (
    country_code VARCHAR(10) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL
);

CREATE TABLE population (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_code VARCHAR(10),
    year INT,
    population BIGINT,
    FOREIGN KEY (country_code) REFERENCES countries(country_code)
);

CREATE TABLE co2_emissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_code VARCHAR(10),
    year INT,
    co2 FLOAT,
    co2_per_capita FLOAT,
    FOREIGN KEY (country_code) REFERENCES countries(country_code)
);