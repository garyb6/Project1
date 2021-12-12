class Stadium:

    def __init__(self, name, category, country, visited, id = None):
        self.name = name
        self.category = category
        self.country = country
        self.visited = visited
        self.id = id 
    
    def mark_visited(self):
        self.visited = True