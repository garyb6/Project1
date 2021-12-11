import unittest
from models.stadium import Stadium

class TestStadium(unittest.TestCase):
    
    def setUp(self):
        self.stadium = Stadium("St James' Park", "Football", "England", True)
    
    
    def test_stadium_has_name(self):
        self.assertEqual("St James' Park", self.stadium.name)
        
        
    def test_stadium_type(self):
        self.assertEqual("Football", self.stadium.type)

        
    # def test_task_has_duration(self):
    #     self.assertEqual(60, self.task.duration)
    
    
    # def test_task_completed_starts_false(self):
    #     self.assertEqual(False, self.task.completed)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)