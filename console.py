from models.stadium import Stadium
from models.country import Country

import repositories.stadium_repository as stadium_repository
import repositories.country_repository as country_repository 

stadium_repository.delete_all() 
country_repository.delete_all() 


country1 = Country("Australia", "English", False)
country_repository.save(country1)

country2 = Country("Portugal", "Portuguese", True)
country_repository.save(country2)

country3 = Country("Germany", "German", True)
country_repository.save(country3)

stadium1 = Stadium("The Gabba", "Cricket", country1, False)
stadium_repository.save(stadium1)

stadium2 = Stadium("Estádio do Dragão", "Football", country2, False)
stadium_repository.save(stadium2)

stadium3 = Stadium("Allianz Arena", "Football", country3, False)
stadium_repository.save(stadium3)

stadium4 = Stadium("Red Bull Arena", "Football", country3, False)
stadium_repository.save(stadium4) 


