import unittest
from models.stadium import Stadium

class TestStadium(unittest.TestCase):
    
    def setUp(self):
        self.stadium = Stadium("St James' Park", "Football", "The best place on Earth", "Newcastle", "England", False, 5)
    
    def test_stadium_has_name(self):
        self.assertEqual("St James' Park", self.stadium.name)
        
    def test_stadium_category(self):
        self.assertEqual("Football", self.stadium.category)
    
    def test_stadium_description(self):
        self.assertEqual("The best place on Earth", self.stadium.description)

    def test_stadium_has_city(self):
        self.assertEqual("Newcastle", self.stadium.city)

    def test_stadium_has_country(self):
        self.assertEqual("England", self.stadium.country)
    
    def test_stadium_visited_starts_false(self):
        self.assertEqual(False, self.stadium.visited)
    
    def test_can_mark_test_complete(self):
        self.stadium.mark_visited()
        self.assertEqual(True, self.stadium.visited)
    
    def test_stadium_rating(self):
        self.assertEqual(5, self.stadium.rating)

    # def test_change_rating(self):
    #     self.stadium.change_rating()
    #     self.assertEqual(2, self.stadium.rating)
