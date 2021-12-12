from db.run_sql import run_sql

from models.country import Country
from models.stadium import Stadium
import repositories.stadium_repository as stadium_repository 

# def save(country):
#     sql = "INSERT INTO countries (name, language, visited) VALUES (%s, %s, %s) RETURNING *"
#     values = [country.name, country.language, country.visited]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     country.id = id
#     return country 

def select_all():
    stadiums = []
    sql = "SELECT * from stadiums"
    results = run_sql(sql)
    for row in results:
        stadium = Stadium(row['name'], row['category'], row['country'], row['visited'], row['id'])
        stadiums.append(stadium)
    return stadiums 