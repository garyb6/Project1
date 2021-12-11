import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("England", "English", False)
    
    
    def test_country_has_name(self):
        self.assertEqual("England", self.country.name)
        
        
    def test_country_lannguage(self):
        self.assertEqual("English", self.country.language)
    
    def test_country_visited_starts_false(self):
        self.assertEqual(False, self.country.visited)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)