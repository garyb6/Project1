class Country:

    def __init__(self, name, language, visited, id = None):
        self.name = name
        self.language = language
        self.visited = visited
        self.id = id 
    
    def mark_visited(self):
        self.visited = True 