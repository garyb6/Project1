DROP TABLE IF EXISTS stadiums;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    languages VARCHAR(255)
    visited BOOLEAN
);

CREATE TABLE stadiums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id)
    );