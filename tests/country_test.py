import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("England", "Europe", "English", "Where BOJO reigns supreme", False, 3)
    
    
    def test_country_has_name(self):
        self.assertEqual("England", self.country.name)

    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country.continent)

    def test_country_lannguage(self):
        self.assertEqual("English", self.country.language)
    
    def test_country_description(self):
        self.assertEqual("Where BOJO reigns supreme", self.country.description)
    
    def test_country_visited_starts_false(self):
        self.assertEqual(False, self.country.visited)
        
    def test_can_mark_test_complete(self):
        self.country.mark_visited()
        self.assertEqual(True, self.country.visited)
    
    def test_country_rating(self):
        self.assertEqual(3, self.country.rating)
    
    def test_can_change_rating(self):
        self.country.change_rating()
        self.assertEqual(4, self.country.rating)
