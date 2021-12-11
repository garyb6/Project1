import unittest
from models.stadium import Stadium

class TestStadium(unittest.TestCase):
    
    def setUp(self):
        self.stadium = Stadium("St James' Park", "Football", "England", False)
    
    
    def test_stadium_has_name(self):
        self.assertEqual("St James' Park", self.stadium.name)
        
        
    def test_stadium_type(self):
        self.assertEqual("Football", self.stadium.type)

        
    def test_stadium_has_country(self):
        self.assertEqual("England", self.stadium.country)
    
    def test_stadium_visited_starts_false(self):
        self.assertEqual(False, self.stadium.visited)
    
    def test_can_mark_test_complete(self):
        self.stadium.mark_visited()
        self.assertEqual(True, self.stadium.visited)