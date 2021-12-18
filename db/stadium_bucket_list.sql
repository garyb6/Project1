DROP TABLE IF EXISTS stadiums;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255),
    language VARCHAR(255),
    description TEXT,
    visited BOOLEAN,
    rating FLOAT,
);

CREATE TABLE stadiums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    description TEXT,
    city VARCHAR(255),
    country_id INT REFERENCES countries(id)
    visited BOOLEAN,
    rating FLOAT, 
    );