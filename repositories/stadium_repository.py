from db.run_sql import run_sql

from models.country import Country
from models.stadium import Stadium
import repositories.country_repository as country_repository 

def save(stadium):
    sql = "INSERT INTO stadiums (name, category, country_id, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [stadium.name, stadium.category, stadium.country.id, stadium.visited]
    results = run_sql(sql, values)
    stadium.id = results[0]['id']
    return stadium 

def select_all():
    stadiums = []
    sql = "SELECT * FROM stadiums"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        stadium = Stadium(row['name'], row['category'], country, row['visited'], row['id'])
        stadiums.append(stadium)
    return stadiums 

def select(id):
    stadium = None
    sql = "SELECT * FROM stadiums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result['country_id'])
        stadium = Stadium(result['name'], result['category'], country, result['visited'], result['id'])
    return stadium 

def delete_all():
    sql = "DELETE FROM stadiums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM stadiums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(stadium):
    sql = "UPDATE stadiums SET (name, category, country_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [stadium.name, stadium.category, stadium.country.id, stadium.visited, stadium.id]
    run_sql(sql, values)

def select_visited():
    stadiums = []
    sql = "SELECT * FROM stadiums WHERE visited = 'TRUE'"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        stadium = Stadium(row['name'], row['category'], country, row['visited'], row['id'])
        stadiums.append(stadium)
    return stadiums 