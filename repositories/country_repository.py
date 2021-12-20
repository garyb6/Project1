from db.run_sql import run_sql

from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, continent, language, description, visited, rating) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [country.name, country.continent, country.language, country.description, country.visited, country.rating]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['continent'], row['language'], row['description'], row['visited'], row['rating'], row['id'])
        countries.append(country)
    return countries 

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        country=Country(result['name'], result['continent'], result['language'], result['description'], result['visited'], result ['rating'], result['id'])
    return country 

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, continent, language, description, visited, rating) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.language, country.description, country.visited, country.rating, country.id]
    run_sql(sql, values)

def select_visited():
    countries = []
    sql = "SELECT * FROM countries WHERE visited = TRUE"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['continent'], row['language'], row['description'], row['visited'], row['rating'], row['id'])
        countries.append(country)
    return countries 

def select_to_visit():
    countries = []
    sql = "SELECT * FROM countries WHERE visited = 'FALSE'"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['continent'], row['language'], row['description'], row['visited'], row['rating'], row['id'])
        countries.append(country)
    return countries 