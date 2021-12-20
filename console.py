from models.stadium import Stadium
from models.country import Country

import repositories.stadium_repository as stadium_repository
import repositories.country_repository as country_repository 

# stadium_repository.delete_all() 
# country_repository.delete_all() 


country1 = Country("Australia", "Oceania", "English", "Kings of the Ashes unfortunately", False, 2)
country_repository.save(country1)

country2 = Country("Portugal", "Europe", "Portuguese", "Home of the Algarve", True, 4)
country_repository.save(country2)

country3 = Country("Germany", "Europe", "German", "Best football stadiums in the world", True, 5)
country_repository.save(country3)

stadium1 = Stadium("The Gabba", "Cricket", "Australia's fortress", "Brisbane", country1, False, 5)
stadium_repository.save(stadium1)

stadium2 = Stadium("Estádio do Dragão", "Football", "Stadium of Light", "Porto", country2, False, 3)
stadium_repository.save(stadium2)

stadium3 = Stadium("Allianz Arena", "Football", "Home of the Champions", "Munich", country3, False, 4)
stadium_repository.save(stadium3)

stadium4 = Stadium("Red Bull Arena", "Football", "Commercialisation of football", "Leipzig", country3, False, 1)
stadium_repository.save(stadium4) 


