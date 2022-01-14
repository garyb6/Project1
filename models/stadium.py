class Stadium:

    def __init__(self, name, category, description, city, country, visited, rating, id = None):
        self.name = name
        self.category = category
        self.description = description
        self.city = city 
        self.country = country
        self.visited = visited
        self.rating = rating
        self.id = id 
    


    def mark_visited(self):
        self.visited = True
    
    def change_rating(self):
        self.rating = 2
        