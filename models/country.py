class Country:

    def __init__(self, name, language, review, visited, id = None):
        self.name = name
        self.language = language
        self.review = review
        self.visited = visited
        self.id = id 
    
    def mark_visited(self):
        self.visited = True 