from models.stadium import Book
from models.country import Country

import repositories.stadium_repository as stadium_repository
import repositories.country_repository as country_repository 

stadium_repository.delete_all() 
country_repository.delete_all() 

