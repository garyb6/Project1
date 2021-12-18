class Country:

    def __init__(self, name, continent, language, description, visited, rating, id = None):
        self.name = name
        self.continent = continent
        self.language = language
        self.review = description
        self.visited = visited
        self.rating = rating
        self.id = id 
    
    def mark_visited(self):
        self.visited = True 